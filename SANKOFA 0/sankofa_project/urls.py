"""
URL configuration for sankofa_project project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from galerie.views_auth import custom_allauth_login_redirect

# Configuration de l'admin
admin.site.site_header = "Galerie Sankofa - Administration"
admin.site.site_title = "Galerie Sankofa Admin"
admin.site.index_title = "Tableau de bord"

# Configuration Swagger/OpenAPI
schema_view = get_schema_view(
   openapi.Info(
      title="Galerie Sankofa API",
      default_version='v1',
      description="API REST pour la plateforme de vente d'artisanat traditionnel ivoirien",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@galeriesankofa.ci"),
      license=openapi.License(name="Proprietary License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rediriger /accounts/login/ vers notre page de connexion personnalisée
    path('accounts/login/', custom_allauth_login_redirect, name='account_login'),
    # Garder les autres URLs allauth pour Google OAuth
    path('accounts/', include('allauth.urls')),
    path('', include('galerie.urls')),
    
    # API REST
    path('api/', include('galerie.urls_api')),
    
    # Swagger/OpenAPI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
