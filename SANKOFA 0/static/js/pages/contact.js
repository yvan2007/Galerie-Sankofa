// ============================================
// CONTACT PAGE
// ============================================

function renderContactPage() {
    return `
        <div class="container" style="padding: 3rem 0;">
            <div class="text-center mb-4">
                <h1 class="section-title">Contactez-nous</h1>
                <p class="section-subtitle">
                    Une question ? Un projet spécial ? N'hésitez pas à nous contacter
                </p>
            </div>

            <div class="grid grid-2" style="gap: 3rem;">
                <div class="card">
                    <div class="card-content">
                        <h2 style="font-size: 1.5rem; color: var(--color-text); margin-bottom: 1.5rem;">Envoyez-nous un message</h2>
                        <form id="contactForm" onsubmit="handleContactSubmit(event)">
                            <div class="form-group">
                                <label class="form-label">Nom complet *</label>
                                <input type="text" class="form-input" name="name" required placeholder="Votre nom">
                            </div>
                            <div class="form-group">
                                <label class="form-label">Email *</label>
                                <input type="email" class="form-input" name="email" required placeholder="votre@email.com">
                            </div>
                            <div class="form-group">
                                <label class="form-label">Message *</label>
                                <textarea class="form-textarea" name="message" required rows="6" placeholder="Écrivez votre message ici..."></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">
                                <i class="fas fa-paper-plane"></i> Envoyer le message
                            </button>
                        </form>
                    </div>
                </div>

                <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                    <div class="card" style="background-color: var(--color-bg-light);">
                        <div class="card-content">
                            <div style="display: flex; gap: 1rem; align-items: start;">
                                <div style="width: 3rem; height: 3rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                                    <i class="fas fa-phone" style="font-size: 1.5rem; color: var(--color-primary);"></i>
                                </div>
                                <div>
                                    <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Téléphone</h3>
                                    <a href="tel:+22507000000" style="color: var(--color-text-light); text-decoration: none; transition: var(--transition);">
                                        +225 07 00 00 00 00
                                    </a>
                                    <p style="font-size: 0.875rem; color: var(--color-text-light); margin-top: 0.25rem;">Lun-Sam: 8h-18h</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="card" style="background-color: var(--color-bg-light);">
                        <div class="card-content">
                            <div style="display: flex; gap: 1rem; align-items: start;">
                                <div style="width: 3rem; height: 3rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                                    <i class="fab fa-whatsapp" style="font-size: 1.5rem; color: var(--color-primary);"></i>
                                </div>
                                <div>
                                    <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">WhatsApp</h3>
                                    <a href="https://wa.me/22507000000" target="_blank" style="color: var(--color-text-light); text-decoration: none; transition: var(--transition);">
                                        +225 07 00 00 00 00
                                    </a>
                                    <p style="font-size: 0.875rem; color: var(--color-text-light); margin-top: 0.25rem;">Réponse rapide garantie</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="card" style="background-color: var(--color-bg-light);">
                        <div class="card-content">
                            <div style="display: flex; gap: 1rem; align-items: start;">
                                <div style="width: 3rem; height: 3rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                                    <i class="fas fa-envelope" style="font-size: 1.5rem; color: var(--color-primary);"></i>
                                </div>
                                <div>
                                    <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Email</h3>
                                    <a href="mailto:contact@galeriesankofa.ci" style="color: var(--color-text-light); text-decoration: none; transition: var(--transition);">
                                        contact@galeriesankofa.ci
                                    </a>
                                    <p style="font-size: 0.875rem; color: var(--color-text-light); margin-top: 0.25rem;">Réponse sous 24h</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="card" style="background-color: var(--color-bg-light);">
                        <div class="card-content">
                            <div style="display: flex; gap: 1rem; align-items: start;">
                                <div style="width: 3rem; height: 3rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                                    <i class="fas fa-map-marker-alt" style="font-size: 1.5rem; color: var(--color-primary);"></i>
                                </div>
                                <div>
                                    <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Adresse</h3>
                                    <p style="color: var(--color-text-light);">
                                        GRAND-BASSAM<br>
                                        Côte d'Ivoire
                                    </p>
                                    <p style="font-size: 0.875rem; color: var(--color-text-light); margin-top: 0.25rem;">Visite sur rendez-vous</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function handleContactSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    // Simulate form submission
    alert('Message envoyé ! Nous vous répondrons dans les plus brefs délais.');
    form.reset();
}

