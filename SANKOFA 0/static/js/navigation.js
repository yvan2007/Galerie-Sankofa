// ============================================
// NAVIGATION FUNCTIONS
// ============================================

// Navigation Functions
function getPageFromURL() {
    const hash = window.location.hash.replace('#', '');
    return hash || null;
}

function navigate(page, productId = null) {
    currentPage = page;
    currentProductId = productId;
    
    // Update URL
    window.location.hash = page;
    if (productId) {
        window.history.pushState({}, '', `#${page}/${productId}`);
    }
    
    // Update active nav link
    updateActiveNavLink();
    
    // Load page content
    loadPage(page, productId);
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
    // Close mobile menu
    closeMobileMenu();
}

function updateActiveNavLink() {
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.dataset.page === currentPage) {
            link.classList.add('active');
        }
    });
}

function loadPage(page, productId = null) {
    const mainContent = document.getElementById('mainContent');
    
    switch(page) {
        case 'home':
            mainContent.innerHTML = renderHomePage();
            break;
        case 'gallery':
            mainContent.innerHTML = renderGalleryPage();
            break;
        case 'about':
            mainContent.innerHTML = renderAboutPage();
            break;
        case 'contact':
            mainContent.innerHTML = renderContactPage();
            break;
        case 'product':
            mainContent.innerHTML = renderProductPage(productId || currentProductId);
            break;
        case 'order':
            mainContent.innerHTML = renderOrderPage(productId || currentProductId);
            break;
        case 'tracking':
            mainContent.innerHTML = renderTrackingPage();
            break;
        case 'profile':
            mainContent.innerHTML = renderProfilePage();
            break;
        case 'login':
            // Use stored user type or default to client
            const loginType = window.loginUserType || 'client';
            mainContent.innerHTML = renderLoginPage(loginType);
            // Clear the stored type after use
            window.loginUserType = null;
            break;
        case 'register':
            mainContent.innerHTML = renderRegisterPage();
            break;
        case 'dashboard':
            mainContent.innerHTML = renderDashboardPage();
            break;
        default:
            mainContent.innerHTML = renderHomePage();
    }
}

// Hash change listener
window.addEventListener('hashchange', () => {
    const page = getPageFromURL();
    if (page) {
        navigate(page);
    }
});

