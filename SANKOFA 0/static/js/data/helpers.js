// ============================================
// DATA HELPER FUNCTIONS
// ============================================

function formatPrice(price) {
    return new Intl.NumberFormat('fr-FR', {
        style: 'currency',
        currency: 'XOF',
        minimumFractionDigits: 0
    }).format(price);
}

function getCategories() {
    const categories = new Set();
    products.forEach(product => categories.add(product.category));
    return Array.from(categories);
}

function getProductById(id) {
    return products.find(p => p.id === id);
}

function getProductsByCategory(category) {
    if (category === "Tous") return products;
    return products.filter(p => p.category === category);
}

function getRelatedProducts(productId, limit = 3) {
    const product = getProductById(productId);
    if (!product) return [];
    return products
        .filter(p => p.category === product.category && p.id !== productId)
        .slice(0, limit);
}

