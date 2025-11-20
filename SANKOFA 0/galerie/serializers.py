"""Serializers pour l'API REST"""
from rest_framework import serializers
from .models import Product, Category, Order, Favorite, Profile


class CategorySerializer(serializers.ModelSerializer):
    """Serializer pour les catégories"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']


class ProductSerializer(serializers.ModelSerializer):
    """Serializer pour les produits"""
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'details', 
            'price', 'category', 'category_id', 'image', 
            'image_url', 'availability', 'stock', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class OrderSerializer(serializers.ModelSerializer):
    """Serializer pour les commandes"""
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'customer', 'product', 'product_id',
            'quantity', 'total', 'status', 'customer_name', 
            'customer_phone', 'customer_address', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['order_number', 'created_at', 'updated_at']


class FavoriteSerializer(serializers.ModelSerializer):
    """Serializer pour les favoris"""
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = Favorite
        fields = ['id', 'product', 'created_at']
        read_only_fields = ['created_at']


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer pour les profils"""
    class Meta:
        model = Profile
        fields = ['id', 'user', 'role', 'phone', 'address', 'whatsapp']

