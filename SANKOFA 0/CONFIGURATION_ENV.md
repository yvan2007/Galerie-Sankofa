# Configuration des Variables d'Environnement

## 📋 Pourquoi utiliser les variables d'environnement ?

Après avoir mis le projet sur GitHub, les secrets (mots de passe, clés API) ne doivent **jamais** être dans le code. Ils doivent être dans un fichier `.env` qui n'est **pas versionné**.

## 🚀 Configuration Rapide

### Option 1 : Fichier .env (Recommandé)

1. **Créez un fichier `.env` à la racine du projet** (à côté de `manage.py`)

2. **Copiez le contenu de `env.example`** et remplissez avec vos vraies valeurs :

```env
# Configuration Email (SMTP)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password-16-characters

# Configuration Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Django Secret Key
SECRET_KEY=your-django-secret-key-here
```

3. **Le fichier `.env` est automatiquement ignoré par Git** (dans `.gitignore`)

### Option 2 : Variables d'environnement système

Sur Windows (PowerShell) :
```powershell
$env:EMAIL_HOST_USER="your-email@gmail.com"
$env:EMAIL_HOST_PASSWORD="your-app-password"
$env:GOOGLE_CLIENT_ID="your-google-client-id.apps.googleusercontent.com"
$env:GOOGLE_CLIENT_SECRET="your-google-client-secret"
$env:SECRET_KEY="your-django-secret-key"
```

Sur Linux/Mac :
```bash
export EMAIL_HOST_USER="your-email@gmail.com"
export EMAIL_HOST_PASSWORD="your-app-password"
export GOOGLE_CLIENT_ID="your-google-client-id.apps.googleusercontent.com"
export GOOGLE_CLIENT_SECRET="your-google-client-secret"
export SECRET_KEY="your-django-secret-key"
```

## ✅ Vérification

Après configuration, testez que tout fonctionne :

1. **Test d'envoi d'email** :
```bash
python manage.py shell
```
Puis dans le shell :
```python
from django.core.mail import send_mail
send_mail(
    'Test Email',
    'Ceci est un test.',
    'your-email@gmail.com',
    ['your-email@gmail.com'],
    fail_silently=False,
)
```

2. **Test de création de compte** :
   - Allez sur `/inscription/`
   - Créez un compte
   - Vérifiez que l'email de bienvenue arrive

3. **Test Google OAuth** :
   - Allez sur `/connexion/`
   - Cliquez sur "Continuer avec Google"
   - Vérifiez que la connexion fonctionne

## 🔒 Sécurité

- ✅ Le fichier `.env` est dans `.gitignore` → **jamais commité**
- ✅ Les secrets ne sont pas dans le code versionné
- ✅ Chaque développeur a son propre `.env` local
- ✅ En production, utilisez les variables d'environnement du serveur

## 📝 Note

Si vous n'avez pas encore configuré les variables d'environnement, `settings.py` utilisera les valeurs par défaut (`'your-email@gmail.com'`, etc.) qui ne fonctionneront pas. **Vous devez configurer le fichier `.env` pour que les emails fonctionnent.**

