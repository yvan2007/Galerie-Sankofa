// ============================================
// HOME PAGE
// ============================================

function renderHomePage() {
    const featuredProducts = selectedCategory === 'Tous' 
        ? products.slice(0, 6) 
        : getProductsByCategory(selectedCategory).slice(0, 6);
    
    const categories = ['Tous', ...getCategories()];
    
    return `
        <!-- Hero Section -->
        <section class="hero">
            <img src="https://images.unsplash.com/photo-1710918861674-c64a977f9de6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920" 
                 alt="Atelier artisan" class="hero-image">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <h1 class="hero-title">Tradition & Innovation</h1>
                <p class="hero-text">L'artisanat ivoirien à l'ère du digital</p>
                <button class="btn btn-primary btn-lg" onclick="navigate('gallery')">
                    Découvrir nos créations
                </button>
            </div>
        </section>

        <!-- About Section -->
        <section class="section">
            <div class="container">
                <div class="grid grid-2" style="gap: 3rem; align-items: center;">
                    <div>
                        <h2 class="section-title" style="text-align: left; margin-bottom: 1.5rem;">Notre Mission</h2>
                        <p style="color: var(--color-text-light); margin-bottom: 1rem;">
                            Galerie Sankofa est née de la passion de préserver et valoriser l'artisanat traditionnel ivoirien. 
                            Chaque pièce que nous créons raconte une histoire, porte en elle des siècles de savoir-faire transmis 
                            de génération en génération.
                        </p>
                        <p style="color: var(--color-text-light);">
                            En alliant techniques ancestrales et designs contemporains, nous donnons une nouvelle vie à nos 
                            traditions, les rendant accessibles au monde entier grâce au digital.
                        </p>
                    </div>
                    <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg);">
                        <img src="https://images.unsplash.com/photo-1710918861674-c64a977f9de6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" 
                             alt="Artisan au travail" style="width: 100%; height: 400px; object-fit: cover;">
                    </div>
                </div>
            </div>
        </section>

        <!-- Products Gallery -->
        <section class="section" style="background-color: var(--color-bg-light);">
            <div class="container">
                <div class="text-center mb-4">
                    <h2 class="section-title">Nos Créations</h2>
                    <p class="section-subtitle">
                        Découvrez notre collection d'œuvres artisanales, chacune unique et fabriquée avec passion
                    </p>
                    
                    <!-- Category Filter -->
                    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-bottom: 2rem;">
                        ${categories.map(category => `
                            <button class="badge ${selectedCategory === category ? 'badge-primary' : ''}" 
                                    onclick="setCategory('${category}'); navigate('home');"
                                    style="${selectedCategory === category ? 'background-color: var(--color-primary); color: white;' : 'background-color: white; border: 1px solid var(--color-border);'} padding: 0.5rem 1.5rem; cursor: pointer;">
                                ${category}
                            </button>
                        `).join('')}
                    </div>
                </div>
                
                <div class="grid grid-3">
                    ${featuredProducts.map(product => renderProductCard(product)).join('')}
                </div>
                
                <div class="text-center mt-4">
                    <button class="btn btn-outline" onclick="navigate('gallery')">
                        Voir toute la galerie
                    </button>
                </div>
            </div>
        </section>

        <!-- Why Choose Sankofa -->
        <section class="section">
            <div class="container">
                <h2 class="section-title">Pourquoi choisir Sankofa ?</h2>
                <div class="grid grid-4" style="margin-top: 2rem;">
                    <div class="card text-center">
                        <div class="card-content">
                            <div style="width: 4rem; height: 4rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                                <i class="fas fa-heart" style="font-size: 2rem; color: var(--color-primary);"></i>
                            </div>
                            <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Fait Main</h3>
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Chaque pièce est unique et fabriquée avec passion par nos artisans
                            </p>
                        </div>
                    </div>
                    
                    <div class="card text-center">
                        <div class="card-content">
                            <div style="width: 4rem; height: 4rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                                <i class="fas fa-check-circle" style="font-size: 2rem; color: var(--color-primary);"></i>
                            </div>
                            <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Authenticité</h3>
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Techniques traditionnelles et matériaux locaux de qualité
                            </p>
                        </div>
                    </div>
                    
                    <div class="card text-center">
                        <div class="card-content">
                            <div style="width: 4rem; height: 4rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                                <i class="fas fa-truck" style="font-size: 2rem; color: var(--color-primary);"></i>
                            </div>
                            <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Livraison</h3>
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Livraison sécurisée partout en Côte d'Ivoire
                            </p>
                        </div>
                    </div>
                    
                    <div class="card text-center">
                        <div class="card-content">
                            <div style="width: 4rem; height: 4rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                                <i class="fas fa-shield-alt" style="font-size: 2rem; color: var(--color-primary);"></i>
                            </div>
                            <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Garantie</h3>
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Satisfaction garantie ou remboursement
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Testimonials -->
        <section class="section" style="background-color: rgba(203, 161, 53, 0.05);">
            <div class="container">
                <h2 class="section-title">Ce que disent nos clients</h2>
                <div class="grid grid-3">
                    <div class="card">
                        <div class="card-content">
                            <div style="color: var(--color-primary); margin-bottom: 1rem;">★★★★★</div>
                            <p style="color: var(--color-text-light); margin-bottom: 1rem;">
                                "Des pièces magnifiques qui apportent une vraie touche d'authenticité à ma maison. 
                                Le travail artisanal est exceptionnel !"
                            </p>
                            <p style="font-size: 0.875rem; color: var(--color-text);">- Aminata K.</p>
                        </div>
                    </div>
                    
                    <div class="card">
                        <div class="card-content">
                            <div style="color: var(--color-primary); margin-bottom: 1rem;">★★★★★</div>
                            <p style="color: var(--color-text-light); margin-bottom: 1rem;">
                                "J'ai commandé plusieurs articles pour offrir. Qualité impeccable et service client 
                                très réactif via WhatsApp."
                            </p>
                            <p style="font-size: 0.875rem; color: var(--color-text);">- Yves T.</p>
                        </div>
                    </div>
                    
                    <div class="card">
                        <div class="card-content">
                            <div style="color: var(--color-primary); margin-bottom: 1rem;">★★★★★</div>
                            <p style="color: var(--color-text-light); margin-bottom: 1rem;">
                                "Fière de soutenir l'artisanat local ! Chaque pièce raconte une histoire et la qualité 
                                est au rendez-vous."
                            </p>
                            <p style="font-size: 0.875rem; color: var(--color-text);">- Marie-Claire D.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    `;
}

