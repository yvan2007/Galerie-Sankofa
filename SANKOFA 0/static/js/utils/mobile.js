// ============================================
// MOBILE MENU FUNCTIONS
// ============================================

function setupMobileMenu() {
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navMobile = document.getElementById('navMobile');
    
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', toggleMobileMenu);
    }
}

function toggleMobileMenu() {
    const navMobile = document.getElementById('navMobile');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    
    if (navMobile) {
        navMobile.classList.toggle('active');
        const icon = mobileMenuBtn.querySelector('i');
        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        }
    }
}

function closeMobileMenu() {
    const navMobile = document.getElementById('navMobile');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    
    if (navMobile) {
        navMobile.classList.remove('active');
        const icon = mobileMenuBtn?.querySelector('i');
        if (icon) {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    }
}

