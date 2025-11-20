// ============================================
// REGISTER PAGE (Client Account Creation)
// ============================================

function renderRegisterPage() {
    return `
        <div style="min-height: calc(100vh - 200px); display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, var(--color-bg-light), #f3f4f6); padding: 2rem;">
            <div style="width: 100%; max-width: 32rem;">
                <div class="text-center mb-4">
                    <div style="width: 5rem; height: 5rem; background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark)); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; box-shadow: var(--shadow-lg);">
                        <span style="color: white; font-size: 2rem; font-weight: 600;">S</span>
                    </div>
                    <h1 style="font-size: 2rem; color: var(--color-text); margin-bottom: 0.5rem;">Galerie Sankofa</h1>
                    <p style="color: var(--color-text-light);">Créer un compte client</p>
                </div>

                <div class="card" style="box-shadow: var(--shadow-lg);">
                    <div class="card-content">
                        <h2 style="font-size: 1.5rem; color: var(--color-text); margin-bottom: 0.5rem; text-align: center;">Inscription</h2>
                        <p style="text-align: center; color: var(--color-text-light); font-size: 0.875rem; margin-bottom: 2rem;">
                            Créez votre compte pour suivre vos commandes et gérer votre profil
                        </p>
                        
                        <form id="registerForm" onsubmit="handleRegisterSubmit(event)">
                            <div class="form-group">
                                <label class="form-label">Nom complet *</label>
                                <div style="position: relative;">
                                    <i class="fas fa-user" style="position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--color-text-light);"></i>
                                    <input type="text" class="form-input" name="fullName" required 
                                           placeholder="Votre nom complet" style="padding-left: 2.5rem;">
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Email *</label>
                                <div style="position: relative;">
                                    <i class="fas fa-envelope" style="position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--color-text-light);"></i>
                                    <input type="email" class="form-input" name="email" required 
                                           placeholder="votre@email.com" style="padding-left: 2.5rem;">
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Téléphone *</label>
                                <div style="position: relative;">
                                    <i class="fas fa-phone" style="position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--color-text-light);"></i>
                                    <input type="tel" class="form-input" name="phone" required 
                                           placeholder="+225 07 00 00 00 00" style="padding-left: 2.5rem;">
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Adresse *</label>
                                <div style="position: relative;">
                                    <i class="fas fa-map-marker-alt" style="position: absolute; left: 1rem; top: 1.5rem; transform: translateY(-50%); color: var(--color-text-light);"></i>
                                    <textarea class="form-textarea" name="address" required rows="3" 
                                              placeholder="Ville, quartier, détails d'adresse..." style="padding-left: 2.5rem;"></textarea>
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Mot de passe *</label>
                                <div style="position: relative;">
                                    <i class="fas fa-lock" style="position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--color-text-light);"></i>
                                    <input type="password" class="form-input" name="password" required 
                                           placeholder="••••••••" minlength="6" style="padding-left: 2.5rem;">
                                </div>
                                <p style="font-size: 0.75rem; color: var(--color-text-light); margin-top: 0.25rem;">
                                    Minimum 6 caractères
                                </p>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Confirmer le mot de passe *</label>
                                <div style="position: relative;">
                                    <i class="fas fa-lock" style="position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--color-text-light);"></i>
                                    <input type="password" class="form-input" name="confirmPassword" required 
                                           placeholder="••••••••" minlength="6" style="padding-left: 2.5rem;">
                                </div>
                            </div>
                            
                            <div style="margin-bottom: 1.5rem;">
                                <label style="display: flex; align-items: start; gap: 0.5rem; cursor: pointer; font-size: 0.875rem;">
                                    <input type="checkbox" name="terms" required style="margin-top: 0.25rem; cursor: pointer;">
                                    <span style="color: var(--color-text-light);">
                                        J'accepte les <a href="#" style="color: var(--color-primary); text-decoration: none;">conditions d'utilisation</a> 
                                        et la <a href="#" style="color: var(--color-primary); text-decoration: none;">politique de confidentialité</a>
                                    </span>
                                </label>
                            </div>
                            
                            <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">
                                <i class="fas fa-user-plus"></i> Créer mon compte
                            </button>
                        </form>
                        
                        <div style="margin-top: 1.5rem; padding: 1rem; background-color: rgba(203, 161, 53, 0.1); border-radius: var(--radius);">
                            <p style="font-size: 0.875rem; color: var(--color-text); text-align: center;">
                                <strong>Demo:</strong> Remplissez le formulaire et créez votre compte
                            </p>
                        </div>
                        
                        <div style="margin-top: 1.5rem; text-align: center; padding-top: 1.5rem; border-top: 1px solid var(--color-border);">
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Vous avez déjà un compte ? 
                                <a href="#" onclick="navigateToLogin('client'); navigate('login'); return false;" style="color: var(--color-primary); text-decoration: none; font-weight: 500;">
                                    Se connecter
                                </a>
                            </p>
                        </div>
                    </div>
                </div>

                <div class="text-center mt-4">
                    <a href="#" onclick="navigate('home'); return false;" style="color: var(--color-text-light); text-decoration: none; font-size: 0.875rem;">
                        ← Retour au site
                    </a>
                </div>
            </div>
        </div>
    `;
}

function handleRegisterSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    const password = formData.get('password');
    const confirmPassword = formData.get('confirmPassword');
    
    // Validate passwords match
    if (password !== confirmPassword) {
        alert('Les mots de passe ne correspondent pas. Veuillez réessayer.');
        return;
    }
    
    // Validate password length
    if (password.length < 6) {
        alert('Le mot de passe doit contenir au moins 6 caractères.');
        return;
    }
    
    // Simulate account creation
    const fullName = formData.get('fullName');
    const email = formData.get('email');
    
    // Simulate successful registration
    alert(`Compte créé avec succès !\n\nBienvenue ${fullName} !\nVotre compte a été créé avec l'email: ${email}\n\nVous allez être connecté automatiquement.`);
    
    // Auto-login after registration
    login('client');
    
    // Reset form
    form.reset();
}

