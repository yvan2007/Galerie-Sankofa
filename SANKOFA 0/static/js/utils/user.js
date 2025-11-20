// ============================================
// USER MANAGEMENT FUNCTIONS
// ============================================

function login(userType = 'client') {
    // userType can be 'client' or 'artisan'
    userRole = userType;
    updateNavigation();
    
    // Redirect based on user type
    if (userType === 'artisan') {
        navigate('dashboard');
    } else {
        // Client is redirected to home or profile
        navigate('home');
    }
}

function logout() {
    userRole = 'visitor';
    updateNavigation();
    navigate('home');
}

function setClientRole() {
    userRole = 'client';
    updateNavigation();
}

function updateNavigation() {
    const userNavLinks = document.getElementById('userNavLinks');
    const userNavLinksMobile = document.getElementById('userNavLinksMobile');
    const logoutBtn = document.getElementById('logoutBtn');
    const logoutBtnMobile = document.getElementById('logoutBtnMobile');
    const loginLinks = document.getElementById('loginLinks');
    const loginLinksMobile = document.getElementById('loginLinksMobile');
    
    if (userRole === 'client') {
        const navLinks = `
            <a href="#" onclick="navigate('tracking'); return false;" class="nav-link" data-page="tracking">
                <i class="fas fa-box"></i> Mes commandes
            </a>
            <a href="#" onclick="navigate('profile'); return false;" class="nav-link" data-page="profile">
                <i class="fas fa-user"></i> Mon profil
            </a>
        `;
        
        if (userNavLinks) userNavLinks.innerHTML = navLinks;
        if (userNavLinksMobile) userNavLinksMobile.innerHTML = navLinks;
        if (logoutBtn) logoutBtn.style.display = 'block';
        if (logoutBtnMobile) logoutBtnMobile.style.display = 'block';
        if (loginLinks) loginLinks.style.display = 'none';
        if (loginLinksMobile) loginLinksMobile.style.display = 'none';
    } else if (userRole === 'artisan') {
        const navLinks = `
            <a href="#" onclick="navigate('dashboard'); return false;" class="nav-link" data-page="dashboard">
                <i class="fas fa-chart-line"></i> Dashboard
            </a>
        `;
        
        if (userNavLinks) userNavLinks.innerHTML = navLinks;
        if (userNavLinksMobile) userNavLinksMobile.innerHTML = navLinks;
        if (logoutBtn) logoutBtn.style.display = 'block';
        if (logoutBtnMobile) logoutBtnMobile.style.display = 'block';
        if (loginLinks) loginLinks.style.display = 'none';
        if (loginLinksMobile) loginLinksMobile.style.display = 'none';
    } else {
        // visitor
        if (userNavLinks) userNavLinks.innerHTML = '';
        if (userNavLinksMobile) userNavLinksMobile.innerHTML = '';
        if (logoutBtn) logoutBtn.style.display = 'none';
        if (logoutBtnMobile) logoutBtnMobile.style.display = 'none';
        if (loginLinks) loginLinks.style.display = 'flex';
        if (loginLinksMobile) loginLinksMobile.style.display = 'flex';
    }
    
    updateActiveNavLink();
}

