# Configuration Google OAuth - Galerie Sankofa

## ✅ Bouton Google OAuth Stylisé

Le bouton "Continuer avec Google" a été amélioré avec :
- ✨ Design moderne avec dégradé bleu Google
- 🎨 Icône Google officielle (SVG)
- 💫 Effets hover et animations
- 📱 Responsive et accessible

---

## Configuration Google OAuth

Pour que le bouton fonctionne complètement, vous devez configurer les credentials Google OAuth.

### Étapes :

1. **Aller sur Google Cloud Console** :
   - https://console.cloud.google.com/

2. **Créer un projet** (ou utiliser un existant)

3. **Activer l'API Google+** :
   - APIs & Services → Library
   - Rechercher "Google+ API"
   - Cliquer sur "Enable"

4. **Créer des identifiants OAuth 2.0** :
   - APIs & Services → Credentials
   - Cliquer sur "Create Credentials" → "OAuth client ID"
   - Type d'application : **Web application**
   - Nom : `Galerie Sankofa`
   
5. **Configurer les URI autorisés** :
   - **Origines JavaScript autorisées** :
     - `http://127.0.0.1:8000`
     - `http://localhost:8000`
   - **URI de redirection autorisés** :
     - `http://127.0.0.1:8000/accounts/google/login/callback/`
     - `http://localhost:8000/accounts/google/login/callback/`

6. **Copier les identifiants** :
   - **Client ID** : Copiez cette valeur
   - **Client Secret** : Copiez cette valeur

   YOUR-GOOGLE-CLIENT-ID.apps.googleusercontent.com

   YOUR-GOOGLE-CLIENT-SECRET

7. **Configurer dans `settings.py`** (lignes 182-183) :
   ```python
   'APP': {
       'client_id': 'VOTRE_CLIENT_ID_ICI',
       'secret': 'VOTRE_CLIENT_SECRET_ICI',
       'key': ''
   }
   ```

---

## Test

1. Allez sur : http://127.0.0.1:8000/connexion/
2. Cliquez sur le bouton **"Continuer avec Google"**
3. Vous serez redirigé vers Google pour vous connecter
4. Après connexion, vous serez redirigé vers le site

---

## Notes

- Le bouton est maintenant stylisé et moderne
- L'icône Google est intégrée (SVG)
- Les effets hover sont actifs
- Le site Django est configuré pour `127.0.0.1:8000`

**⚠️ Important** : Sans les credentials Google OAuth, le bouton redirigera vers Google mais l'authentification échouera. Configurez les credentials pour un fonctionnement complet.

