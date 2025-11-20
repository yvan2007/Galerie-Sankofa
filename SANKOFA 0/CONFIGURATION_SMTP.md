# Configuration SMTP - Galerie Sankofa

## Option 1 : Gmail (Recommandé pour le développement)

### Étapes :

1. **Activer la validation en 2 étapes** sur votre compte Gmail
   - Allez sur : https://myaccount.google.com/security
   - Activez la "Validation en deux étapes"

2. **Créer un mot de passe d'application**
   - Allez sur : https://myaccount.google.com/apppasswords
   - Sélectionnez "Application" : "Courrier"
   - Sélectionnez "Appareil" : "Autre (nom personnalisé)"
   - Entrez "Galerie Sankofa"
   - Cliquez sur "Générer"
   - **Copiez le mot de passe de 16 caractères** (sans espaces)

3. **Configurer dans settings.py** :
   ```python
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'votre-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'votre-mot-de-passe-application-16-caracteres'
   ```

---

## Option 2 : Outlook / Hotmail

### Étapes :

1. **Activer la validation en 2 étapes** sur votre compte Microsoft
   - Allez sur : https://account.microsoft.com/security
   - Activez la "Validation en deux étapes"

2. **Créer un mot de passe d'application**
   - Allez sur : https://account.microsoft.com/security/app-passwords
   - Créez un nouveau mot de passe d'application
   - **Copiez le mot de passe**

3. **Configurer dans settings.py** :
   ```python
   EMAIL_HOST = 'smtp-mail.outlook.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'votre-email@outlook.com'
   EMAIL_HOST_PASSWORD = 'votre-mot-de-passe-application'
   ```

---

## Option 3 : Yahoo Mail

### Étapes :

1. **Activer la validation en 2 étapes** sur votre compte Yahoo
   - Allez sur : https://login.yahoo.com/account/security
   - Activez la "Validation en deux étapes"

2. **Créer un mot de passe d'application**
   - Allez sur : https://login.yahoo.com/account/security/app-passwords
   - Créez un nouveau mot de passe d'application
   - **Copiez le mot de passe**

3. **Configurer dans settings.py** :
   ```python
   EMAIL_HOST = 'smtp.mail.yahoo.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'votre-email@yahoo.com'
   EMAIL_HOST_PASSWORD = 'votre-mot-de-passe-application'
   ```

---

## Option 4 : Serveur SMTP personnalisé

Si vous avez votre propre serveur SMTP :

```python
EMAIL_HOST = 'smtp.votre-domaine.com'
EMAIL_PORT = 587  # ou 465 pour SSL
EMAIL_USE_TLS = True  # False si vous utilisez SSL (port 465)
EMAIL_USE_SSL = False  # True si port 465
EMAIL_HOST_USER = 'votre-email@votre-domaine.com'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe'
```

---

## Test de la configuration

Après avoir configuré, testez avec cette commande :

```bash
python manage.py shell
```

Puis dans le shell :
```python
from django.core.mail import send_mail
send_mail(
    'Test SMTP',
    'Ceci est un test de configuration SMTP.',
    'votre-email@gmail.com',
    ['votre-email@gmail.com'],
    fail_silently=False,
)
```

Si vous recevez l'email, la configuration est correcte !

---

## Sécurité (Recommandé)

Pour plus de sécurité, utilisez des variables d'environnement au lieu de mettre les mots de passe directement dans settings.py.

1. Installez `python-decouple` :
   ```bash
   pip install python-decouple
   ```

2. Créez un fichier `.env` à la racine du projet :
   ```
   EMAIL_HOST_USER=votre-email@gmail.com
   EMAIL_HOST_PASSWORD=votre-mot-de-passe-application
   ```

3. Modifiez `settings.py` :
   ```python
   from decouple import config
   
   EMAIL_HOST_USER = config('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
   ```

4. Ajoutez `.env` à votre `.gitignore` pour ne pas le commiter !

