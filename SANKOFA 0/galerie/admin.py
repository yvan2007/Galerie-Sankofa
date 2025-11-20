from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.shortcuts import redirect
from .models import Category, Product, Profile, Order, ContactMessage, ArtisanVerification, Favorite


# Personnalisation de l'interface admin
admin.site.site_header = "Galerie Sankofa - Administration"
admin.site.site_title = "Galerie Sankofa Admin"
admin.site.index_title = "Tableau de bord"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Administration des catégories"""
    list_display = ['name', 'product_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def product_count(self, obj):
        """Affiche le nombre de produits dans cette catégorie"""
        count = obj.products.count()
        if count > 0:
            url = reverse('admin:galerie_product_changelist') + f'?category__id__exact={obj.id}'
            return format_html('<a href="{}">{} produit(s)</a>', url, count)
        return '0 produit'
    product_count.short_description = 'Produits'
    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Administration des produits"""
    list_display = ['image_thumbnail', 'name', 'category', 'price_display', 'stock', 'availability_badge', 'created_at']
    list_filter = ['category', 'availability', 'created_at', 'stock']
    search_fields = ['name', 'description', 'details']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at', 'image_preview']
    list_per_page = 25
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('name', 'slug', 'category', 'description', 'details')
        }),
        ('Prix et disponibilité', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Images', {
            'fields': ('image', 'image_preview', 'image_url')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_thumbnail(self, obj):
        """Affiche une miniature de l'image"""
        if obj.get_image():
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.get_image()
            )
        return format_html('<span style="color: #999;">Pas d\'image</span>')
    image_thumbnail.short_description = 'Image'
    
    def image_preview(self, obj):
        """Aperçu de l'image en grand"""
        if obj.get_image():
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />',
                obj.get_image()
            )
        return 'Aucune image'
    image_preview.short_description = 'Aperçu'
    
    def price_display(self, obj):
        """Affiche le prix formaté"""
        return format_html('<strong style="color: #CBA135;">{} XOF</strong>', int(obj.price))
    price_display.short_description = 'Prix'
    
    def availability_badge(self, obj):
        """Badge de disponibilité"""
        if obj.availability and obj.stock > 0:
            return format_html(
                '<span style="background-color: #10b981; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">✓ En stock</span>'
            )
        elif obj.availability:
            return format_html(
                '<span style="background-color: #f59e0b; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">⚠ Disponible</span>'
            )
        else:
            return format_html(
                '<span style="background-color: #ef4444; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">✗ Épuisé</span>'
            )
    availability_badge.short_description = 'Statut'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Administration des profils utilisateurs"""
    list_display = ['user', 'role_badge', 'phone', 'artisan_info', 'created_at']
    list_filter = ['role', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone', 'address']
    readonly_fields = ['created_at', 'artisan_status']
    actions = ['make_artisan', 'remove_artisan']
    
    fieldsets = (
        ('Utilisateur', {
            'fields': ('user', 'role')
        }),
        ('Coordonnées', {
            'fields': ('phone', 'whatsapp', 'address')
        }),
        ('Statut Artisan', {
            'fields': ('artisan_status',),
            'classes': ('collapse',),
            'description': 'Informations sur le statut artisan de cet utilisateur'
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def role_badge(self, obj):
        """Badge de rôle"""
        colors = {
            'visitor': '#6b7280',
            'client': '#3b82f6',
            'artisan': '#CBA135'
        }
        color = colors.get(obj.role, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">{}</span>',
            color, obj.get_role_display()
        )
    role_badge.short_description = 'Rôle'
    
    def artisan_info(self, obj):
        """Affiche des informations sur le statut artisan"""
        if obj.role == 'artisan':
            existing_artisan = Profile.objects.filter(role='artisan').exclude(id=obj.id).exists()
            if existing_artisan:
                return format_html(
                    '<span style="color: #ef4444; font-size: 11px;">⚠ Autre artisan existe</span>'
                )
            return format_html(
                '<span style="color: #10b981; font-size: 11px;">✓ Artisan unique</span>'
            )
        return '-'
    artisan_info.short_description = 'Info Artisan'
    
    def artisan_status(self, obj):
        """Affiche le statut artisan détaillé"""
        if obj.role == 'artisan':
            existing_artisan = Profile.objects.filter(role='artisan').exclude(id=obj.id).exists()
            if existing_artisan:
                other_artisan = Profile.objects.filter(role='artisan').exclude(id=obj.id).first()
                return format_html(
                    '<div style="padding: 1rem; background-color: #fef3c7; border-left: 4px solid #f59e0b; border-radius: 4px;">'
                    '<strong style="color: #92400e;">⚠ Attention :</strong><br>'
                    'Un autre compte artisan existe déjà ({})<br>'
                    'Seul un compte artisan peut exister dans le système.',
                    other_artisan.user.username if other_artisan else 'Inconnu'
                )
            return format_html(
                '<div style="padding: 1rem; background-color: #d1fae5; border-left: 4px solid #10b981; border-radius: 4px;">'
                '<strong style="color: #065f46;">✓ Statut Artisan Actif</strong><br>'
                'Cet utilisateur est le compte artisan unique du système.'
            )
        return format_html(
            '<div style="padding: 1rem; background-color: #f3f4f6; border-left: 4px solid #6b7280; border-radius: 4px;">'
            'Cet utilisateur n\'est pas artisan. Utilisez l\'action "Définir comme artisan" pour le transformer.'
        )
    artisan_status.short_description = 'Statut Artisan'
    
    def make_artisan(self, request, queryset):
        """Action pour transformer des utilisateurs en artisan"""
        # Vérifier si un artisan existe déjà
        existing_artisan = Profile.objects.filter(role='artisan').exclude(id__in=queryset.values_list('id', flat=True)).first()
        
        if existing_artisan:
            self.message_user(
                request,
                f'Un compte artisan existe déjà ({existing_artisan.user.username}). '
                'Seul un compte artisan peut exister. Supprimez d\'abord l\'artisan existant.',
                level=messages.ERROR
            )
            return
        
        count = 0
        for profile in queryset:
            if profile.role != 'artisan':
                profile.role = 'artisan'
                profile.save()
                count += 1
        
        if count > 0:
            self.message_user(
                request,
                f'{count} utilisateur(s) transformé(s) en artisan avec succès.',
                level=messages.SUCCESS
            )
        else:
            self.message_user(
                request,
                'Aucun utilisateur n\'a été modifié.',
                level=messages.WARNING
            )
    make_artisan.short_description = 'Définir comme artisan'
    
    def remove_artisan(self, request, queryset):
        """Action pour retirer le statut artisan"""
        count = 0
        for profile in queryset:
            if profile.role == 'artisan':
                profile.role = 'client'
                profile.save()
                count += 1
        
        if count > 0:
            self.message_user(
                request,
                f'{count} utilisateur(s) n\'est/sont plus artisan(s).',
                level=messages.SUCCESS
            )
        else:
            self.message_user(
                request,
                'Aucun utilisateur n\'a été modifié.',
                level=messages.WARNING
            )
    remove_artisan.short_description = 'Retirer le statut artisan'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Administration des commandes"""
    list_display = ['order_number', 'customer_link', 'product_link', 'quantity', 'total_display', 'status_badge', 'created_at']
    list_filter = ['status', 'created_at', 'product__category']
    search_fields = ['order_number', 'customer_name', 'customer_phone', 'customer_email', 'product__name']
    readonly_fields = ['order_number', 'created_at', 'updated_at']
    list_per_page = 25
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Informations de commande', {
            'fields': ('order_number', 'product', 'quantity', 'total', 'status')
        }),
        ('Informations client', {
            'fields': ('customer', 'customer_name', 'customer_phone', 'customer_address')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def customer_link(self, obj):
        """Lien vers le client"""
        if obj.customer:
            url = reverse('admin:auth_user_change', args=[obj.customer.id])
            return format_html('<a href="{}">{}</a>', url, obj.customer_name)
        return obj.customer_name
    customer_link.short_description = 'Client'
    
    def product_link(self, obj):
        """Lien vers le produit"""
        if obj.product:
            url = reverse('admin:galerie_product_change', args=[obj.product.id])
            return format_html('<a href="{}">{}</a>', url, obj.product.name)
        return '-'
    product_link.short_description = 'Produit'
    
    def total_display(self, obj):
        """Affiche le total formaté"""
        return format_html('<strong style="color: #CBA135;">{} XOF</strong>', int(obj.total))
    total_display.short_description = 'Total'
    
    def status_badge(self, obj):
        """Badge de statut"""
        colors = {
            'en attente': '#f59e0b',
            'en cours': '#3b82f6',
            'livrée': '#10b981',
            'annulée': '#ef4444'
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Statut'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Administration des messages de contact"""
    list_display = ['name', 'email', 'subject', 'read_badge', 'created_at']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    list_per_page = 25
    
    fieldsets = (
        ('Informations expéditeur', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message', 'read')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def read_badge(self, obj):
        """Badge lu/non lu"""
        if obj.read:
            return format_html(
                '<span style="background-color: #10b981; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">✓ Lu</span>'
            )
        return format_html(
            '<span style="background-color: #ef4444; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">✗ Non lu</span>'
        )
    read_badge.short_description = 'Statut'


@admin.register(ArtisanVerification)
class ArtisanVerificationAdmin(admin.ModelAdmin):
    """Administration des codes de vérification artisan"""
    list_display = ['user', 'code', 'used_badge', 'expires_at', 'created_at']
    list_filter = ['used', 'created_at', 'expires_at']
    search_fields = ['user__username', 'user__email', 'code']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Informations', {
            'fields': ('user', 'code', 'used', 'expires_at')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def used_badge(self, obj):
        """Badge utilisé/non utilisé"""
        if obj.used:
            return format_html(
                '<span style="background-color: #10b981; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">✓ Utilisé</span>'
            )
        return format_html(
            '<span style="background-color: #f59e0b; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">⏳ En attente</span>'
        )
    used_badge.short_description = 'Statut'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Administration des favoris"""
    list_display = ['user', 'product', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'user__email', 'product__name']
    readonly_fields = ['created_at']
    list_per_page = 25
    
    fieldsets = (
        ('Informations', {
            'fields': ('user', 'product')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


# Personnalisation de l'admin User pour faciliter la création d'artisan
class ProfileInline(admin.StackedInline):
    """Inline pour le profil dans l'admin User"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profil'
    fields = ('role', 'phone', 'whatsapp', 'address')
    fk_name = 'user'


class CustomUserAdmin(BaseUserAdmin):
    """Admin User personnalisé avec actions artisan"""
    inlines = (ProfileInline,)
    actions = ['make_artisan', 'remove_artisan']
    
    def make_artisan(self, request, queryset):
        """Action pour transformer des utilisateurs en artisan"""
        # Vérifier si un artisan existe déjà
        existing_artisan = Profile.objects.filter(role='artisan').exclude(user__in=queryset).first()
        
        if existing_artisan:
            self.message_user(
                request,
                f'Un compte artisan existe déjà ({existing_artisan.user.username}). '
                'Seul un compte artisan peut exister. Supprimez d\'abord l\'artisan existant.',
                level=messages.ERROR
            )
            return
        
        count = 0
        for user in queryset:
            profile, created = Profile.objects.get_or_create(user=user)
            if profile.role != 'artisan':
                profile.role = 'artisan'
                profile.save()
                count += 1
        
        if count > 0:
            self.message_user(
                request,
                f'{count} utilisateur(s) transformé(s) en artisan avec succès.',
                level=messages.SUCCESS
            )
        else:
            self.message_user(
                request,
                'Aucun utilisateur n\'a été modifié.',
                level=messages.WARNING
            )
    make_artisan.short_description = 'Définir comme artisan'
    
    def remove_artisan(self, request, queryset):
        """Action pour retirer le statut artisan"""
        count = 0
        for user in queryset:
            try:
                profile = user.profile
                if profile.role == 'artisan':
                    profile.role = 'client'
                    profile.save()
                    count += 1
            except Profile.DoesNotExist:
                pass
        
        if count > 0:
            self.message_user(
                request,
                f'{count} utilisateur(s) n\'est/sont plus artisan(s).',
                level=messages.SUCCESS
            )
        else:
            self.message_user(
                request,
                'Aucun utilisateur n\'a été modifié.',
                level=messages.WARNING
            )
    remove_artisan.short_description = 'Retirer le statut artisan'


# Désenregistrer l'admin User par défaut et enregistrer le nôtre
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
