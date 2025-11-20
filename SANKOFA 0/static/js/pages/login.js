// ============================================
// LOGIN PAGE
// ============================================

function renderLoginPage(userType = 'client') {
    // userType can be 'client' or 'artisan'
    const isClient = userType === 'client';
    
    return `
        <div style="min-height: calc(100vh - 200px); display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, var(--color-bg-light), #f3f4f6); padding: 2rem;">
            <div style="width: 100%; max-width: 28rem;">
                <div class="text-center mb-4">
                    <div style="width: 5rem; height: 5rem; background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark)); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; box-shadow: var(--shadow-lg);">
                        <span style="color: white; font-size: 2rem; font-weight: 600;">S</span>
                    </div>
                    <h1 style="font-size: 2rem; color: var(--color-text); margin-bottom: 0.5rem;">Galerie Sankofa</h1>
                    <p style="color: var(--color-text-light);">${isClient ? 'Espace Client' : 'Espace Artisan'}</p>
                </div>

                <div class="card" style="box-shadow: var(--shadow-lg);">
                    <div class="card-content">
                        <h2 style="font-size: 1.5rem; color: var(--color-text); margin-bottom: 0.5rem; text-align: center;">Connexion</h2>
                        <p style="text-align: center; color: var(--color-text-light); font-size: 0.875rem; margin-bottom: 2rem;">
                            ${isClient ? 'Accédez à votre espace client' : 'Accédez à votre tableau de bord'}
                        </p>
                        
                        <form id="loginForm" onsubmit="handleLoginSubmit(event, '${userType}')">
                            <input type="hidden" name="userType" value="${userType}">
                            <div class="form-group">
                                <label class="form-label">Email</label>
                                <div style="position: relative;">
                                    <i class="fas fa-envelope" style="position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--color-text-light);"></i>
                                    <input type="email" class="form-input" name="email" required 
                                           placeholder="votre@email.com" style="padding-left: 2.5rem;">
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Mot de passe</label>
                                <div style="position: relative;">
                                    <i class="fas fa-lock" style="position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--color-text-light);"></i>
                                    <input type="password" class="form-input" name="password" required 
                                           placeholder="••••••••" style="padding-left: 2.5rem;">
                                </div>
                            </div>
                            
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; font-size: 0.875rem;">
                                <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer;">
                                    <input type="checkbox" name="remember" style="cursor: pointer;">
                                    <span style="color: var(--color-text-light);">Se souvenir de moi</span>
                                </label>
                                <a href="#" style="color: var(--color-primary); text-decoration: none;">Mot de passe oublié ?</a>
                            </div>
                            
                            <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">
                                Se connecter
                            </button>
                        </form>
                        
                        <div style="margin-top: 1.5rem; padding: 1rem; background-color: rgba(203, 161, 53, 0.1); border-radius: var(--radius);">
                            <p style="font-size: 0.875rem; color: var(--color-text); text-align: center;">
                                <strong>Demo:</strong> Entrez n'importe quelle adresse email et mot de passe
                            </p>
                        </div>
                        
                        ${isClient ? `
                            <div style="margin-top: 1rem; text-align: center;">
                                <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                    Pas encore de compte ? 
                                    <a href="#" onclick="navigate('register'); return false;" style="color: var(--color-primary); text-decoration: none; font-weight: 500;">
                                        Créer un compte
                                    </a>
                                </p>
                            </div>
                        ` : ''}
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

function renderLoginPageWithType(userType) {
    currentPage = 'login';
    const mainContent = document.getElementById('mainContent');
    if (mainContent) {
        mainContent.innerHTML = renderLoginPage(userType);
    }
    // Update URL if needed
    if (window.location.hash !== '#login') {
        window.location.hash = 'login';
    }
}

// Helper function to navigate to login with a specific user type
function navigateToLogin(userType) {
    // Store the user type before navigation
    window.loginUserType = userType;
    // Navigate to login page
    navigate('login');
}

function handleLoginSubmit(event, userType = 'client') {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const type = formData.get('userType') || userType;
    
    login(type);
}

