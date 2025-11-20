# Galerie Sankofa - Site Web Artisanat Traditionnel Ivoirien

## 📋 Description

Site web complet pour la **Galerie Sankofa**, une plateforme de vente d'artisanat traditionnel ivoirien. Le site est développé en **Django** avec une interface moderne et responsive.

## 🎨 Caractéristiques

### Design
- **Palette de couleurs** : Doré (#CBA135), Brun foncé (#3E2C1B), Crème (#FFFFF0)
- **Design responsive** : Adapté mobile, tablette et desktop
- **Interface moderne** : Animations fluides et transitions élégantes
- **Navigation intuitive** : Menu adaptatif selon le rôle utilisateur

### Pages Disponibles

1. **Accueil** : Hero section, présentation, produits en vedette, témoignages
2. **Galerie** : Catalogue complet avec filtres par catégorie
3. **À propos** : Histoire, valeurs, mission de la galerie
4. **Contact** : Formulaire de contact et informations de contact
5. **Détails produit** : Page détaillée avec images, descriptions, commande
6. **Commande** : Formulaire de commande en ligne avec validation de stock
7. **Suivi commande** : Suivi des commandes clients
8. **Profil** : Profil utilisateur avec favoris
9. **Connexion** : Page de connexion avec Google OAuth
10. **Dashboard** : Tableau de bord artisan avec statistiques et gestion CRUD

### Fonctionnalités

- ✅ **Authentification** : Connexion client/artisan avec Google OAuth
- ✅ **Gestion des rôles** : Visiteur, Client, Artisan (unique)
- ✅ **Dashboard Artisan** : CRUD produits/catégories, gestion commandes
- ✅ **Système de favoris** : Clients peuvent ajouter des produits en favoris
- ✅ **Validation de stock** : Vérification automatique lors des commandes
- ✅ **Email** : Envoi d'emails (bienvenue, réinitialisation, 2FA artisan)
- ✅ **2FA Artisan** : Vérification par email pour l'accès au dashboard
- ✅ **Gestion commandes** : Suivi des statuts (en attente, en cours, livrée)
- ✅ **Responsive design** : Mobile-first approach

## 🚀 Installation

### Prérequis

- Python 3.8+
- pip
- Git

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/yvan2007/Galerie-Sankofa.git
cd Galerie-Sankofa
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**

Créez un fichier `.env` à la racine du projet (ou configurez directement `settings.py`) :

```env
SECRET_KEY=votre-secret-key-django
EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-de-passe-application
GOOGLE_CLIENT_ID=votre-google-client-id
GOOGLE_CLIENT_SECRET=votre-google-client-secret
```

**OU** copiez `sankofa_project/settings.example.py` vers `sankofa_project/settings.py` et modifiez les valeurs.

5. **Appliquer les migrations**
```bash
python manage.py migrate
```

6. **Créer un superutilisateur (optionnel)**
```bash
python manage.py createsuperuser
```

7. **Charger les données initiales (optionnel)**
```bash
python manage.py load_initial_data
```

8. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

Le site sera accessible sur `http://127.0.0.1:8000`

## 📁 Structure du Projet

```
Galerie-Sankofa/
├── galerie/                 # Application principale
│   ├── models.py           # Modèles de données
│   ├── views.py            # Vues publiques
│   ├── views_auth.py       # Vues d'authentification
│   ├── views_dashboard.py  # Vues dashboard artisan
│   ├── forms.py            # Formulaires Django
│   ├── widgets.py          # Widgets personnalisés
│   ├── adapters.py         # Adaptateurs allauth
│   ├── templates/          # Templates HTML
│   └── static/             # Fichiers statiques
├── sankofa_project/        # Configuration Django
│   ├── settings.py         # Paramètres (à configurer)
│   └── urls.py             # URLs principales
├── templates/              # Templates globaux
├── static/                 # Fichiers statiques
├── media/                  # Fichiers uploadés (non versionné)
├── requirements.txt        # Dépendances Python
└── README.md              # Ce fichier
```

## ⚙️ Configuration

### Configuration Email (SMTP Gmail)

1. Activez l'authentification à deux facteurs sur votre compte Gmail
2. Générez un mot de passe d'application : [Google Account](https://myaccount.google.com/apppasswords)
3. Configurez dans `settings.py` ou `.env` :
   - `EMAIL_HOST_USER` : Votre email Gmail
   - `EMAIL_HOST_PASSWORD` : Le mot de passe d'application généré

### Configuration Google OAuth

1. Créez un projet sur [Google Cloud Console](https://console.cloud.google.com/)
2. Activez l'API Google+
3. Créez des identifiants OAuth 2.0
4. Ajoutez l'URI de redirection : `http://127.0.0.1:8000/accounts/google/login/callback/`
5. Configurez dans `settings.py` ou `.env` :
   - `GOOGLE_CLIENT_ID` : Votre Client ID
   - `GOOGLE_CLIENT_SECRET` : Votre Client Secret

## 🔐 Sécurité

⚠️ **IMPORTANT** : Ne commitez jamais :
- `db.sqlite3` (base de données)
- `settings.py` avec des secrets (utilisez `settings.example.py`)
- Fichiers dans `media/` (uploads utilisateurs)
- Fichiers dans `venv/` (environnement virtuel)

Le fichier `.gitignore` est configuré pour exclure ces fichiers automatiquement.

## 📝 Utilisation

### Compte Artisan

- **Création** : Via l'admin Django ou directement en base de données
- **Connexion** : `/connexion/?type=artisan`
- **2FA** : Un code de vérification est envoyé par email
- **Dashboard** : `/dashboard/` après vérification

### Compte Client

- **Inscription** : `/inscription/` ou connexion Google
- **Connexion** : `/connexion/?type=client` ou bouton Google
- **Profil** : `/profil/` pour gérer ses informations et favoris

## 🧪 Tests

```bash
# Tester l'envoi d'emails artisan
python manage.py test_artisan_email
```

## 🚀 Déploiement

### Production

1. Configurez `DEBUG = False` dans `settings.py`
2. Configurez `ALLOWED_HOSTS` avec votre domaine
3. Utilisez une base de données PostgreSQL ou MySQL
4. Configurez les fichiers statiques avec `python manage.py collectstatic`
5. Utilisez un serveur WSGI (Gunicorn, uWSGI)
6. Configurez un serveur web (Nginx, Apache)

## 📄 Licence

Ce projet est créé pour la Galerie Sankofa. Tous droits réservés.

---

**Galerie Sankofa** - Artisanat traditionnel ivoirien à l'ère du digital
