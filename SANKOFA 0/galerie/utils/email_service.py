"""Service d'envoi d'emails"""
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags


def send_welcome_email(user):
    """Envoyer un email de bienvenue (sans mot de passe pour la sécurité)"""
    subject = 'Bienvenue sur Galerie Sankofa !'
    html_message = render_to_string('galerie/emails/welcome.html', {
        'user': user,
        'site_url': settings.SITE_URL if hasattr(settings, 'SITE_URL') else 'http://127.0.0.1:8000'
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )


def send_password_reset_email(user, reset_token):
    """Envoyer un email de réinitialisation de mot de passe"""
    subject = 'Réinitialisation de votre mot de passe - Galerie Sankofa'
    reset_url = f"{settings.SITE_URL if hasattr(settings, 'SITE_URL') else 'http://127.0.0.1:8000'}/reinitialisation/{reset_token}/"
    
    html_message = render_to_string('galerie/emails/password_reset.html', {
        'user': user,
        'reset_url': reset_url,
        'site_url': settings.SITE_URL if hasattr(settings, 'SITE_URL') else 'http://127.0.0.1:8000'
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )


def send_artisan_verification_code(user, code):
    """Envoyer le code de vérification pour l'accès au dashboard artisan"""
    subject = 'Code de vérification - Dashboard Artisan Galerie Sankofa'
    
    html_message = render_to_string('galerie/emails/artisan_verification.html', {
        'user': user,
        'code': code,
        'site_url': settings.SITE_URL if hasattr(settings, 'SITE_URL') else 'http://127.0.0.1:8000'
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )


