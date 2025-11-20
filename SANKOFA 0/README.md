# 🎨 Galerie Sankofa - Plateforme E-commerce Artisanat Traditionnel Ivoirien

## 📋 Description

**Galerie Sankofa** est une plateforme e-commerce complète développée en Django pour la vente d'artisanat traditionnel ivoirien. Le projet offre une interface web moderne, un dashboard artisan complet, une API REST avec documentation Swagger, et un système d'authentification avancé.

## ✨ Fonctionnalités Principales

### 🌐 Site Web Public
- **Accueil** : Hero section, produits en vedette, témoignages
- **Galerie** : Catalogue complet avec filtres par catégorie
- **Détails produit** : Pages détaillées avec images, descriptions, système de favoris
- **À propos** : Histoire, valeurs, mission de la galerie
- **Contact** : Formulaire de contact fonctionnel

### 👤 Espace Client
- **Inscription/Connexion** : 
  - Inscription classique avec email
  - Connexion via Google OAuth
  - Réinitialisation de mot de passe par email
- **Profil utilisateur** : Gestion des informations personnelles
- **Système de favoris** : Ajouter/retirer des produits en favoris
- **Commandes** : 
  - Création de commande avec validation de stock
  - Auto-remplissage des informations pour utilisateurs connectés
  - Suivi des commandes en temps réel
- **Historique** : Consultation de toutes les commandes passées

### 🎯 Dashboard Artisan
- **Vue d'ensemble** : 
  - Statistiques complètes (ventes, produits, commandes)
  - Prédictions mensuelles
  - Alertes stock faible
- **Gestion produits** : 
  - CRUD complet (Créer, Lire, Modifier, Supprimer)
  - Upload d'images
  - Éditeur de texte riche (CKEditor)
  - Gestion du stock
- **Gestion catégories** : CRUD complet
- **Gestion commandes** : 
  - Mise à jour des statuts (en attente, en cours, livrée, annulée)
  - Vue détaillée de toutes les commandes
- **Sécurité** : 
  - Compte artisan unique
  - Authentification 2FA par email
  - Code de vérification requis à chaque connexion

### 🔌 API REST
- **Documentation Swagger** : Interface interactive pour tester l'API
- **Endpoints disponibles** :
  - `/api/products/` - Gestion des produits
  - `/api/categories/` - Gestion des catégories
  - `/api/orders/` - Gestion des commandes
  - `/api/favorites/` - Gestion des favoris
  - `/api/profiles/` - Gestion des profils
- **Authentification** : Session-based authentication
- **Permissions** : Gestion fine des permissions selon les rôles

### 📧 Système d'Emails
- **Email de bienvenue** : Envoyé lors de l'inscription
- **Réinitialisation de mot de passe** : Email avec lien de réinitialisation
- **2FA Artisan** : Code de vérification par email
- **Notifications** : (Prêt pour extension)

## 🏗️ Architecture du Projet

```
Galerie-Sankofa/
├── galerie/                      # Application principale
│   ├── models.py                 # Modèles de données (Product, Category, Order, etc.)
│   ├── views.py                  # Vues publiques (home, gallery, product_detail, etc.)
│   ├── views_auth.py             # Vues d'authentification (login, register, 2FA)
│   ├── views_dashboard.py        # Vues dashboard artisan (CRUD)
│   ├── views_api.py              # Vues API REST (ViewSets)
│   ├── serializers.py            # Serializers pour l'API
│   ├── forms.py                  # Formulaires Django
│   ├── widgets.py                # Widgets personnalisés (téléphone avec code pays)
│   ├── adapters.py               # Adaptateurs allauth personnalisés
│   ├── urls.py                   # URLs de l'application
│   ├── urls_api.py               # URLs de l'API REST
│   ├── admin.py                  # Configuration admin Django
│   ├── templates/                # Templates HTML
│   │   ├── galerie/              # Templates pages publiques
│   │   │   ├── home.html
│   │   │   ├── gallery.html
│   │   │   ├── product_detail.html
│   │   │   ├── dashboard.html
│   │   │   └── emails/           # Templates emails
│   │   └── socialaccount/        # Templates OAuth
│   ├── static/                   # Fichiers statiques
│   │   ├── css/                  # Styles CSS
│   │   └── js/                   # JavaScript
│   ├── management/commands/      # Commandes Django personnalisées
│   └── migrations/               # Migrations base de données
│
├── sankofa_project/              # Configuration Django
│   ├── settings.py               # Paramètres (avec variables d'environnement)
│   ├── urls.py                   # URLs principales + Swagger
│   ├── wsgi.py                   # WSGI pour production
│   └── asgi.py                   # ASGI pour production
│
├── templates/                     # Templates globaux
│   └── admin/                    # Templates admin personnalisés
│
├── static/                        # Fichiers statiques globaux
│   └── admin/                    # CSS admin personnalisé
│
├── media/                         # Fichiers uploadés (non versionné)
│   └── products/                 # Images produits
│
├── requirements.txt               # Dépendances Python
├── env.example                    # Exemple de fichier .env
├── README.md                      # Ce fichier
├── README_CONFIG.md               # Guide de configuration
└── .gitignore                     # Fichiers ignorés par Git
```

## 🗄️ Modèles de Données

### Product (Produit)
- Nom, slug, description, détails (rich text)
- Prix, catégorie, images
- Disponibilité, stock
- Dates de création/modification

### Category (Catégorie)
- Nom, slug, description

### Order (Commande)
- Numéro de commande unique
- Client, produit, quantité, total
- Statut (en attente, en cours, livrée, annulée)
- Informations client (nom, téléphone, adresse)
- Notes

### Favorite (Favoris)
- Utilisateur, produit
- Date d'ajout

### Profile (Profil)
- Utilisateur, rôle (visitor, client, artisan)
- Téléphone, adresse, WhatsApp

### ArtisanVerification (Vérification Artisan)
- Utilisateur, code de vérification
- Expiration, statut d'utilisation

## 🎨 Technologies Utilisées

### Backend
- **Django 5.2.8** : Framework web Python
- **Django REST Framework** : API REST
- **drf-yasg** : Documentation Swagger/OpenAPI
- **django-allauth** : Authentification et OAuth Google
- **CKEditor** : Éditeur de texte riche
- **Pillow** : Traitement d'images

### Frontend
- **HTML5/CSS3** : Structure et styles
- **JavaScript** : Interactivité
- **Font Awesome** : Icônes
- **CKEditor** : Éditeur WYSIWYG

### Base de données
- **SQLite** : Développement (peut être migré vers PostgreSQL/MySQL en production)

## 🔐 Sécurité

- ✅ Secrets dans variables d'environnement (pas dans le code)
- ✅ Authentification 2FA pour artisans
- ✅ Permissions basées sur les rôles
- ✅ Protection CSRF
- ✅ Validation des formulaires
- ✅ Gestion sécurisée des uploads

## 📱 Responsive Design

Le site est entièrement responsive :
- **Mobile** : Navigation hamburger, colonne unique
- **Tablette** : 2 colonnes pour les produits
- **Desktop** : 3-4 colonnes, navigation complète

## 🌟 Points Forts

1. **Code propre et organisé** : Architecture MVC respectée
2. **API REST complète** : Prête pour applications mobiles
3. **Documentation Swagger** : Interface interactive pour tester l'API
4. **Sécurité renforcée** : 2FA, permissions, validation
5. **Interface moderne** : Design soigné et responsive
6. **Gestion complète** : CRUD pour tous les modèles
7. **Emails fonctionnels** : SMTP configuré et testé
8. **OAuth Google** : Connexion sociale intégrée

## 📊 Statistiques Dashboard

Le dashboard artisan affiche :
- Total des ventes
- Nombre de produits (en stock / épuisés)
- Commandes (en attente, en cours, livrées)
- Prédictions mensuelles
- Valeur moyenne des commandes
- Stock total

## 🚀 Déploiement

Le projet est prêt pour le déploiement en production :
- Configuration via variables d'environnement
- Support PostgreSQL/MySQL
- Collecte des fichiers statiques
- Configuration WSGI/ASGI

## 📝 Licence

Ce projet est créé pour la Galerie Sankofa. Tous droits réservés.

---

**Galerie Sankofa** - Artisanat traditionnel ivoirien à l'ère du digital

Pour la configuration et l'installation, consultez [README_CONFIG.md](README_CONFIG.md)
