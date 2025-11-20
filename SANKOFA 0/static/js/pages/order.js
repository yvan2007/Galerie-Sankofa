// ============================================
// ORDER PAGE
// ============================================

function renderOrderPage(productId) {
    const product = productId ? getProductById(productId) : null;
    
    return `
        <div class="container" style="padding: 2rem 0;">
            <button class="btn btn-outline mb-4" onclick="navigate('home')">
                <i class="fas fa-arrow-left"></i> Retour
            </button>

            <div class="card" style="max-width: 42rem; margin: 0 auto;">
                <div class="card-content">
                    <h1 style="font-size: 2rem; color: var(--color-text); margin-bottom: 0.5rem;">Passer une commande</h1>
                    <p style="color: var(--color-text-light); margin-bottom: 2rem;">
                        Remplissez le formulaire ci-dessous et nous vous contacterons pour finaliser votre commande.
                    </p>
                    
                    <form id="orderForm" onsubmit="handleOrderSubmit(event)">
                        <div class="form-group">
                            <label class="form-label">Nom complet *</label>
                            <input type="text" class="form-input" name="name" required placeholder="Votre nom">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Téléphone *</label>
                            <input type="tel" class="form-input" name="phone" required placeholder="+225 07 00 00 00 00">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Produit *</label>
                            <input type="text" class="form-input" name="product" required 
                                   value="${product ? product.name : ''}" placeholder="Nom du produit">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Quantité *</label>
                            <input type="number" class="form-input" name="quantity" required min="1" value="1">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Adresse de livraison *</label>
                            <textarea class="form-textarea" name="address" required rows="3" placeholder="Ville, quartier, détails d'adresse..."></textarea>
                        </div>
                        
                        <div class="alert alert-info" style="margin-bottom: 1.5rem;">
                            <p style="font-size: 0.875rem;">
                                <strong>Note :</strong> Un membre de notre équipe vous contactera dans les 24h pour 
                                confirmer votre commande et organiser la livraison.
                            </p>
                        </div>
                        
                        <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">
                            <i class="fas fa-shopping-cart"></i> Confirmer la commande
                        </button>
                    </form>
                </div>
            </div>
        </div>
    `;
}

function handleOrderSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    // Set user as client after order
    setClientRole();
    
    // Simulate order submission
    alert('Commande reçue ! Merci pour votre commande. Nous vous contacterons très bientôt.');
    
    // Redirect to tracking page
    setTimeout(() => {
        navigate('tracking');
    }, 1000);
}

