// ============================================
// TRACKING PAGE
// ============================================

function renderTrackingPage() {
    const userOrders = orders; // In real app, filter by user
    
    return `
        <div class="container" style="padding: 3rem 0;">
            <h1 class="section-title">Suivi de mes commandes</h1>
            
            ${userOrders.length > 0 ? `
                <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 2rem;">
                    ${userOrders.map(order => `
                        <div class="card">
                            <div class="card-content">
                                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                                    <div>
                                        <h3 style="font-size: 1.25rem; color: var(--color-text); margin-bottom: 0.25rem;">Commande ${order.id}</h3>
                                        <p style="color: var(--color-text-light); font-size: 0.875rem;">
                                            ${new Date(order.date).toLocaleDateString('fr-FR')}
                                        </p>
                                    </div>
                                    ${getStatusBadge(order.status)}
                                </div>
                                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
                                    <div>
                                        <p style="font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.25rem;">Produit</p>
                                        <p style="font-weight: 500;">${order.product}</p>
                                    </div>
                                    <div>
                                        <p style="font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.25rem;">Quantité</p>
                                        <p style="font-weight: 500;">${order.quantity}</p>
                                    </div>
                                    <div>
                                        <p style="font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.25rem;">Total</p>
                                        <p style="font-weight: 500; color: var(--color-primary);">${formatPrice(order.total)}</p>
                                    </div>
                                </div>
                                <div style="padding-top: 1rem; border-top: 1px solid var(--color-border);">
                                    <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                        <i class="fas fa-map-marker-alt"></i> ${order.address}
                                    </p>
                                </div>
                            </div>
                        </div>
                    `).join('')}
                </div>
            ` : `
                <div class="text-center" style="padding: 4rem 0;">
                    <i class="fas fa-box" style="font-size: 4rem; color: var(--color-text-light); margin-bottom: 1rem;"></i>
                    <h3 style="font-size: 1.25rem; color: var(--color-text); margin-bottom: 0.5rem;">Aucune commande</h3>
                    <p style="color: var(--color-text-light); margin-bottom: 1.5rem;">
                        Vous n'avez pas encore passé de commande.
                    </p>
                    <button class="btn btn-primary" onclick="navigate('gallery')">
                        Découvrir nos produits
                    </button>
                </div>
            `}
        </div>
    `;
}

function getStatusBadge(status) {
    const badges = {
        'en attente': '<span class="badge badge-warning">En attente</span>',
        'en cours': '<span class="badge badge-primary">En cours</span>',
        'livrée': '<span class="badge badge-success">Livrée</span>'
    };
    return badges[status] || `<span class="badge">${status}</span>`;
}

