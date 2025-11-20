# ⚙️ Guide de Configuration - Galerie Sankofa

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Git (optionnel, pour cloner le projet)

## 🚀 Installation

### 1. Cloner le projet (ou télécharger)

```bash
git clone https://github.com/yvan2007/Galerie-Sankofa.git
cd Galerie-Sankofa
```

### 2. Créer un environnement virtuel

**Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet (à côté de `manage.py`) :

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

**OU** copiez `env.example` vers `.env` et modifiez les valeurs :

```bash
cp env.example .env
# Puis éditez .env avec vos vraies valeurs
```

### 5. Appliquer les migrations

```bash
python manage.py migrate
```

### 6. Créer un superutilisateur (optionnel)

```bash
python manage.py createsuperuser
```

### 7. Charger les données initiales (optionnel)

```bash
python manage.py load_initial_data
```

### 8. Lancer le serveur de développement

```bash
python manage.py runserver
```

Le site sera accessible sur `http://127.0.0.1:8000`

## 📧 Configuration Email (SMTP)

### Gmail (Recommandé pour le développement)

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

3. **Configurer dans `.env`** :
   ```env
   EMAIL_HOST_USER=votre-email@gmail.com
   EMAIL_HOST_PASSWORD=mot-de-passe-application-16-caracteres
   ```

### Tester l'envoi d'email

```bash
python manage.py shell
```

Puis dans le shell :
```python
from django.core.mail import send_mail
send_mail(
    'Test Email',
    'Ceci est un test.',
    'votre-email@gmail.com',
    ['votre-email@gmail.com'],
    fail_silently=False,
)
```

## 🔐 Configuration Google OAuth

1. **Créer un projet sur Google Cloud Console**
   - Allez sur : https://console.cloud.google.com/
   - Créez un nouveau projet

2. **Activer l'API Google+**
   - APIs & Services → Library
   - Rechercher "Google+ API"
   - Cliquer sur "Enable"

3. **Créer des identifiants OAuth 2.0**
   - APIs & Services → Credentials
   - Cliquer sur "Create Credentials" → "OAuth client ID"
   - Type d'application : **Web application**
   - Nom : `Galerie Sankofa`
   
4. **Configurer les URI autorisés**
   - **Origines JavaScript autorisées** :
     - `http://127.0.0.1:8000`
     - `http://localhost:8000`
   - **URI de redirection autorisés** :
     - `http://127.0.0.1:8000/accounts/google/login/callback/`
     - `http://localhost:8000/accounts/google/login/callback/`

5. **Configurer dans `.env`** :
   ```env
   GOOGLE_CLIENT_ID=votre-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=votre-client-secret
   ```

## 🗄️ Base de Données

### Développement (SQLite)

Par défaut, le projet utilise SQLite. Aucune configuration supplémentaire n'est nécessaire.

### Production (PostgreSQL/MySQL)

Modifiez `sankofa_project/settings.py` :

**PostgreSQL :**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'galerie_sankofa',
        'USER': 'votre_user',
        'PASSWORD': 'votre_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**MySQL :**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'galerie_sankofa',
        'USER': 'votre_user',
        'PASSWORD': 'votre_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Puis installez le driver :
```bash
# Pour PostgreSQL
pip install psycopg2-binary

# Pour MySQL
pip install mysqlclient
```

## 🔌 API REST et Swagger

### Accéder à la documentation Swagger

Une fois le serveur lancé :
- **Swagger UI** : http://127.0.0.1:8000/swagger/
- **ReDoc** : http://127.0.0.1:8000/redoc/
- **Schema JSON** : http://127.0.0.1:8000/swagger.json
- **Schema YAML** : http://127.0.0.1:8000/swagger.yaml

### Endpoints API disponibles

- `GET/POST /api/products/` - Liste et création de produits
- `GET/PUT/PATCH/DELETE /api/products/{slug}/` - Détails, modification, suppression
- `POST /api/products/{slug}/toggle_favorite/` - Ajouter/retirer des favoris
- `GET/POST /api/categories/` - Liste et création de catégories
- `GET/POST /api/orders/` - Liste et création de commandes
- `PATCH /api/orders/{id}/update_status/` - Mettre à jour le statut
- `GET /api/favorites/` - Liste des favoris
- `GET/PUT/PATCH /api/profiles/` - Gestion du profil

### Authentification API

L'API utilise l'authentification par session Django. Pour tester :

1. Connectez-vous sur le site web
2. Ouvrez Swagger UI
3. Les requêtes authentifiées utiliseront votre session

## 👤 Créer un compte Artisan

### Méthode 1 : Via l'admin Django

1. Créez un superutilisateur si ce n'est pas déjà fait :
   ```bash
   python manage.py createsuperuser
   ```

2. Connectez-vous sur `/admin/`

3. Créez un utilisateur dans "Users"

4. Créez un profil pour cet utilisateur dans "Profiles" avec le rôle "artisan"

### Méthode 2 : Via le shell Django

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
from galerie.models import Profile

# Créer l'utilisateur
user = User.objects.create_user(
    username='artisan',
    email='artisan@example.com',
    password='mot-de-passe-securise'
)

# Créer le profil artisan
profile = Profile.objects.create(
    user=user,
    role='artisan'
)
```

## 🧪 Tests

### Tester l'envoi d'emails artisan

```bash
python manage.py test_artisan_email
```

### Tester la création de compte

1. Allez sur `/inscription/`
2. Remplissez le formulaire
3. Vérifiez que l'email de bienvenue arrive

### Tester Google OAuth

1. Allez sur `/connexion/`
2. Cliquez sur "Continuer avec Google"
3. Connectez-vous avec votre compte Google
4. Vérifiez que le compte est créé automatiquement

## 🚀 Déploiement en Production

### 1. Configuration

Modifiez `sankofa_project/settings.py` :

```python
DEBUG = False
ALLOWED_HOSTS = ['votre-domaine.com', 'www.votre-domaine.com']

# Utilisez une base de données PostgreSQL ou MySQL
# Configurez les variables d'environnement sur le serveur
```

### 2. Collecter les fichiers statiques

```bash
python manage.py collectstatic
```

### 3. Utiliser un serveur WSGI

**Gunicorn :**
```bash
pip install gunicorn
gunicorn sankofa_project.wsgi:application
```

**uWSGI :**
```bash
pip install uwsgi
uwsgi --http :8000 --module sankofa_project.wsgi
```

### 4. Configurer Nginx (recommandé)

Exemple de configuration Nginx pour servir les fichiers statiques et proxy vers Gunicorn.

## 📦 Dépendances

Le fichier `requirements.txt` contient :
- Django==5.2.8
- Pillow==12.0.0
- django-ckeditor==6.7.3
- django-allauth
- djangorestframework==3.14.0
- drf-yasg==1.21.7
- requests
- PyJWT
- cryptography

## ❓ Problèmes Courants

### Erreur : "No module named 'django'"

**Solution :** Activez votre environnement virtuel et installez les dépendances :
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Erreur : "ModuleNotFoundError: No module named 'requests'"

**Solution :** Installez les dépendances manquantes :
```bash
pip install requests PyJWT cryptography
```

### Les emails ne partent pas

**Solution :** 
1. Vérifiez que `.env` est bien configuré
2. Vérifiez que le mot de passe d'application Gmail est correct
3. Testez avec `python manage.py shell` (voir section "Tester l'envoi d'email")

### Google OAuth ne fonctionne pas

**Solution :**
1. Vérifiez que les identifiants sont corrects dans `.env`
2. Vérifiez que les URI de redirection sont bien configurés dans Google Cloud Console
3. Vérifiez que l'API Google+ est activée

## 📞 Support

Pour toute question ou problème, consultez :
- La documentation Django : https://docs.djangoproject.com/
- La documentation DRF : https://www.django-rest-framework.org/
- La documentation Swagger : https://drf-yasg.readthedocs.io/

---

**Bon développement ! 🚀**

