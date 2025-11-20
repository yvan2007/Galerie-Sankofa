# 🌳 Arbre du Projet - Galerie Sankofa

## 📁 Structure Complète du Projet

```
SANKOFA 0/
│
├── 📄 index.html                          # Page principale HTML
├── 📄 README.md                           # Documentation principale du projet
├── 📄 ARBRE_PROJET.md                     # Ce fichier - Documentation de l'arborescence
├── 📄 SCRIPT_POWERPOINT_GALERIE_SANKOFA.md # Script pour présentation PowerPoint
├── 📄 docx_content.json                   # Contenu extrait d'un document Word (structure du projet)
├── 📁 Galerie-Sankofa.pptx                # Présentation PowerPoint de la galerie
│
├── 📁 css/                                # Styles CSS organisés par architecture
│   ├── 📄 variables.css                   # Variables CSS (couleurs, espacements, ombres)
│   ├── 📄 base.css                        # Styles de base et reset CSS
│   ├── 📄 layout.css                      # Mise en page générale (grilles, flexbox)
│   ├── 📄 style.css                       # Fichier CSS principal (importe tous les autres)
│   │
│   ├── 📁 components/                     # Styles des composants réutilisables
│   │   ├── 📄 alert.css                   # Styles des alertes/notifications
│   │   ├── 📄 badge.css                   # Styles des badges/étiquettes
│   │   ├── 📄 button.css                  # Styles des boutons
│   │   ├── 📄 card.css                    # Styles des cartes produits
│   │   ├── 📄 footer.css                  # Styles du pied de page
│   │   ├── 📄 form.css                    # Styles des formulaires
│   │   ├── 📄 header.css                  # Styles de l'en-tête/navigation
│   │   ├── 📄 hero.css                    # Styles de la section hero (bannière)
│   │   ├── 📄 table.css                   # Styles des tableaux
│   │   └── 📄 tabs.css                    # Styles des onglets
│   │
│   └── 📁 pages/                          # Styles spécifiques aux pages
│       └── 📄 dashboard.css               # Styles du tableau de bord artisan
│
└── 📁 js/                                 # Scripts JavaScript organisés par architecture
    ├── 📄 app.js                          # Point d'entrée principal de l'application
    │
    ├── 📁 data/                           # Gestion des données
    │   ├── 📄 products.js                 # Données et fonctions des produits
    │   ├── 📄 orders.js                   # Données et fonctions des commandes
    │   └── 📄 helpers.js                  # Fonctions utilitaires pour les données
    │
    ├── 📁 utils/                          # Fonctions utilitaires
    │   ├── 📄 helpers.js                  # Fonctions utilitaires générales
    │   ├── 📄 user.js                     # Gestion des utilisateurs et authentification
    │   └── 📄 mobile.js                   # Fonctions pour la gestion mobile
    │
    ├── 📁 components/                     # Composants JavaScript réutilisables
    │   └── 📄 productCard.js              # Composant carte produit
    │
    ├── 📁 pages/                          # Logique de rendu des pages
    │   ├── 📄 home.js                     # Page d'accueil
    │   ├── 📄 gallery.js                  # Page galerie/catalogue
    │   ├── 📄 product.js                  # Page détails produit
    │   ├── 📄 about.js                    # Page à propos
    │   ├── 📄 contact.js                  # Page contact
    │   ├── 📄 order.js                    # Page formulaire de commande
    │   ├── 📄 tracking.js                 # Page suivi de commande
    │   ├── 📄 profile.js                  # Page profil utilisateur
    │   ├── 📄 login.js                    # Page de connexion
    │   ├── 📄 register.js                 # Page d'inscription
    │   └── 📄 dashboard.js                # Page tableau de bord artisan
    │
    └── 📄 navigation.js                   # Gestion de la navigation SPA (Single Page Application)
```

---

## 📝 Description Détaillée des Fichiers

### 📄 Fichiers Racine

#### `index.html`
**Rôle :** Point d'entrée principal de l'application web
- Structure HTML de base avec header, main et footer
- Contient la navigation principale (desktop et mobile)
- Charge tous les scripts JavaScript dans le bon ordre
- Point de montage pour le contenu dynamique (SPA)

#### `README.md`
**Rôle :** Documentation principale du projet
- Description complète du projet
- Guide d'utilisation
- Instructions d'installation
- Liste des fonctionnalités
- Technologies utilisées

#### `ARBRE_PROJET.md`
**Rôle :** Documentation de l'arborescence du projet (ce fichier)
- Structure complète des fichiers
- Description de chaque fichier et son rôle

#### `SCRIPT_POWERPOINT_GALERIE_SANKOFA.md`
**Rôle :** Script pour créer une présentation PowerPoint
- Contenu structuré pour chaque slide
- Palette de couleurs à utiliser
- Instructions de design

#### `docx_content.json`
**Rôle :** Contenu extrait d'un document Word
- Structure du projet original
- Paragraphes et sections du document source
- Utilisé comme référence pour le développement

#### `Galerie-Sankofa.pptx`
**Rôle :** Présentation PowerPoint de la galerie
- Présentation visuelle du projet
- Design et maquettes

---

### 📁 Dossier `css/`

#### `variables.css`
**Rôle :** Définition des variables CSS globales
- Couleurs principales (doré #CBA135, brun #3E2C1B, crème #FFFFF0)
- Espacements et rayons de bordure
- Ombres et transitions
- Permet une personnalisation centralisée

#### `base.css`
**Rôle :** Styles de base et reset CSS
- Reset des styles par défaut du navigateur
- Styles typographiques de base
- Normalisation des éléments HTML

#### `layout.css`
**Rôle :** Mise en page générale
- Grilles et flexbox pour la structure
- Conteneurs et espacements
- Responsive design de base

#### `style.css`
**Rôle :** Fichier CSS principal
- Importe tous les autres fichiers CSS
- Point d'entrée unique pour les styles
- Chargé dans `index.html`

#### `components/` - Composants CSS

##### `alert.css`
**Rôle :** Styles des alertes et notifications
- Messages d'information, succès, erreur, avertissement
- Animations d'apparition/disparition

##### `badge.css`
**Rôle :** Styles des badges et étiquettes
- Badges de catégorie, statut, quantité
- Indicateurs visuels

##### `button.css`
**Rôle :** Styles des boutons
- Boutons primaires, secondaires, outline
- États hover, active, disabled
- Tailles et variantes

##### `card.css`
**Rôle :** Styles des cartes produits
- Mise en page des cartes
- Images, titres, descriptions, prix
- Effets hover et transitions

##### `footer.css`
**Rôle :** Styles du pied de page
- Grille de colonnes
- Liens et informations de contact
- Réseaux sociaux

##### `form.css`
**Rôle :** Styles des formulaires
- Champs de saisie, labels, erreurs
- Boutons de soumission
- Validation visuelle

##### `header.css`
**Rôle :** Styles de l'en-tête et navigation
- Logo et navigation desktop/mobile
- Menu hamburger
- États actifs des liens

##### `hero.css`
**Rôle :** Styles de la section hero (bannière principale)
- Image de fond avec overlay
- Titre et texte centré
- Call-to-action

##### `table.css`
**Rôle :** Styles des tableaux
- Tableaux de données (dashboard)
- Lignes alternées, en-têtes
- Responsive tables

##### `tabs.css`
**Rôle :** Styles des onglets
- Navigation par onglets (dashboard)
- États actifs/inactifs
- Transitions

#### `pages/` - Styles de Pages

##### `dashboard.css`
**Rôle :** Styles spécifiques au tableau de bord artisan
- Statistiques et graphiques
- Tableaux de gestion
- Layout spécifique

---

### 📁 Dossier `js/`

#### `app.js`
**Rôle :** Point d'entrée principal de l'application JavaScript
- Initialisation de l'application au chargement
- Gestion de l'état global (currentPage, userRole, etc.)
- Coordination entre les différents modules
- Fonction `loadPage()` qui charge le contenu des pages

#### `navigation.js`
**Rôle :** Gestion de la navigation SPA (Single Page Application)
- Fonction `navigate()` pour changer de page sans rechargement
- Mise à jour de l'URL avec hash (#)
- Gestion des liens actifs
- Navigation par historique du navigateur

#### `data/` - Gestion des Données

##### `products.js`
**Rôle :** Gestion des données produits
- Tableau des produits avec leurs propriétés
- Fonctions pour récupérer, filtrer, rechercher des produits
- Gestion des catégories

##### `orders.js`
**Rôle :** Gestion des données commandes
- Tableau des commandes
- Fonctions pour créer, récupérer, mettre à jour des commandes
- Gestion des statuts (en attente, en cours, livrée)

##### `helpers.js`
**Rôle :** Fonctions utilitaires pour les données
- Fonctions de formatage (prix en XOF)
- Fonctions de tri et filtrage
- Utilitaires pour manipuler les données

#### `utils/` - Fonctions Utilitaires

##### `helpers.js`
**Rôle :** Fonctions utilitaires générales
- Fonction `setCategory()` pour filtrer par catégorie
- Fonction `setViewMode()` pour changer la vue (grille/liste)
- Autres fonctions utilitaires partagées

##### `user.js`
**Rôle :** Gestion des utilisateurs
- Authentification (login/logout)
- Gestion des rôles (visiteur, client, artisan)
- Stockage de l'état utilisateur
- Mise à jour de la navigation selon le rôle

##### `mobile.js`
**Rôle :** Fonctions pour la gestion mobile
- Toggle du menu mobile
- Gestion des interactions tactiles
- Adaptation mobile

#### `components/` - Composants JavaScript

##### `productCard.js`
**Rôle :** Composant carte produit réutilisable
- Fonction pour générer le HTML d'une carte produit
- Affichage des informations produit
- Gestion des interactions (clic, hover)

#### `pages/` - Logique des Pages

##### `home.js`
**Rôle :** Logique de la page d'accueil
- Fonction `renderHomePage()` qui génère le HTML
- Section hero, produits en vedette, catégories
- Témoignages et call-to-action

##### `gallery.js`
**Rôle :** Logique de la page galerie
- Affichage de tous les produits
- Filtres par catégorie
- Vue grille/liste
- Compteur de produits

##### `product.js`
**Rôle :** Logique de la page détails produit
- Affichage détaillé d'un produit
- Images, description, prix
- Bouton de commande
- Produits similaires

##### `about.js`
**Rôle :** Logique de la page à propos
- Histoire de la galerie
- Valeurs et mission
- Équipe et artisans

##### `contact.js`
**Rôle :** Logique de la page contact
- Formulaire de contact
- Informations de contact
- Intégration WhatsApp
- Carte (si applicable)

##### `order.js`
**Rôle :** Logique de la page formulaire de commande
- Formulaire de commande
- Sélection du produit et quantité
- Informations client
- Validation et soumission

##### `tracking.js`
**Rôle :** Logique de la page suivi de commande
- Liste des commandes du client
- Statut de chaque commande
- Détails de la commande
- Historique

##### `profile.js`
**Rôle :** Logique de la page profil utilisateur
- Informations du profil
- Modification des données
- Historique des commandes
- Paramètres

##### `login.js`
**Rôle :** Logique de la page de connexion
- Formulaire de connexion
- Authentification client/artisan
- Redirection selon le rôle
- Gestion des erreurs

##### `register.js`
**Rôle :** Logique de la page d'inscription
- Formulaire d'inscription
- Validation des données
- Création de compte
- Redirection après inscription

##### `dashboard.js`
**Rôle :** Logique de la page tableau de bord artisan
- Vue d'ensemble avec statistiques
- Gestion des produits (liste, ajout, modification, suppression)
- Gestion des commandes
- Profil artisan
- Navigation par onglets

---

## 🏗️ Architecture du Projet

### Organisation Modulaire

Le projet suit une **architecture modulaire** claire :

1. **Séparation des responsabilités** : CSS, JS, données sont séparés
2. **Composants réutilisables** : Cartes, boutons, formulaires
3. **Pages modulaires** : Chaque page a son propre fichier JS
4. **Utilitaires centralisés** : Fonctions partagées dans `utils/`
5. **Données centralisées** : Toutes les données dans `data/`

### Flux de Données

```
index.html
    ↓
app.js (initialisation)
    ↓
navigation.js (routage)
    ↓
pages/*.js (rendu)
    ↓
data/*.js (données)
    ↓
components/*.js (composants)
```

### Responsive Design

- **Mobile-first** : Design adapté mobile, tablette, desktop
- **Navigation adaptative** : Menu hamburger sur mobile
- **Grilles flexibles** : CSS Grid et Flexbox
- **Images responsives** : Adaptation automatique

---

## 🎯 Points Clés

- **SPA (Single Page Application)** : Navigation sans rechargement de page
- **Vanilla JavaScript** : Pas de framework, JavaScript pur
- **CSS Modulaire** : Organisation par composants et pages
- **Architecture claire** : Facile à maintenir et étendre
- **Responsive** : Fonctionne sur tous les appareils

---

**Dernière mise à jour :** 2025


