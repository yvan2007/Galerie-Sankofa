# Galerie Sankofa - Version Django

## 🚀 Installation et Démarrage

### Prérequis
- Python 3.8+
- pip

### Étapes d'installation

1. **Activer l'environnement virtuel** (déjà créé)
   ```bash
   .\venv\Scripts\activate
   ```

2. **Installer les dépendances** (déjà fait)
   ```bash
   pip install django pillow
   ```

3. **Créer un superutilisateur** (pour accéder à l'admin Django)
   ```bash
   python manage.py createsuperuser
   ```

4. **Charger les données initiales** (produits et catégories)
   ```bash
   python manage.py load_initial_data
   ```

5. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

6. **Accéder au site**
   - Site web : http://127.0.0.1:8000/
   - Admin Django : http://127.0.0.1:8000/admin/

## 📁 Structure du Projet Django

```
SANKOFA 0/
├── manage.py                 # Script de gestion Django
├── sankofa_project/          # Configuration du projet
│   ├── settings.py          # Paramètres Django
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuration WSGI
├── galerie/                 # Application principale
│   ├── models.py            # Modèles (Product, Order, Category, etc.)
│   ├── views.py              # Vues (Controllers)
│   ├── forms.py              # Formulaires
│   ├── urls.py               # URLs de l'application
│   ├── admin.py              # Configuration admin Django
│   ├── management/
│   │   └── commands/
│   │       └── load_initial_data.py  # Script de chargement des données
│   └── migrations/           # Migrations de base de données
├── templates/                # Templates HTML
│   └── galerie/
│       ├── base.html         # Template de base
│       ├── home.html         # Page d'accueil
│       ├── gallery.html      # Galerie produits
│       ├── product_detail.html  # Détails produit
│       ├── about.html        # À propos
│       ├── contact.html      # Contact
│       ├── order.html        # Commande
│       ├── tracking.html     # Suivi commandes
│       ├── profile.html     # Profil utilisateur
│       ├── login.html        # Connexion
│       ├── register.html     # Inscription
│       └── dashboard.html    # Dashboard artisan
├── static/                   # Fichiers statiques (CSS, JS, images)
│   ├── css/                  # Styles CSS (copiés depuis le projet original)
│   └── js/                   # Scripts JavaScript (copiés depuis le projet original)
├── media/                    # Fichiers uploadés (images produits)
└── db.sqlite3               # Base de données SQLite
```

## 🎯 Fonctionnalités

### Pages Publiques
- **Accueil** : Hero section, produits en vedette, témoignages
- **Galerie** : Catalogue complet avec filtres par catégorie
- **Détails Produit** : Page détaillée avec images, descriptions, commande
- **À propos** : Histoire, valeurs, mission
- **Contact** : Formulaire de contact

### Pages Client (nécessite connexion)
- **Commande** : Formulaire de commande en ligne
- **Suivi** : Suivi des commandes avec statuts
- **Profil** : Gestion du profil utilisateur

### Pages Artisan (nécessite connexion artisan)
- **Dashboard** : Tableau de bord avec statistiques
  - Vue d'ensemble : Ventes, produits, commandes
  - Gestion produits : Liste, ajout, modification, suppression
  - Gestion commandes : Liste et changement de statut

## 🔐 Authentification

### Mode Démo
- **Connexion** : Entrez n'importe quel email et mot de passe
- Le système créera automatiquement un compte si l'email n'existe pas
- Pour devenir artisan : Connectez-vous puis modifiez votre profil dans l'admin Django

### Créer un compte Artisan
1. Créez un compte normal via l'inscription
2. Connectez-vous à l'admin Django : http://127.0.0.1:8000/admin/
3. Allez dans "Profils" → Sélectionnez votre profil → Changez le rôle en "Artisan"

## 🗄️ Base de Données

### Modèles Principaux
- **Category** : Catégories de produits (Céramique, Vannerie, Textile, etc.)
- **Product** : Produits avec images, prix, descriptions
- **Order** : Commandes avec statuts (en attente, en cours, livrée)
- **Profile** : Profils utilisateurs avec rôles (visitor, client, artisan)
- **ContactMessage** : Messages de contact

## 🎨 Design

Le design est **identique à 100%** au projet original :
- ✅ Mêmes couleurs (Doré #CBA135, Brun #3E2C1B, Crème #FFFFF0)
- ✅ Même placement des éléments
- ✅ Mêmes images
- ✅ Même structure HTML/CSS
- ✅ Même responsive design

## 📝 Commandes Utiles

```bash
# Activer le venv
.\venv\Scripts\activate

# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Charger les données initiales
python manage.py load_initial_data

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver

# Collecter les fichiers statiques (pour production)
python manage.py collectstatic
```

## 🔧 Configuration

### Settings importants dans `sankofa_project/settings.py`
- `LANGUAGE_CODE = 'fr-fr'` : Langue française
- `TIME_ZONE = 'Africa/Abidjan'` : Fuseau horaire Côte d'Ivoire
- `MEDIA_URL = '/media/'` : URL pour les fichiers uploadés
- `STATIC_URL = 'static/'` : URL pour les fichiers statiques

## 🌐 URLs Principales

- `/` : Accueil
- `/galerie/` : Galerie produits
- `/produit/<slug>/` : Détails produit
- `/a-propos/` : À propos
- `/contact/` : Contact
- `/commande/` : Créer une commande
- `/commande/<id>/` : Commande avec produit spécifique
- `/suivi/` : Suivi des commandes
- `/profil/` : Profil utilisateur
- `/connexion/` : Connexion
- `/inscription/` : Inscription
- `/dashboard/` : Dashboard artisan
- `/admin/` : Interface d'administration Django

## 🚨 Notes Importantes

1. **Toujours activer le venv** avant d'exécuter des commandes Django
2. Les fichiers CSS et JS sont dans `static/` (copiés depuis le projet original)
3. Les images uploadées seront dans `media/products/`
4. La base de données SQLite est créée automatiquement au premier `migrate`

## 📦 Dépendances

- Django 5.2.8
- Pillow 12.0.0 (pour les images)

## 🎉 C'est prêt !

Votre projet Django est maintenant fonctionnel avec :
- ✅ Backend complet (modèles, vues, formulaires)
- ✅ Design identique au projet original
- ✅ Toutes les fonctionnalités implémentées
- ✅ Architecture MVC respectée
- ✅ Base de données configurée

Bon développement ! 🚀

