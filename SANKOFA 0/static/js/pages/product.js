// ============================================
// PRODUCT DETAILS PAGE
// ============================================

function renderProductPage(productId) {
    const product = getProductById(productId);
    
    if (!product) {
        return `
            <div class="container" style="padding: 4rem 0; text-align: center;">
                <p style="color: var(--color-text-light); margin-bottom: 1rem;">Produit non trouvé</p>
                <button class="btn btn-primary" onclick="navigate('home')">Retour à l'accueil</button>
            </div>
        `;
    }
    
    const relatedProducts = getRelatedProducts(productId, 3);
    let quantity = 1;
    
    return `
        <div class="container" style="padding: 2rem 0;">
            <button class="btn btn-outline mb-4" onclick="navigate('home')">
                <i class="fas fa-arrow-left"></i> Retour
            </button>
            
            <div class="grid grid-2" style="gap: 3rem; margin-bottom: 4rem;">
                <div style="aspect-ratio: 1; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg);">
                    <img src="${product.image}" alt="${product.name}" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                
                <div>
                    <span class="badge badge-warning mb-2">${product.category}</span>
                    <h1 style="font-size: 2.5rem; color: var(--color-text); margin-bottom: 1rem;">${product.name}</h1>
                    <p style="font-size: 1.5rem; color: var(--color-primary); margin-bottom: 1.5rem;">${formatPrice(product.price)}</p>
                    
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">
                        ${product.availability 
                            ? '<i class="fas fa-check-circle" style="color: #10b981;"></i><span style="color: #065f46;">En stock</span>'
                            : '<i class="fas fa-times-circle" style="color: #ef4444;"></i><span style="color: #991b1b;">Épuisé</span>'
                        }
                    </div>
                    
                    <div style="margin-bottom: 2rem;">
                        <h2 style="font-size: 1.25rem; color: var(--color-text); margin-bottom: 0.75rem;">Description</h2>
                        <p style="color: var(--color-text-light); margin-bottom: 0.75rem;">${product.description}</p>
                        <p style="color: var(--color-text-light);">${product.details}</p>
                    </div>
                    
                    ${product.availability ? `
                        <div style="margin-bottom: 1.5rem;">
                            <label style="display: block; color: var(--color-text); margin-bottom: 0.5rem; font-weight: 500;">Quantité</label>
                            <div style="display: flex; align-items: center; gap: 0.75rem;">
                                <button class="btn btn-outline" onclick="this.parentElement.querySelector('span').textContent = Math.max(1, parseInt(this.parentElement.querySelector('span').textContent) - 1)" style="padding: 0.5rem 1rem;">-</button>
                                <span style="width: 3rem; text-align: center; font-weight: 500;">1</span>
                                <button class="btn btn-outline" onclick="this.parentElement.querySelector('span').textContent = parseInt(this.parentElement.querySelector('span').textContent) + 1" style="padding: 0.5rem 1rem;">+</button>
                            </div>
                        </div>
                        
                        <div style="margin-bottom: 1.5rem; padding: 1rem; background-color: #f9fafb; border-radius: var(--radius);">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="color: var(--color-text-light);">Total</span>
                                <span style="font-size: 1.25rem; color: var(--color-primary); font-weight: 600;">${formatPrice(product.price)}</span>
                            </div>
                        </div>
                    ` : ''}
                    
                    <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                        ${product.availability ? `
                            <button class="btn btn-primary btn-lg" onclick="navigate('order', '${product.id}')">
                                <i class="fas fa-shopping-cart"></i> Commander
                            </button>
                            <button class="btn btn-green btn-lg" onclick="openWhatsApp('${product.name}', 1, ${product.price})">
                                <i class="fab fa-whatsapp"></i> Contacter l'artisan
                            </button>
                        ` : `
                            <button class="btn btn-green btn-lg" onclick="openWhatsApp('${product.name}', 1, ${product.price})">
                                <i class="fab fa-whatsapp"></i> Me notifier quand disponible
                            </button>
                        `}
                    </div>
                </div>
            </div>
            
            ${relatedProducts.length > 0 ? `
                <section>
                    <h2 style="font-size: 1.5rem; color: var(--color-text); margin-bottom: 1.5rem;">Produits similaires</h2>
                    <div class="grid grid-3">
                        ${relatedProducts.map(p => renderProductCard(p)).join('')}
                    </div>
                </section>
            ` : ''}
        </div>
    `;
}

