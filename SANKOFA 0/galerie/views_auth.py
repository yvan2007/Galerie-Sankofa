"""Vues d'authentification améliorées"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Profile, ArtisanVerification
from .utils.email_service import send_welcome_email, send_password_reset_email, send_artisan_verification_code
import secrets
import string


def check_artisan_exists():
    """Vérifie si un compte artisan existe déjà"""
    return Profile.objects.filter(role='artisan').exists()


def login_view(request):
    """Page de connexion améliorée"""
    user_type = request.GET.get('type', 'client')
    next_url = request.GET.get('next', '')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('userType', user_type)
        
        # Authentification Django
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Connecter l'utilisateur en session Django d'abord
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            # Vérifier le rôle
            try:
                profile = user.profile
            except Profile.DoesNotExist:
                # Créer un profil par défaut
                profile = Profile.objects.create(user=user, role=user_type)
            
            # Gestion selon le type de connexion demandé
            if user_type == 'artisan':
                # Vérifier que l'utilisateur est bien artisan
                if profile.role != 'artisan':
                    logout(request)  # Déconnecter si pas artisan
                    messages.error(request, 'Vous n\'avez pas accès à l\'espace artisan.')
                    return redirect('galerie:login?type=artisan')
                
                # Pour artisan : nécessite code de vérification
                # Sauvegarder next_url si fourni
                if next_url:
                    request.session['artisan_next_url'] = next_url
                return redirect('galerie:artisan_verify')
            
            else:
                # Connexion client (ou artisan se connectant comme client)
                if next_url:
                    return redirect(next_url)
                return redirect('galerie:home')
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')
    
    return render(request, 'galerie/login.html', {'user_type': user_type})


def register(request):
    """Page d'inscription améliorée"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone', '')
        user_type = request.POST.get('userType', 'client')
        
        # Vérifier si artisan existe déjà
        if user_type == 'artisan' and check_artisan_exists():
            messages.error(request, 'Un compte artisan existe déjà. Vous ne pouvez pas en créer un nouveau.')
            return redirect('galerie:register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur existe déjà.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            Profile.objects.create(user=user, role=user_type, phone=phone)
            
            # Envoyer email de bienvenue (sans mot de passe pour la sécurité)
            try:
                send_welcome_email(user)
            except Exception as e:
                print(f"Erreur envoi email: {e}")
            
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Compte créé avec succès ! Un email de bienvenue vous a été envoyé.')
            
            if user_type == 'artisan':
                return redirect('galerie:artisan_verify')
            else:
                return redirect('galerie:home')
    
    return render(request, 'galerie/register.html')


def password_reset_request(request):
    """Demande de réinitialisation de mot de passe"""
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Générer un token
            token = secrets.token_urlsafe(32)
            # Stocker le token (dans la session ou un modèle dédié)
            request.session['password_reset_token'] = token
            request.session['password_reset_user_id'] = user.id
            request.session['password_reset_expires'] = (timezone.now() + timedelta(hours=24)).isoformat()
            
            # Envoyer email
            try:
                send_password_reset_email(user, token)
                messages.success(request, 'Un email de réinitialisation vous a été envoyé.')
            except Exception as e:
                messages.error(request, f'Erreur lors de l\'envoi de l\'email: {e}')
            
            return redirect('galerie:login')
        except User.DoesNotExist:
            messages.error(request, 'Aucun compte trouvé avec cet email.')
    
    return render(request, 'galerie/password_reset_request.html')


def password_reset_confirm(request, token):
    """Confirmation de réinitialisation de mot de passe"""
    user_id = request.session.get('password_reset_user_id')
    stored_token = request.session.get('password_reset_token')
    expires = request.session.get('password_reset_expires')
    
    if not user_id or not stored_token or stored_token != token:
        messages.error(request, 'Lien invalide ou expiré.')
        return redirect('galerie:password_reset_request')
    
    if expires:
        expires_dt = timezone.datetime.fromisoformat(expires)
        if timezone.now() > expires_dt:
            messages.error(request, 'Ce lien a expiré. Veuillez faire une nouvelle demande.')
            return redirect('galerie:password_reset_request')
    
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
        elif len(password) < 8:
            messages.error(request, 'Le mot de passe doit contenir au moins 8 caractères.')
        else:
            user.set_password(password)
            user.save()
            # Nettoyer la session
            del request.session['password_reset_token']
            del request.session['password_reset_user_id']
            del request.session['password_reset_expires']
            messages.success(request, 'Votre mot de passe a été réinitialisé avec succès.')
            return redirect('galerie:login')
    
    return render(request, 'galerie/password_reset_confirm.html', {'token': token})


@login_required
def artisan_verify(request):
    """Vérification 2FA pour accès dashboard artisan"""
    try:
        profile = request.user.profile
        if profile.role != 'artisan':
            messages.error(request, 'Accès réservé aux artisans.')
            return redirect('galerie:login?type=artisan')
    except Profile.DoesNotExist:
        messages.error(request, 'Profil non trouvé.')
        return redirect('galerie:login?type=artisan')
    
    # Vérifier si déjà vérifié dans cette session
    if request.session.get('artisan_verified'):
        return redirect('galerie:dashboard')
    
    if request.method == 'POST':
        code = request.POST.get('code')
        
        # Vérifier le code
        verification = ArtisanVerification.objects.filter(
            user=request.user,
            code=code,
            used=False,
            expires_at__gt=timezone.now()
        ).first()
        
        if verification:
            verification.used = True
            verification.save()
            request.session['artisan_verified'] = True
            messages.success(request, 'Code vérifié avec succès !')
            # Rediriger vers next_url si fourni, sinon vers dashboard
            next_url = request.session.get('artisan_next_url', '')
            if next_url:
                del request.session['artisan_next_url']
                return redirect(next_url)
            return redirect('galerie:dashboard')
        else:
            messages.error(request, 'Code invalide ou expiré.')
    
    # Vérifier si l'utilisateur demande un nouveau code
    resend_code = request.GET.get('resend', 'false') == 'true'
    
    # Générer et envoyer un nouveau code si pas déjà fait ou si renvoi demandé
    if resend_code or not request.session.get('verification_code_sent'):
        # Invalider les anciens codes non utilisés
        ArtisanVerification.objects.filter(
            user=request.user,
            used=False,
            expires_at__gt=timezone.now()
        ).update(used=True)
        
        code = ArtisanVerification.generate_code()
        verification = ArtisanVerification.objects.create(
            user=request.user,
            code=code,
            expires_at=timezone.now() + timedelta(minutes=10)
        )
        
        try:
            send_artisan_verification_code(request.user, code)
            request.session['verification_code_sent'] = True
            if resend_code:
                messages.success(request, f'Un nouveau code de vérification a été envoyé à {request.user.email}.')
            else:
                messages.info(request, f'Un code de vérification a été envoyé à {request.user.email}.')
            
            # En mode DEBUG, afficher le code dans la console (pour test)
            if settings.DEBUG:
                import logging
                logger = logging.getLogger(__name__)
                logger.info(f'[DEBUG] Code de vérification artisan pour {request.user.email}: {code}')
                messages.warning(request, f'[MODE DEBUG] Code: {code} (visible uniquement en développement)')
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f'Erreur envoi email artisan: {e}')
            messages.error(request, f'Erreur lors de l\'envoi du code: {str(e)}. Veuillez vérifier votre configuration email.')
            # En mode DEBUG, afficher quand même le code
            if settings.DEBUG:
                messages.warning(request, f'[MODE DEBUG] Code généré: {code} (email non envoyé)')
    
    context = {
        'user_email': request.user.email,
    }
    return render(request, 'galerie/artisan_verify.html', context)


def logout_view(request):
    """Déconnexion"""
    # Nettoyer la session artisan
    if 'artisan_verified' in request.session:
        del request.session['artisan_verified']
    if 'verification_code_sent' in request.session:
        del request.session['verification_code_sent']
    
    logout(request)
    messages.success(request, 'Vous avez été déconnecté.')
    return redirect('galerie:home')


def custom_allauth_login_redirect(request):
    """Rediriger les tentatives de connexion allauth vers notre page personnalisée"""
    # Vérifier si c'est une redirection pour artisan (depuis le dashboard ou vérification)
    next_url = request.GET.get('next', '')
    
    # Si la redirection est vers le dashboard ou la vérification artisan, utiliser type=artisan
    if 'dashboard' in next_url or 'verification-artisan' in next_url or 'verification' in next_url:
        return redirect(f'galerie:login?type=artisan&next={next_url}')
    
    # Si c'est une tentative de connexion Google (via allauth), laisser allauth gérer
    if request.GET.get('process') == 'login' or 'socialaccount' in request.path:
        # Importer et utiliser la vue allauth originale
        from allauth.account.views import login as allauth_login
        return allauth_login(request)
    
    # Sinon, rediriger vers la page de connexion client normale
    return redirect(f'galerie:login?next={next_url}' if next_url else 'galerie:login')


