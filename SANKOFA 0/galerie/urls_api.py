"""URLs pour l'API REST"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import (
    ProductViewSet, CategoryViewSet, OrderViewSet,
    FavoriteViewSet, ProfileViewSet
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]

