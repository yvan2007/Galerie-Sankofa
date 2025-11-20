"""Adaptateurs personnalisés pour django-allauth"""
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """Adaptateur personnalisé pour les comptes sociaux"""
    
    def pre_social_login(self, request, sociallogin):
        """Appelé avant la connexion sociale"""
        # Si l'utilisateur existe déjà avec cet email, connecter directement
        if sociallogin.is_existing:
            return
        
        # Vérifier si un utilisateur existe avec cet email
        email = sociallogin.account.extra_data.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                # Connecter l'utilisateur existant
                sociallogin.connect(request, user)
            except User.DoesNotExist:
                pass
    
    def populate_user(self, request, sociallogin, data):
        """Remplir les données utilisateur depuis le compte social"""
        user = super().populate_user(request, sociallogin, data)
        
        # Extraire le nom depuis les données Google
        if 'name' in data:
            name_parts = data['name'].split(' ', 1)
            if len(name_parts) > 1:
                user.first_name = name_parts[0]
                user.last_name = name_parts[1]
            else:
                user.first_name = name_parts[0]
        
        # Si pas de prénom/nom, utiliser l'email
        if not user.first_name and not user.last_name:
            user.first_name = user.email.split('@')[0]
        
        return user
    
    def save_user(self, request, sociallogin, form=None):
        """Sauvegarder l'utilisateur et créer son profil"""
        user = super().save_user(request, sociallogin, form)
        
        # Créer le profil client pour les nouveaux utilisateurs
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'role': 'client',
            }
        )
        
        return user


class CustomAccountAdapter(DefaultAccountAdapter):
    """Adaptateur personnalisé pour les comptes normaux"""
    
    def save_user(self, request, user, form, commit=True):
        """Sauvegarder l'utilisateur et créer son profil"""
        user = super().save_user(request, user, form, commit)
        
        if commit:
            # Créer le profil client pour les nouveaux utilisateurs
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'role': 'client',
                }
            )
        
        return user

