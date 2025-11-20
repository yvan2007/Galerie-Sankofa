// ============================================
// PROFILE PAGE
// ============================================

function renderProfilePage() {
    return `
        <div class="container" style="padding: 3rem 0;">
            <h1 class="section-title">Mon Profil</h1>
            
            <div class="card" style="max-width: 42rem; margin: 2rem auto 0;">
                <div class="card-content">
                    <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                        <div>
                            <label style="display: block; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.5rem;">Nom complet</label>
                            <p style="color: var(--color-text); font-weight: 500;">Client Sankofa</p>
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.5rem;">Email</label>
                            <p style="color: var(--color-text); font-weight: 500;">client@example.com</p>
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.5rem;">Téléphone</label>
                            <p style="color: var(--color-text); font-weight: 500;">+225 07 00 00 00 00</p>
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.5rem;">Adresse</label>
                            <p style="color: var(--color-text); font-weight: 500;">Abidjan, Côte d'Ivoire</p>
                        </div>
                        <div style="padding-top: 1rem; border-top: 1px solid var(--color-border);">
                            <button class="btn btn-primary">
                                <i class="fas fa-edit"></i> Modifier le profil
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

