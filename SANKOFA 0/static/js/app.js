// ============================================
// GALERIE SANKOFA - APPLICATION
// ============================================

// Application State
let currentPage = 'home';
let currentProductId = null;
let userRole = 'visitor'; // 'visitor', 'client', 'artisan'
let selectedCategory = 'Tous';
let viewMode = 'grid'; // 'grid' or 'list'

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});

function initializeApp() {
    // Load initial page
    const page = getPageFromURL() || 'home';
    navigate(page);
    
    // Setup mobile menu
    setupMobileMenu();
    
    // Update navigation based on user role
    updateNavigation();
}

