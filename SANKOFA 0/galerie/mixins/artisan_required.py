from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied


class ArtisanRequiredMixin:
    """Mixin pour vérifier que l'utilisateur est artisan"""
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Vous devez être connecté en tant qu\'artisan.')
            return redirect('galerie:login?type=artisan')
        
        try:
            profile = request.user.profile
            if profile.role != 'artisan':
                messages.error(request, 'Accès réservé aux artisans.')
                return redirect('galerie:home')
        except:
            messages.error(request, 'Profil non trouvé.')
            return redirect('galerie:home')
        
        return super().dispatch(request, *args, **kwargs)

