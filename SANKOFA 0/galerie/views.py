from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Sum, Count
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Product, Category, Order, Profile, ContactMessage, Favorite
from .forms import OrderForm, ContactForm, ProductForm
import json


def home(request):
    """Page d'accueil"""
    categories = Category.objects.all()
    featured_products = Product.objects.filter(availability=True)[:6]
    
    # Récupérer la catégorie sélectionnée depuis la session ou GET
    selected_category = request.GET.get('category', 'Tous')
    if selected_category != 'Tous':
        try:
            category_obj = Category.objects.get(name=selected_category)
            featured_products = Product.objects.filter(
                category=category_obj, 
                availability=True
            )[:6]
        except Category.DoesNotExist:
            pass
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'galerie/home.html', context)


def gallery(request):
    """Page galerie avec filtres"""
    categories = Category.objects.all()
    selected_category = request.GET.get('category', 'Tous')
    view_mode = request.GET.get('view', 'grid')
    
    products = Product.objects.all()
    
    if selected_category != 'Tous':
        try:
            category_obj = Category.objects.get(name=selected_category)
            products = products.filter(category=category_obj)
        except Category.DoesNotExist:
            pass
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'view_mode': view_mode,
    }
    return render(request, 'galerie/gallery.html', context)


def product_detail(request, slug):
    """Page détails produit"""
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:3]
    
    # Vérifier si le produit est en favoris pour l'utilisateur connecté
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
    
    context = {
        'product': product,
        'related_products': related_products,
        'is_favorite': is_favorite,
    }
    return render(request, 'galerie/product_detail.html', context)


def about(request):
    """Page à propos"""
    return render(request, 'galerie/about.html')


def contact(request):
    """Page contact"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès !')
            return redirect('galerie:contact')
    else:
        form = ContactForm()
    
    return render(request, 'galerie/contact.html', {'form': form})


def order_create(request, product_id=None):
    """Créer une commande"""
    product = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)
    
    # Auto-remplir les informations si l'utilisateur est connecté
    initial_data = {}
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            initial_data = {
                'customer_name': request.user.get_full_name() or request.user.username,
                'customer_phone': profile.phone or '',
                'customer_address': profile.address or '',
            }
        except Profile.DoesNotExist:
            initial_data = {
                'customer_name': request.user.get_full_name() or request.user.username,
            }
    
    if request.method == 'POST':
        # Récupérer product_id depuis POST si présent
        product_id_from_post = request.POST.get('product_id')
        if product_id_from_post and not product:
            try:
                product = get_object_or_404(Product, id=int(product_id_from_post))
            except (ValueError, TypeError):
                pass
        
        form = OrderForm(request.POST)
        if form.is_valid():
            # Récupérer le produit
            product_id_from_form = form.cleaned_data.get('product_id')
            if product_id_from_form:
                product = get_object_or_404(Product, id=product_id_from_form)
            elif product:
                pass  # Utiliser le produit déjà récupéré
            else:
                messages.error(request, 'Veuillez sélectionner un produit.')
                context = {
                    'form': form,
                    'product': product,
                }
                return render(request, 'galerie/order.html', context)
            
            # Vérifier le stock
            quantity = form.cleaned_data.get('quantity', 1)
            if product.stock < quantity:
                messages.error(request, f'Stock insuffisant. Stock disponible : {product.stock} unité(s).')
                context = {
                    'form': form,
                    'product': product,
                }
                return render(request, 'galerie/order.html', context)
            
            if not product.availability:
                messages.error(request, 'Ce produit n\'est plus disponible.')
                context = {
                    'form': form,
                    'product': product,
                }
                return render(request, 'galerie/order.html', context)
            
            # Créer la commande
            order = form.save(commit=False)
            order.product = product
            order.total = product.price * quantity
            
            if request.user.is_authenticated:
                order.customer = request.user
                # Mettre à jour le profil en client si nécessaire
                profile, created = Profile.objects.get_or_create(user=request.user)
                if profile.role == 'visitor':
                    profile.role = 'client'
                    profile.save()
            
            order.save()
            
            # Mettre à jour le stock
            product.stock -= quantity
            if product.stock == 0:
                product.availability = False
            product.save()
            
            messages.success(request, f'Commande {order.order_number} créée avec succès ! Nous vous contacterons sous peu.')
            if request.user.is_authenticated:
                return redirect('galerie:order_tracking')
            else:
                return redirect('galerie:home')
        else:
            # Afficher les erreurs du formulaire
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
            # Re-rendre le formulaire avec les erreurs
            context = {
                'form': form,
                'product': product,
            }
            return render(request, 'galerie/order.html', context)
    else:
        # Fusionner les données initiales
        if product:
            initial_data['product_id'] = product.id
        form = OrderForm(initial=initial_data)
        # S'assurer que product_id est dans le formulaire
        if product:
            form.fields['product_id'].initial = product.id
    
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'galerie/order.html', context)


@login_required
def order_tracking(request):
    """Suivi des commandes"""
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'galerie/tracking.html', context)


@login_required
def profile(request):
    """Profil utilisateur"""
    profile_obj, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile_obj.phone = request.POST.get('phone', '')
        profile_obj.address = request.POST.get('address', '')
        profile_obj.whatsapp = request.POST.get('whatsapp', '')
        profile_obj.save()
        messages.success(request, 'Profil mis à jour avec succès !')
        return redirect('galerie:profile')
    
    # Compter les commandes livrées
    delivered_count = Order.objects.filter(customer=request.user, status='livrée').count()
    
    # Récupérer les favoris
    favorites = Favorite.objects.filter(user=request.user).select_related('product').order_by('-created_at')
    
    context = {
        'profile': profile_obj,
        'delivered_count': delivered_count,
        'favorites': favorites,
    }
    return render(request, 'galerie/profile.html', context)


def login_view(request):
    """Page de connexion"""
    user_type = request.GET.get('type', 'client')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('userType', user_type)
        
        # Authentification Django
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # Vérifier le rôle
            try:
                profile = user.profile
                if user_type == 'artisan' and profile.role != 'artisan':
                    messages.error(request, 'Vous n\'avez pas accès à l\'espace artisan.')
                    return redirect('galerie:login')
                elif user_type == 'client' and profile.role == 'artisan':
                    # Les artisans peuvent aussi accéder comme clients
                    pass
            except Profile.DoesNotExist:
                # Créer un profil par défaut
                Profile.objects.create(user=user, role=user_type)
            
            if user_type == 'artisan':
                return redirect('galerie:dashboard')
            else:
                return redirect('galerie:home')
        else:
            # Mode démo : accepter n'importe quel email/mot de passe
            # Créer un utilisateur temporaire pour la démo
            from django.contrib.auth.models import User
            user, created = User.objects.get_or_create(
                username=email,
                defaults={'email': email}
            )
            if created:
                user.set_password(password or 'demo123')
                user.save()
                Profile.objects.create(user=user, role=user_type)
            
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            if user_type == 'artisan':
                return redirect('galerie:dashboard')
            else:
                return redirect('galerie:home')
    
    return render(request, 'galerie/login.html', {'user_type': user_type})


def register(request):
    """Page d'inscription"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone', '')
        
        from django.contrib.auth.models import User
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
            Profile.objects.create(user=user, role='client', phone=phone)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Compte créé avec succès !')
            return redirect('galerie:home')
    
    return render(request, 'galerie/register.html')


def logout_view(request):
    """Déconnexion"""
    logout(request)
    messages.success(request, 'Vous avez été déconnecté.')
    return redirect('galerie:home')


@login_required
def dashboard(request):
    """Tableau de bord artisan"""
    # Vérifier que l'utilisateur est artisan
    try:
        profile = request.user.profile
        if profile.role != 'artisan':
            messages.error(request, 'Accès réservé aux artisans.')
            return redirect('galerie:home')
    except Profile.DoesNotExist:
        messages.error(request, 'Profil non trouvé.')
        return redirect('galerie:login?type=artisan')
    
    # Vérifier la vérification 2FA
    if not request.session.get('artisan_verified'):
        return redirect('galerie:artisan_verify')
    
    # Statistiques
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_sales = Order.objects.aggregate(
        total=Sum('total')
    )['total'] or 0
    pending_orders = Order.objects.filter(status='en attente').count()
    in_progress_orders = Order.objects.filter(status='en cours').count()
    delivered_orders = Order.objects.filter(status='livrée').count()
    in_stock_products = Product.objects.filter(availability=True, stock__gt=0).count()
    out_of_stock_products = Product.objects.filter(availability=False).count()
    total_stock = Product.objects.aggregate(total=Sum('stock'))['total'] or 0
    
    # Statistiques mensuelles (dernier mois)
    from django.utils import timezone
    from datetime import timedelta
    last_month = timezone.now() - timedelta(days=30)
    monthly_orders = Order.objects.filter(created_at__gte=last_month).count()
    monthly_sales = Order.objects.filter(created_at__gte=last_month).aggregate(
        total=Sum('total')
    )['total'] or 0
    
    # Projection mensuelle (basée sur les 30 derniers jours)
    from decimal import Decimal
    if monthly_orders > 0:
        avg_order_value = float(monthly_sales) / monthly_orders if monthly_sales else 0
        projected_monthly = float(monthly_sales) * 1.1 if monthly_sales else 0  # Projection avec 10% de croissance
    else:
        avg_order_value = 0
        projected_monthly = 0
    
    # Onglet actif
    tab = request.GET.get('tab', 'overview')
    
    # Données selon l'onglet
    products = Product.objects.all().order_by('-created_at')
    orders = Order.objects.all().order_by('-created_at')
    
    context = {
        'total_products': total_products,
        'total_orders': total_orders,
        'total_sales': total_sales,
        'pending_orders': pending_orders,
        'in_progress_orders': in_progress_orders,
        'delivered_orders': delivered_orders,
        'in_stock_products': in_stock_products,
        'out_of_stock_products': out_of_stock_products,
        'total_stock': total_stock,
        'monthly_sales': monthly_sales,
        'monthly_orders': monthly_orders,
        'projected_monthly': projected_monthly,
        'avg_order_value': avg_order_value,
        'tab': tab,
        'products': products,
        'orders': orders,
    }
    return render(request, 'galerie/dashboard.html', context)


@login_required
@require_http_methods(["POST"])
def dashboard_product_create(request):
    """Créer un produit depuis le dashboard"""
    try:
        profile = request.user.profile
        if profile.role != 'artisan':
            return JsonResponse({'error': 'Accès non autorisé'}, status=403)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profil non trouvé'}, status=403)
    
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save()
        return JsonResponse({
            'success': True,
            'product': {
                'id': product.id,
                'name': product.name,
                'price': float(product.price),
                'category': product.category.name,
            }
        })
    else:
        return JsonResponse({'error': 'Données invalides', 'errors': form.errors}, status=400)


@login_required
@require_http_methods(["POST"])
def dashboard_product_update(request, product_id):
    """Mettre à jour un produit"""
    try:
        profile = request.user.profile
        if profile.role != 'artisan':
            return JsonResponse({'error': 'Accès non autorisé'}, status=403)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profil non trouvé'}, status=403)
    
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST, request.FILES, instance=product)
    
    if form.is_valid():
        product = form.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Données invalides', 'errors': form.errors}, status=400)


@login_required
@require_http_methods(["POST"])
def dashboard_product_delete(request, product_id):
    """Supprimer un produit"""
    try:
        profile = request.user.profile
        if profile.role != 'artisan':
            return JsonResponse({'error': 'Accès non autorisé'}, status=403)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profil non trouvé'}, status=403)
    
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return JsonResponse({'success': True})


@login_required
@require_http_methods(["POST"])
def add_favorite(request, product_id):
    """Ajouter un produit aux favoris"""
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    
    if created:
        return JsonResponse({'success': True, 'message': 'Produit ajouté aux favoris'})
    else:
        return JsonResponse({'success': False, 'message': 'Produit déjà en favoris'})


@login_required
@require_http_methods(["POST"])
def remove_favorite(request, product_id):
    """Retirer un produit des favoris"""
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    return JsonResponse({'success': True, 'message': 'Produit retiré des favoris'})


@login_required
def favorites_list(request):
    """Liste des produits favoris"""
    favorites = Favorite.objects.filter(user=request.user).select_related('product').order_by('-created_at')
    
    context = {
        'favorites': favorites,
    }
    return render(request, 'galerie/favorites.html', context)


@login_required
@require_http_methods(["POST"])
def dashboard_order_update_status(request, order_id):
    """Mettre à jour le statut d'une commande"""
    try:
        profile = request.user.profile
        if profile.role != 'artisan':
            return JsonResponse({'error': 'Accès non autorisé'}, status=403)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profil non trouvé'}, status=403)
    
    order = get_object_or_404(Order, id=order_id)
    new_status = request.POST.get('status')
    
    if new_status in dict(Order.STATUS_CHOICES):
        order.status = new_status
        order.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Statut invalide'}, status=400)
