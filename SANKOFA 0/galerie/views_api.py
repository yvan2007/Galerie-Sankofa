"""Vues API REST pour Galerie Sankofa"""
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Product, Category, Order, Favorite, Profile
from .serializers import (
    ProductSerializer, CategorySerializer, OrderSerializer,
    FavoriteSerializer, ProfileSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet pour les produits"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    def get_permissions(self):
        """Permissions différentes selon l'action"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [IsAuthenticatedOrReadOnly()]
    
    def perform_create(self, serializer):
        """Vérifier que l'utilisateur est artisan"""
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.role != 'artisan':
            raise serializers.ValidationError("Seuls les artisans peuvent créer des produits")
        serializer.save()
    
    def perform_update(self, serializer):
        """Vérifier que l'utilisateur est artisan"""
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.role != 'artisan':
            raise serializers.ValidationError("Seuls les artisans peuvent modifier des produits")
        serializer.save()
    
    def perform_destroy(self, instance):
        """Vérifier que l'utilisateur est artisan"""
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.role != 'artisan':
            raise serializers.ValidationError("Seuls les artisans peuvent supprimer des produits")
        instance.delete()
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def toggle_favorite(self, request, slug=None):
        """Ajouter/retirer un produit des favoris"""
        product = self.get_object()
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            product=product
        )
        
        if not created:
            favorite.delete()
            return Response({'status': 'removed', 'message': 'Produit retiré des favoris'})
        
        return Response({'status': 'added', 'message': 'Produit ajouté aux favoris'})


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet pour les catégories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    def get_permissions(self):
        """Permissions différentes selon l'action"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [IsAuthenticatedOrReadOnly()]
    
    def perform_create(self, serializer):
        """Vérifier que l'utilisateur est artisan"""
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.role != 'artisan':
            raise serializers.ValidationError("Seuls les artisans peuvent créer des catégories")
        serializer.save()
    
    def perform_update(self, serializer):
        """Vérifier que l'utilisateur est artisan"""
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.role != 'artisan':
            raise serializers.ValidationError("Seuls les artisans peuvent modifier des catégories")
        serializer.save()
    
    def perform_destroy(self, instance):
        """Vérifier que l'utilisateur est artisan"""
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.role != 'artisan':
            raise serializers.ValidationError("Seuls les artisans peuvent supprimer des catégories")
        instance.delete()


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet pour les commandes"""
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filtrer les commandes selon le rôle"""
        user = self.request.user
        if hasattr(user, 'profile') and user.profile.role == 'artisan':
            # Artisan voit toutes les commandes
            return Order.objects.all()
        # Client voit seulement ses commandes
        return Order.objects.filter(customer=user)
    
    def perform_create(self, serializer):
        """Créer une commande avec le client connecté"""
        serializer.save(customer=self.request.user)
    
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_status(self, request, pk=None):
        """Mettre à jour le statut d'une commande (artisan seulement)"""
        order = self.get_object()
        
        if not hasattr(request.user, 'profile') or request.user.profile.role != 'artisan':
            return Response(
                {'error': 'Seuls les artisans peuvent modifier le statut'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        new_status = request.data.get('status')
        if new_status not in dict(Order.STATUS_CHOICES):
            return Response(
                {'error': 'Statut invalide'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        order.status = new_status
        order.save()
        
        return Response({'status': 'updated', 'order_status': order.status})


class FavoriteViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet pour les favoris (lecture seule)"""
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Retourner les favoris de l'utilisateur connecté"""
        return Favorite.objects.filter(user=self.request.user)


class ProfileViewSet(viewsets.ModelViewSet):
    """ViewSet pour les profils"""
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Un utilisateur ne peut voir que son propre profil"""
        return Profile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Créer un profil pour l'utilisateur connecté"""
        serializer.save(user=self.request.user)
