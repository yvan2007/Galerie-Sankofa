// ============================================
// GALLERY PAGE
// ============================================

function renderGalleryPage() {
    const filteredProducts = getProductsByCategory(selectedCategory);
    const categories = ['Tous', ...getCategories()];
    
    return `
        <!-- Hero Section -->
        <section style="background: linear-gradient(135deg, var(--color-secondary), var(--color-secondary-dark)); color: white; padding: 4rem 0;">
            <div class="container">
                <div class="text-center">
                    <h1 class="section-title" style="color: var(--color-primary);">Notre Galerie</h1>
                    <p class="section-subtitle" style="color: rgba(255,255,255,0.9);">
                        Explorez notre collection complète d'artisanat traditionnel ivoirien
                    </p>
                </div>
            </div>
        </section>

        <!-- Filter and View Controls -->
        <section style="background-color: var(--color-bg-light); border-bottom: 1px solid var(--color-border); position: sticky; top: 4rem; z-index: 40; padding: 1.5rem 0;">
            <div class="container">
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem;">
                        <i class="fas fa-filter" style="color: var(--color-text);"></i>
                        <span style="font-size: 0.875rem; color: var(--color-text-light);">Catégories:</span>
                        ${categories.map(category => `
                            <button class="badge ${selectedCategory === category ? 'badge-primary' : ''}" 
                                    onclick="setCategory('${category}')"
                                    style="${selectedCategory === category ? 'background-color: var(--color-primary); color: white;' : 'background-color: white; border: 1px solid var(--color-border);'} padding: 0.375rem 1rem; cursor: pointer;">
                                ${category}
                            </button>
                        `).join('')}
                    </div>
                    
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-size: 0.875rem; color: var(--color-text-light);">Affichage:</span>
                        <div style="display: flex; background: white; border-radius: var(--radius); border: 1px solid var(--color-border); padding: 0.25rem;">
                            <button class="tab ${viewMode === 'grid' ? 'active' : ''}" 
                                    onclick="setViewMode('grid')"
                                    style="padding: 0.5rem;">
                                <i class="fas fa-th"></i>
                            </button>
                            <button class="tab ${viewMode === 'list' ? 'active' : ''}" 
                                    onclick="setViewMode('list')"
                                    style="padding: 0.5rem;">
                                <i class="fas fa-list"></i>
                            </button>
                        </div>
                    </div>
                    
                    <div style="font-size: 0.875rem; color: var(--color-text-light);">
                        ${filteredProducts.length} ${filteredProducts.length === 1 ? 'produit trouvé' : 'produits trouvés'}
                        ${selectedCategory !== 'Tous' ? ` dans "${selectedCategory}"` : ''}
                    </div>
                </div>
            </div>
        </section>

        <!-- Products -->
        <section class="section">
            <div class="container">
                ${filteredProducts.length > 0 ? (
                    viewMode === 'grid' 
                        ? `<div class="grid grid-4">${filteredProducts.map(p => renderProductCard(p)).join('')}</div>`
                        : `<div style="display: flex; flex-direction: column; gap: 1rem;">${filteredProducts.map(p => renderProductListCard(p)).join('')}</div>`
                ) : `
                    <div class="text-center" style="padding: 4rem 0;">
                        <div style="width: 5rem; height: 5rem; background-color: #f3f4f6; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                            <i class="fas fa-filter" style="font-size: 2.5rem; color: #9ca3af;"></i>
                        </div>
                        <h3 style="font-size: 1.25rem; color: var(--color-text); margin-bottom: 0.5rem;">Aucun produit trouvé</h3>
                        <p style="color: var(--color-text-light); margin-bottom: 1.5rem;">
                            Essayez de sélectionner une autre catégorie
                        </p>
                        <button class="btn btn-outline" onclick="setCategory('Tous')">
                            Voir tous les produits
                        </button>
                    </div>
                `}
            </div>
        </section>
    `;
}

