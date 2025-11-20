from django import forms
from .models import Product, Order, ContactMessage, Category
from .widgets import CountryCodePhoneField


class OrderForm(forms.ModelForm):
    """Formulaire de commande avec sélecteur de code pays"""
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False
    )
    customer_phone = CountryCodePhoneField(
        label='Téléphone',
        required=True
    )
    
    class Meta:
        model = Order
        fields = ['quantity', 'customer_name', 'customer_phone', 'customer_address', 'notes']
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'form-input',
                'min': 1,
                'value': 1,
                'id': 'id_quantity'
            }),
            'customer_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Votre nom complet'
            }),
            'customer_address': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 3,
                'placeholder': 'Ville, quartier, détails d\'adresse...'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 3,
                'placeholder': 'Notes supplémentaires (optionnel)'
            }),
        }
    
    def clean_quantity(self):
        """Valider la quantité"""
        quantity = self.cleaned_data.get('quantity')
        if quantity and quantity < 1:
            raise forms.ValidationError('La quantité doit être au moins 1.')
        return quantity


class ContactForm(forms.ModelForm):
    """Formulaire de contact"""
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Votre nom'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'votre@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+225 07 00 00 00 00'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Sujet de votre message'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 6,
                'placeholder': 'Écrivez votre message ici...'
            }),
        }


class ProductForm(forms.ModelForm):
    """Formulaire de produit avec CKEditor"""
    class Meta:
        model = Product
        fields = ['name', 'description', 'details', 'price', 'category', 'image', 'image_url', 'stock', 'availability']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nom du produit'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 3,
                'placeholder': 'Description courte'
            }),
            'details': forms.Textarea(attrs={
                'class': 'form-textarea ckeditor',
                'rows': 10,
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'min': 0,
                'placeholder': 'Prix en XOF'
            }),
            'category': forms.Select(attrs={
                'class': 'form-input',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-input',
                'accept': 'image/*'
            }),
            'image_url': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'https://... (si pas d\'upload)'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-input',
                'min': 0,
                'placeholder': 'Quantité en stock'
            }),
            'availability': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
        }


class CategoryForm(forms.ModelForm):
    """Formulaire de catégorie"""
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nom de la catégorie'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 3,
                'placeholder': 'Description de la catégorie'
            }),
        }
