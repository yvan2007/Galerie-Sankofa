"""Vues pour le dashboard artisan - CRUD complet"""
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from .models import Product, Category, Order, Profile
from .forms import ProductForm, CategoryForm
from .mixins.artisan_required import ArtisanRequiredMixin


def check_artisan(request):
    """Vérifie que l'utilisateur est artisan"""
    if not request.user.is_authenticated:
        return False, redirect('galerie:login')
    try:
        profile = request.user.profile
        if profile.role != 'artisan':
            return False, redirect('galerie:home')
    except:
        return False, redirect('galerie:home')
    return True, None


# ==================== PRODUITS ====================

@login_required
@require_http_methods(["GET", "POST"])
def product_create(request):
    """Créer un produit"""
    is_artisan, redirect_response = check_artisan(request)
    if not is_artisan:
        return redirect_response
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': f'Produit "{product.name}" créé avec succès !',
                    'product': {
                        'id': product.id,
                        'name': product.name,
                        'price': float(product.price),
                        'category': product.category.name,
                        'image': product.get_image(),
                    }
                })
            messages.success(request, f'Produit "{product.name}" créé avec succès !')
            return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=products')
    else:
        form = ProductForm()
    
    categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories,
        'action': 'create',
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.template.loader import render_to_string
        html = render_to_string('galerie/partials/product_form_modal.html', context, request=request)
        return JsonResponse({'html': html})
    
    return render(request, 'galerie/product_form.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def product_update(request, product_id):
    """Modifier un produit"""
    is_artisan, redirect_response = check_artisan(request)
    if not is_artisan:
        return redirect_response
    
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': f'Produit "{product.name}" modifié avec succès !',
                    'product': {
                        'id': product.id,
                        'name': product.name,
                        'price': float(product.price),
                        'category': product.category.name,
                        'image': product.get_image(),
                    }
                })
            messages.success(request, f'Produit "{product.name}" modifié avec succès !')
            return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=products')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                from django.template.loader import render_to_string
                context = {'form': form, 'product': product, 'categories': Category.objects.all(), 'action': 'update'}
                html = render_to_string('galerie/partials/product_form_modal.html', context, request=request)
                return JsonResponse({'html': html, 'success': False, 'errors': form.errors})
    else:
        form = ProductForm(instance=product)
    
    categories = Category.objects.all()
    context = {
        'form': form,
        'product': product,
        'categories': categories,
        'action': 'update',
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.template.loader import render_to_string
        html = render_to_string('galerie/partials/product_form_modal.html', context, request=request)
        return JsonResponse({'html': html})
    
    return render(request, 'galerie/product_form.html', context)


@login_required
@require_http_methods(["POST"])
def product_delete(request, product_id):
    """Supprimer un produit"""
    is_artisan, redirect_response = check_artisan(request)
    if not is_artisan:
        return redirect_response
    
    product = get_object_or_404(Product, id=product_id)
    product_name = product.name
    product.delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': f'Produit "{product_name}" supprimé avec succès !'
        })
    
    messages.success(request, f'Produit "{product_name}" supprimé avec succès !')
    return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=products')


# ==================== CATÉGORIES ====================

@login_required
@require_http_methods(["GET", "POST"])
def category_create(request):
    """Créer une catégorie"""
    is_artisan, redirect_response = check_artisan(request)
    if not is_artisan:
        return redirect_response
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': f'Catégorie "{category.name}" créée avec succès !',
                    'category': {
                        'id': category.id,
                        'name': category.name,
                    }
                })
            messages.success(request, f'Catégorie "{category.name}" créée avec succès !')
            return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=products')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'action': 'create',
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.template.loader import render_to_string
        html = render_to_string('galerie/partials/category_form_modal.html', context, request=request)
        return JsonResponse({'html': html})
    
    return render(request, 'galerie/category_form.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def category_update(request, category_id):
    """Modifier une catégorie"""
    is_artisan, redirect_response = check_artisan(request)
    if not is_artisan:
        return redirect_response
    
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': f'Catégorie "{category.name}" modifiée avec succès !',
                    'category': {
                        'id': category.id,
                        'name': category.name,
                    }
                })
            messages.success(request, f'Catégorie "{category.name}" modifiée avec succès !')
            return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=products')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'category': category,
        'action': 'update',
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.template.loader import render_to_string
        html = render_to_string('galerie/partials/category_form_modal.html', context, request=request)
        return JsonResponse({'html': html})
    
    return render(request, 'galerie/category_form.html', context)


@login_required
@require_http_methods(["POST"])
def category_delete(request, category_id):
    """Supprimer une catégorie"""
    is_artisan, redirect_response = check_artisan(request)
    if not is_artisan:
        return redirect_response
    
    category = get_object_or_404(Category, id=category_id)
    category_name = category.name
    
    # Vérifier si des produits utilisent cette catégorie
    products_count = Product.objects.filter(category=category).count()
    if products_count > 0:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': f'Impossible de supprimer cette catégorie : {products_count} produit(s) l\'utilise(nt).'
            }, status=400)
        messages.error(request, f'Impossible de supprimer : {products_count} produit(s) utilisent cette catégorie.')
        return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=products')
    
    category.delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': f'Catégorie "{category_name}" supprimée avec succès !'
        })
    
    messages.success(request, f'Catégorie "{category_name}" supprimée avec succès !')
    return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=products')


# ==================== COMMANDES ====================

@login_required
@require_http_methods(["POST"])
def order_update_status(request, order_id):
    """Mettre à jour le statut d'une commande"""
    is_artisan, redirect_response = check_artisan(request)
    if not is_artisan:
        return redirect_response
    
    order = get_object_or_404(Order, id=order_id)
    new_status = request.POST.get('status')
    
    if new_status not in dict(Order.STATUS_CHOICES):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Statut invalide'
            }, status=400)
        messages.error(request, 'Statut invalide')
        return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=orders')
    
    order.status = new_status
    order.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': f'Statut de la commande {order.order_number} mis à jour !',
            'status': new_status
        })
    
    messages.success(request, f'Statut de la commande {order.order_number} mis à jour !')
    return HttpResponseRedirect(reverse('galerie:dashboard') + '?tab=orders')

