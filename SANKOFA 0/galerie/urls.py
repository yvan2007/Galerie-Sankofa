from django.urls import path
from . import views
from . import views_dashboard
from . import views_auth

app_name = 'galerie'

urlpatterns = [
    # Pages publiques
    path('', views.home, name='home'),
    path('galerie/', views.gallery, name='gallery'),
    path('produit/<slug:slug>/', views.product_detail, name='product_detail'),
    path('a-propos/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # Pages client
    path('commande/', views.order_create, name='order_create'),
    path('commande/<int:product_id>/', views.order_create, name='order_create_product'),
    path('suivi/', views.order_tracking, name='order_tracking'),
    path('profil/', views.profile, name='profile'),
    path('favoris/ajouter/<int:product_id>/', views.add_favorite, name='add_favorite'),
    path('favoris/retirer/<int:product_id>/', views.remove_favorite, name='remove_favorite'),
    path('favoris/', views.favorites_list, name='favorites_list'),
    
    # Authentification
    path('connexion/', views_auth.login_view, name='login'),
    path('inscription/', views_auth.register, name='register'),
    path('deconnexion/', views_auth.logout_view, name='logout'),
    path('mot-de-passe-oublie/', views_auth.password_reset_request, name='password_reset_request'),
    path('reinitialisation/<str:token>/', views_auth.password_reset_confirm, name='password_reset_confirm'),
    path('verification-artisan/', views_auth.artisan_verify, name='artisan_verify'),
    
    # Dashboard artisan
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # CRUD Produits
    path('dashboard/produit/creer/', views_dashboard.product_create, name='product_create'),
    path('dashboard/produit/<int:product_id>/modifier/', views_dashboard.product_update, name='product_update'),
    path('dashboard/produit/<int:product_id>/supprimer/', views_dashboard.product_delete, name='product_delete'),
    
    # CRUD Catégories
    path('dashboard/categorie/creer/', views_dashboard.category_create, name='category_create'),
    path('dashboard/categorie/<int:category_id>/modifier/', views_dashboard.category_update, name='category_update'),
    path('dashboard/categorie/<int:category_id>/supprimer/', views_dashboard.category_delete, name='category_delete'),
    
    # Gestion commandes
    path('dashboard/commande/<int:order_id>/statut/', views_dashboard.order_update_status, name='order_update_status'),
]
