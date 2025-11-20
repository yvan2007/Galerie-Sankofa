// ============================================
// DASHBOARD PAGE
// ============================================

function renderDashboardPage() {
    const totalProducts = products.length;
    const totalOrders = orders.length;
    const totalSales = orders.reduce((sum, order) => sum + order.total, 0);
    const pendingOrders = orders.filter(o => o.status === 'en attente').length;
    const inStockProducts = products.filter(p => p.availability).length;
    
    return `
        <div class="dashboard-header">
            <div class="container">
                <div class="dashboard-header-content">
                    <div style="display: flex; align-items: center; gap: 0.75rem;">
                        <div style="width: 2.5rem; height: 2.5rem; background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark)); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: var(--shadow-md);">
                            <span style="color: white; font-size: 1.25rem; font-weight: 600;">S</span>
                        </div>
                        <div>
                            <h1 class="dashboard-title">Dashboard Artisan</h1>
                            <p class="dashboard-subtitle">Galerie Sankofa</p>
                        </div>
                    </div>
                    <button class="btn-logout" onclick="logout()" style="color: white; border: 1px solid rgba(255,255,255,0.2);">
                        <i class="fas fa-sign-out-alt"></i> Déconnexion
                    </button>
                </div>
            </div>
        </div>

        <div class="container" style="padding: 2rem 0;">
            <div style="margin-bottom: 2rem;">
                <h2 style="font-size: 1.5rem; color: var(--color-text); margin-bottom: 0.5rem;">Vue d'ensemble</h2>
                <p style="color: var(--color-text-light);">
                    Gérez vos produits, commandes et suivez vos statistiques
                </p>
            </div>

            <!-- Tabs -->
            <div class="tabs">
                <div class="tabs-list">
                    <button class="tab active" onclick="switchTab('overview')">
                        <i class="fas fa-chart-line"></i> Vue d'ensemble
                    </button>
                    <button class="tab" onclick="switchTab('products')">
                        <i class="fas fa-box"></i> Produits
                    </button>
                    <button class="tab" onclick="switchTab('orders')">
                        <i class="fas fa-shopping-cart"></i> Commandes
                    </button>
                    <button class="tab" onclick="switchTab('profile')">
                        <i class="fas fa-user"></i> Profil
                    </button>
                </div>

                <!-- Overview Tab -->
                <div id="tab-overview" class="tab-content active">
                    <div class="stats-grid">
                        <div class="stat-card">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                                <span style="color: var(--color-text-light); font-size: 0.875rem;">Ventes totales</span>
                                <i class="fas fa-arrow-up" style="color: #10b981;"></i>
                            </div>
                            <div style="font-size: 1.875rem; font-weight: 700; color: var(--color-text);">
                                ${formatPrice(totalSales)}
                            </div>
                            <p style="font-size: 0.875rem; color: var(--color-text-light); margin-top: 0.25rem;">+12% ce mois</p>
                        </div>
                        <div class="stat-card">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                                <span style="color: var(--color-text-light); font-size: 0.875rem;">Produits</span>
                                <i class="fas fa-box" style="color: var(--color-primary);"></i>
                            </div>
                            <div style="font-size: 1.875rem; font-weight: 700; color: var(--color-text);">
                                ${totalProducts}
                            </div>
                            <p style="font-size: 0.875rem; color: var(--color-text-light); margin-top: 0.25rem;">${inStockProducts} en stock</p>
                        </div>
                        <div class="stat-card">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                                <span style="color: var(--color-text-light); font-size: 0.875rem;">Commandes</span>
                                <i class="fas fa-shopping-cart" style="color: #3b82f6;"></i>
                            </div>
                            <div style="font-size: 1.875rem; font-weight: 700; color: var(--color-text);">
                                ${totalOrders}
                            </div>
                            <p style="font-size: 0.875rem; color: var(--color-text-light); margin-top: 0.25rem;">${pendingOrders} en attente</p>
                        </div>
                    </div>

                    <div class="card" style="margin-top: 2rem;">
                        <div class="card-content">
                            <h3 style="font-size: 1.25rem; color: var(--color-text); margin-bottom: 1rem;">Commandes récentes</h3>
                            <div class="table-wrapper">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>N° Commande</th>
                                            <th>Client</th>
                                            <th>Produit</th>
                                            <th>Total</th>
                                            <th>Statut</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${orders.slice(0, 5).map(order => `
                                            <tr>
                                                <td>${order.id}</td>
                                                <td>${order.customerName}</td>
                                                <td>${order.product}</td>
                                                <td>${formatPrice(order.total)}</td>
                                                <td>${getStatusBadge(order.status)}</td>
                                            </tr>
                                        `).join('')}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Products Tab -->
                <div id="tab-products" class="tab-content">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                        <h2 style="font-size: 1.25rem; color: var(--color-text);">Gestion des produits</h2>
                        <button class="btn btn-primary">
                            <i class="fas fa-plus"></i> Ajouter un produit
                        </button>
                    </div>
                    <div class="card">
                        <div class="card-content" style="padding: 0;">
                            <div class="table-wrapper">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>Image</th>
                                            <th>Nom</th>
                                            <th>Catégorie</th>
                                            <th>Prix</th>
                                            <th>Stock</th>
                                            <th>Actions</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${products.map(product => `
                                            <tr>
                                                <td>
                                                    <img src="${product.image}" alt="${product.name}" 
                                                         style="width: 3rem; height: 3rem; object-fit: cover; border-radius: var(--radius);">
                                                </td>
                                                <td>${product.name}</td>
                                                <td>${product.category}</td>
                                                <td>${formatPrice(product.price)}</td>
                                                <td>
                                                    ${product.availability 
                                                        ? '<span class="badge badge-success">En stock</span>'
                                                        : '<span class="badge badge-danger">Épuisé</span>'
                                                    }
                                                </td>
                                                <td>
                                                    <div style="display: flex; gap: 0.5rem;">
                                                        <button class="btn btn-outline" style="padding: 0.5rem;">
                                                            <i class="fas fa-edit" style="color: #3b82f6;"></i>
                                                        </button>
                                                        <button class="btn btn-outline" style="padding: 0.5rem;">
                                                            <i class="fas fa-trash" style="color: #ef4444;"></i>
                                                        </button>
                                                    </div>
                                                </td>
                                            </tr>
                                        `).join('')}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Orders Tab -->
                <div id="tab-orders" class="tab-content">
                    <h2 style="font-size: 1.25rem; color: var(--color-text); margin-bottom: 1.5rem;">Gestion des commandes</h2>
                    <div class="card">
                        <div class="card-content" style="padding: 0;">
                            <div class="table-wrapper">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>N° Commande</th>
                                            <th>Date</th>
                                            <th>Client</th>
                                            <th>Téléphone</th>
                                            <th>Produit</th>
                                            <th>Quantité</th>
                                            <th>Total</th>
                                            <th>Statut</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${orders.map(order => `
                                            <tr>
                                                <td>${order.id}</td>
                                                <td>${new Date(order.date).toLocaleDateString('fr-FR')}</td>
                                                <td>${order.customerName}</td>
                                                <td>${order.phone}</td>
                                                <td>${order.product}</td>
                                                <td>${order.quantity}</td>
                                                <td>${formatPrice(order.total)}</td>
                                                <td>${getStatusBadge(order.status)}</td>
                                            </tr>
                                        `).join('')}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Profile Tab -->
                <div id="tab-profile" class="tab-content">
                    <h2 style="font-size: 1.25rem; color: var(--color-text); margin-bottom: 1.5rem;">Profil de l'artisan</h2>
                    <div class="card">
                        <div class="card-content">
                            <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                                <div>
                                    <label style="display: block; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.5rem;">Nom de la galerie</label>
                                    <p style="color: var(--color-text); font-weight: 500;">Galerie Sankofa</p>
                                </div>
                                <div>
                                    <label style="display: block; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.5rem;">Email</label>
                                    <p style="color: var(--color-text); font-weight: 500;">contact@galeriesankofa.ci</p>
                                </div>
                                <div>
                                    <label style="display: block; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.5rem;">Téléphone</label>
                                    <p style="color: var(--color-text); font-weight: 500;">+225 07 00 00 00 00</p>
                                </div>
                                <div>
                                    <label style="display: block; font-size: 0.875rem; color: var(--color-text-light); margin-bottom: 0.5rem;">Adresse</label>
                                    <p style="color: var(--color-text); font-weight: 500;">GRAND-BASSAM, Côte d'Ivoire</p>
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
            </div>
        </div>
    `;
}

function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    document.querySelectorAll('.tab').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    const tabContent = document.getElementById(`tab-${tabName}`);
    const tabButton = event.target.closest('.tab');
    
    if (tabContent) tabContent.classList.add('active');
    if (tabButton) tabButton.classList.add('active');
}

