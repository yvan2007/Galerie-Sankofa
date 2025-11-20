// ============================================
// PRODUCT CARD COMPONENTS
// ============================================

// Render Product Card
function renderProductCard(product) {
    return `
        <div class="product-card">
            <div class="product-image-wrapper">
                <img src="${product.image}" alt="${product.name}" class="product-image" 
                     onclick="navigate('product', '${product.id}')">
                <div class="product-badge">
                    <span class="badge badge-primary">${product.category}</span>
                </div>
                ${!product.availability ? `
                    <div class="product-unavailable">
                        <span class="badge badge-danger">Épuisé</span>
                    </div>
                ` : ''}
            </div>
            <div class="product-info">
                <h3 class="product-name" onclick="navigate('product', '${product.id}')">${product.name}</h3>
                <p class="product-description">${product.description}</p>
                <p class="product-price">${formatPrice(product.price)}</p>
                <div class="product-actions">
                    <button class="btn btn-primary" onclick="navigate('product', '${product.id}')">
                        Voir détails
                    </button>
                    <button class="btn btn-green" onclick="openWhatsApp('${product.name}', 1, ${product.price})">
                        <i class="fab fa-whatsapp"></i> WhatsApp
                    </button>
                </div>
            </div>
        </div>
    `;
}

function renderProductListCard(product) {
    return `
        <div class="card" style="display: flex; flex-direction: column; md:flex-row;">
            <div style="display: grid; grid-template-columns: 1fr 3fr; gap: 1rem;">
                <img src="${product.image}" alt="${product.name}" 
                     style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: var(--radius-lg) 0 0 var(--radius-lg);">
                <div style="padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                            <h3 style="font-size: 1.25rem; color: var(--color-text);">${product.name}</h3>
                            <span style="font-size: 1.125rem; color: var(--color-primary);">${formatPrice(product.price)}</span>
                        </div>
                        <p style="font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.75rem;">
                            ${product.description}
                        </p>
                        <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                            <span class="badge badge-primary">${product.category}</span>
                            ${product.availability 
                                ? '<span class="badge badge-success">Disponible</span>'
                                : '<span class="badge badge-danger">Rupture de stock</span>'
                            }
                        </div>
                    </div>
                    <div style="display: flex; gap: 0.75rem;">
                        <button class="btn btn-primary" onclick="navigate('product', '${product.id}')" style="flex: 1;">
                            Voir détails
                        </button>
                        <button class="btn btn-green" onclick="openWhatsApp('${product.name}', 1, ${product.price})">
                            <i class="fab fa-whatsapp"></i> WhatsApp
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

