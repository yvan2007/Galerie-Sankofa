# 🧪 Guide de Test Web - Galerie Sankofa

## Serveur Django
✅ Serveur démarré sur : **http://127.0.0.1:8000**

---

## TEST 1 : INSCRIPTION CLIENT → Email de Bienvenue

### Étapes :
1. Ouvrez votre navigateur
2. Allez sur : **http://127.0.0.1:8000/inscription/**
3. Remplissez le formulaire :
   - Nom d'utilisateur : `test_client_web`
   - Email : `kouayavana20@gmail.com` (ou un autre email)
   - Mot de passe : `test123456`
   - Téléphone : `+225 07 00 00 00 00`
   - Type : **Client**
4. Cliquez sur "Créer un compte"
5. ✅ **Résultat attendu** :
   - Redirection vers la page d'accueil
   - Message de succès : "Compte créé avec succès ! Un email de bienvenue vous a été envoyé."
   - **Vérifiez votre boîte email** → Vous devriez recevoir un email de bienvenue HTML

---

## TEST 2 : MOT DE PASSE OUBLIÉ → Email de Réinitialisation

### Étapes :
1. Allez sur : **http://127.0.0.1:8000/connexion/**
2. Cliquez sur **"Mot de passe oublié ?"** (lien en bas du formulaire)
3. Entrez votre email : `kouayavana20@gmail.com`
4. Cliquez sur **"Envoyer le lien de réinitialisation"**
5. ✅ **Résultat attendu** :
   - Message : "Un email de réinitialisation vous a été envoyé."
   - **Vérifiez votre boîte email** → Email avec lien de réinitialisation
   - Cliquez sur le lien dans l'email
   - Entrez un nouveau mot de passe
   - Confirmez le nouveau mot de passe
   - Message : "Votre mot de passe a été réinitialisé avec succès."

---

## TEST 3 : CONNEXION ARTISAN → Code de Vérification (2FA)

### Prérequis :
- Un compte artisan doit exister (créé précédemment ou via le test)

### Étapes :
1. Allez sur : **http://127.0.0.1:8000/connexion/?type=artisan**
2. Entrez les identifiants artisan :
   - Email : Email de l'artisan
   - Mot de passe : Mot de passe de l'artisan
3. Cliquez sur **"Se connecter"**
4. ✅ **Résultat attendu** :
   - Redirection vers la page de vérification : **http://127.0.0.1:8000/verification-artisan/**
   - Message : "Un code de vérification vous a été envoyé par email."
   - **Vérifiez votre boîte email** → Email avec code à 6 chiffres
5. Entrez le code reçu (exemple : `808821`)
6. Cliquez sur **"Vérifier"**
7. ✅ **Résultat attendu** :
   - Redirection vers le dashboard : **http://127.0.0.1:8000/dashboard/**
   - Message : "Code vérifié avec succès !"

---

## TEST 4 : CRÉATION ARTISAN (Un seul compte possible)

### Étapes :
1. Allez sur : **http://127.0.0.1:8000/inscription/**
2. Remplissez le formulaire avec :
   - Type : **Artisan**
   - Email : `artisan@test.com`
3. Cliquez sur "Créer un compte"

### Scénario A : Premier artisan
- ✅ Si aucun artisan n'existe → Compte créé avec succès
- Email de bienvenue envoyé
- Redirection vers page de vérification

### Scénario B : Artisan existe déjà
- ❌ Message d'erreur : "Un compte artisan existe déjà. Vous ne pouvez pas en créer un nouveau."
- Redirection vers la page d'inscription

---

## TEST 5 : CONNEXION CLIENT NORMAL

### Étapes :
1. Allez sur : **http://127.0.0.1:8000/connexion/**
2. Entrez les identifiants d'un compte client
3. Cliquez sur "Se connecter"
4. ✅ **Résultat attendu** :
   - Connexion réussie
   - Redirection vers la page d'accueil
   - Pas de code de vérification (seulement pour artisan)

---

## TEST 6 : GOOGLE OAUTH (Si configuré)

### Étapes :
1. Allez sur : **http://127.0.0.1:8000/connexion/**
2. Cliquez sur le bouton **"Continuer avec Google"**
3. ✅ **Résultat attendu** :
   - Redirection vers Google pour authentification
   - Après authentification → Retour sur le site
   - Connexion automatique

**Note** : Nécessite la configuration des credentials Google OAuth dans `settings.py`

---

## 📊 Checklist de Vérification

- [ ] Email de bienvenue reçu après inscription
- [ ] Email de réinitialisation reçu avec lien fonctionnel
- [ ] Code de vérification artisan reçu par email
- [ ] Code de vérification fonctionne pour accéder au dashboard
- [ ] Impossible de créer un deuxième compte artisan
- [ ] Messages Django disparaissent automatiquement après quelques secondes
- [ ] Bouton "Annuler" fonctionne dans les modaux

---

## 🐛 En cas de problème

1. **Email non reçu** :
   - Vérifiez le dossier SPAM
   - Vérifiez que SMTP est bien configuré dans `settings.py`
   - Vérifiez les logs du serveur Django

2. **Erreur de connexion** :
   - Vérifiez que le serveur est démarré
   - Vérifiez les identifiants utilisateur

3. **Code de vérification invalide** :
   - Le code expire après 10 minutes
   - Demandez un nouveau code

---

**Bon test ! 🚀**

