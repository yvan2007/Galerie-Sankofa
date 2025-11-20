from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from decimal import Decimal
import secrets
import string


class Category(models.Model):
    """Catégorie de produits"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """Produit artisanal"""
    name = models.CharField(max_length=200, verbose_name="Nom")
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(verbose_name="Description courte")
    details = models.TextField(verbose_name="Détails complets")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=0, 
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Prix (XOF)"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products',
        verbose_name="Catégorie"
    )
    image = models.ImageField(
        upload_to='products/', 
        blank=True, 
        null=True,
        verbose_name="Image"
    )
    image_url = models.URLField(
        blank=True, 
        null=True,
        verbose_name="URL Image (si pas d'upload)"
    )
    availability = models.BooleanField(default=True, verbose_name="Disponible")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        # Mettre à jour availability selon le stock
        if self.stock == 0:
            self.availability = False
        super().save(*args, **kwargs)

    def get_image(self):
        """Retourne l'image uploadée ou l'URL"""
        if self.image:
            return self.image.url
        return self.image_url or 'https://via.placeholder.com/400'


class Profile(models.Model):
    """Profil utilisateur étendu"""
    ROLE_CHOICES = [
        ('visitor', 'Visiteur'),
        ('client', 'Client'),
        ('artisan', 'Artisan'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='visitor', verbose_name="Rôle")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    address = models.TextField(blank=True, verbose_name="Adresse")
    whatsapp = models.CharField(max_length=20, blank=True, verbose_name="WhatsApp")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"


class Order(models.Model):
    """Commande"""
    STATUS_CHOICES = [
        ('en attente', 'En attente'),
        ('en cours', 'En cours'),
        ('livrée', 'Livrée'),
        ('annulée', 'Annulée'),
    ]

    order_number = models.CharField(max_length=20, unique=True, verbose_name="Numéro de commande")
    customer = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders',
        verbose_name="Client"
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='orders',
        verbose_name="Produit"
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Quantité"
    )
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=0,
        verbose_name="Total (XOF)"
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='en attente',
        verbose_name="Statut"
    )
    customer_name = models.CharField(max_length=200, verbose_name="Nom du client")
    customer_phone = models.CharField(max_length=30, verbose_name="Téléphone")
    customer_address = models.TextField(verbose_name="Adresse")
    notes = models.TextField(blank=True, verbose_name="Notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.order_number} - {self.customer_name}"

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Générer un numéro de commande unique
            self.order_number = 'CMD' + ''.join(secrets.choice(string.digits) for _ in range(6))
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    """Message de contact"""
    name = models.CharField(max_length=200, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    subject = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    read = models.BooleanField(default=False, verbose_name="Lu")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class ArtisanVerification(models.Model):
    """Code de vérification pour l'accès au dashboard artisan"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verifications')
    code = models.CharField(max_length=6, verbose_name="Code de vérification")
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False, verbose_name="Utilisé")
    expires_at = models.DateTimeField(verbose_name="Expire à")

    class Meta:
        verbose_name = "Vérification Artisan"
        verbose_name_plural = "Vérifications Artisan"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.code}"

    @classmethod
    def generate_code(cls):
        """Génère un code de 6 chiffres"""
        return ''.join(secrets.choice(string.digits) for _ in range(6))


class Favorite(models.Model):
    """Produit favori d'un utilisateur"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name="Utilisateur")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by', verbose_name="Produit")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")

    class Meta:
        verbose_name = "Favori"
        verbose_name_plural = "Favoris"
        unique_together = ['user', 'product']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
