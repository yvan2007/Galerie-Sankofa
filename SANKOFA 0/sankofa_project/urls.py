"""
URL configuration for sankofa_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from galerie.views_auth import custom_allauth_login_redirect

# Configuration de l'admin
admin.site.site_header = "Galerie Sankofa - Administration"
admin.site.site_title = "Galerie Sankofa Admin"
admin.site.index_title = "Tableau de bord"

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rediriger /accounts/login/ vers notre page de connexion personnalisée
    path('accounts/login/', custom_allauth_login_redirect, name='account_login'),
    # Garder les autres URLs allauth pour Google OAuth
    path('accounts/', include('allauth.urls')),
    path('', include('galerie.urls')),
]

# Servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
