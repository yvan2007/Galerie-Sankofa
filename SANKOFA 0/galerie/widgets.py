"""Widgets personnalisés"""
from django import forms
from .data.country_codes import COUNTRY_CODES


class CountryCodePhoneWidget(forms.MultiWidget):
    """Widget pour sélectionner le code pays et le numéro de téléphone"""
    
    def __init__(self, attrs=None):
        # Tous les codes pays avec drapeaux
        country_codes = COUNTRY_CODES
        
        widgets = (
            forms.Select(attrs={
                'class': 'form-input country-code-select',
                'style': 'width: 280px; flex-shrink: 0; font-size: 0.9375rem;'
            }, choices=country_codes),
            forms.TextInput(attrs={
                'class': 'form-input phone-number-input',
                'placeholder': 'Numéro de téléphone',
                'style': 'flex: 1;'
            })
        )
        super().__init__(widgets, attrs)
    
    def decompress(self, value):
        """Décompose la valeur en code pays et numéro"""
        if value:
            # Si c'est déjà une liste (venant de la base de données ou du formulaire)
            if isinstance(value, list):
                if len(value) >= 2:
                    return [value[0] or '+225', value[1] or '']
                return ['+225', value[0] if value else '']
            # Si c'est une chaîne
            if isinstance(value, str):
                # Si la valeur commence par un code pays connu
                for code, _ in self.widgets[0].choices:
                    if value.startswith(code):
                        return [code, value[len(code):].strip()]
                # Sinon, on assume +225 par défaut
                if value.startswith('+'):
                    # Extraire le code (premiers chiffres après +)
                    import re
                    match = re.match(r'^\+(\d{1,3})', value)
                    if match:
                        code = '+' + match.group(1)
                        number = value[len(code):].strip()
                        return [code, number]
                return ['+225', value]
        return ['+225', '']
    
    def format_output(self, rendered_widgets):
        """Formate la sortie avec les deux widgets côte à côte"""
        return f'''
        <div style="display: flex; gap: 0.5rem; align-items: center;">
            {rendered_widgets[0]}
            {rendered_widgets[1]}
        </div>
        '''
    
    def value_from_datadict(self, data, files, name):
        """Retourne une liste de valeurs pour MultiValueField"""
        code = data.get(f'{name}_0', '+225')
        number = data.get(f'{name}_1', '')
        return [code, number]


class CountryCodePhoneField(forms.MultiValueField):
    """Champ pour code pays + numéro de téléphone"""
    
    def __init__(self, *args, **kwargs):
        # Tous les codes pays avec drapeaux
        country_codes = COUNTRY_CODES
        
        fields = (
            forms.ChoiceField(choices=country_codes, initial='+225'),
            forms.CharField(max_length=25)
        )
        widget = CountryCodePhoneWidget()
        super().__init__(fields=fields, widget=widget, *args, **kwargs)
    
    def compress(self, data_list):
        """Combine les valeurs en une seule chaîne"""
        if data_list and len(data_list) >= 2:
            code = data_list[0] if data_list[0] else '+225'
            number = data_list[1] if len(data_list) > 1 else ''
            if number and number.strip():
                return f"{code} {number.strip()}"
        # Si pas de numéro, lever une erreur de validation
        from django.core.exceptions import ValidationError
        raise ValidationError('Veuillez entrer un numéro de téléphone valide.')
    
    def clean(self, value):
        """Validation personnalisée pour le champ"""
        if value:
            return value
        from django.core.exceptions import ValidationError
        raise ValidationError('Ce champ est obligatoire.')

