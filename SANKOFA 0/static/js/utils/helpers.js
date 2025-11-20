// ============================================
// UTILITY HELPER FUNCTIONS
// ============================================

// Category Filter
function setCategory(category) {
    selectedCategory = category;
    if (currentPage === 'gallery' || currentPage === 'home') {
        loadPage(currentPage);
    }
}

// View Mode Toggle
function setViewMode(mode) {
    viewMode = mode;
    if (currentPage === 'gallery') {
        loadPage('gallery');
    }
}

// WhatsApp Integration
function openWhatsApp(productName = '', quantity = 1, price = 0) {
    let message = 'Bonjour, ';
    if (productName) {
        message += `je suis intéressé(e) par ${quantity} x ${productName}`;
        if (price > 0) {
            message += ` (${formatPrice(price)})`;
        }
    } else {
        message += 'j\'aimerais en savoir plus sur vos produits artisanaux.';
    }
    
    const url = `https://wa.me/22507000000?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank');
}

