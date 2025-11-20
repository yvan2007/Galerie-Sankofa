// ============================================
// ABOUT PAGE
// ============================================

function renderAboutPage() {
    return `
        <div class="container" style="padding: 3rem 0;">
            <div class="text-center mb-4">
                <h1 class="section-title">À Propos de Galerie Sankofa</h1>
                <p class="section-subtitle">
                    Une passion pour l'artisanat traditionnel ivoirien, transmise de génération en génération
                </p>
            </div>

            <section style="margin-bottom: 4rem;">
                <div class="grid grid-2" style="gap: 3rem; align-items: center;">
                    <div style="aspect-ratio: 4/3; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg);">
                        <img src="https://images.unsplash.com/photo-1710918861674-c64a977f9de6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" 
                             alt="Artisan au travail" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    <div>
                        <h2 style="font-size: 2rem; color: var(--color-text); margin-bottom: 1.5rem;">Notre Histoire</h2>
                        <p style="color: var(--color-text-light); margin-bottom: 1rem;">
                            Galerie Sankofa est née de la vision de préserver et valoriser l'artisanat traditionnel 
                            ivoirien dans un monde en constante évolution. Le nom "Sankofa" vient du symbole Akan qui 
                            signifie "retourne et prends" - l'importance de se souvenir du passé pour construire l'avenir.
                        </p>
                        <p style="color: var(--color-text-light); margin-bottom: 1rem;">
                            Depuis plus de 20 ans, notre atelier situé au cœur d'Abidjan perpétue les techniques 
                            ancestrales transmises par nos maîtres artisans. Chaque pièce que nous créons est le 
                            fruit d'un savoir-faire unique, alliant tradition et innovation.
                        </p>
                        <p style="color: var(--color-text-light);">
                            Grâce au digital, nous partageons aujourd'hui notre passion avec le monde entier, 
                            permettant à chacun de découvrir et d'acquérir des œuvres authentiques qui racontent 
                            l'histoire et la culture de la Côte d'Ivoire.
                        </p>
                    </div>
                </div>
            </section>

            <section style="margin-bottom: 4rem;">
                <div class="text-center mb-4">
                    <h2 class="section-title">Nos Valeurs</h2>
                    <p class="section-subtitle">Les principes qui guident notre travail au quotidien</p>
                </div>
                <div class="grid grid-4">
                    <div class="card text-center" style="background-color: var(--color-bg-light);">
                        <div class="card-content">
                            <div style="width: 4rem; height: 4rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                                <i class="fas fa-heart" style="font-size: 2rem; color: var(--color-primary);"></i>
                            </div>
                            <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Passion</h3>
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Chaque création est réalisée avec amour et dévouement
                            </p>
                        </div>
                    </div>
                    <div class="card text-center" style="background-color: var(--color-bg-light);">
                        <div class="card-content">
                            <div style="width: 4rem; height: 4rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                                <i class="fas fa-award" style="font-size: 2rem; color: var(--color-primary);"></i>
                            </div>
                            <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Authenticité</h3>
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Des techniques ancestrales et des matériaux locaux de qualité
                            </p>
                        </div>
                    </div>
                    <div class="card text-center" style="background-color: var(--color-bg-light);">
                        <div class="card-content">
                            <div style="width: 4rem; height: 4rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                                <i class="fas fa-users" style="font-size: 2rem; color: var(--color-primary);"></i>
                            </div>
                            <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Communauté</h3>
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Soutenir les artisans locaux et préserver notre héritage
                            </p>
                        </div>
                    </div>
                    <div class="card text-center" style="background-color: var(--color-bg-light);">
                        <div class="card-content">
                            <div style="width: 4rem; height: 4rem; background-color: rgba(203, 161, 53, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
                                <i class="fas fa-bullseye" style="font-size: 2rem; color: var(--color-primary);"></i>
                            </div>
                            <h3 style="color: var(--color-text); margin-bottom: 0.5rem;">Excellence</h3>
                            <p style="font-size: 0.875rem; color: var(--color-text-light);">
                                Un engagement constant envers la qualité et la satisfaction
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <section style="margin-bottom: 4rem;">
                <div class="text-center mb-4">
                    <h2 class="section-title">Notre Atelier</h2>
                    <p class="section-subtitle">Un espace où la tradition rencontre la modernité</p>
                </div>
                <div class="grid grid-3">
                    <div style="aspect-ratio: 3/4; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg);">
                        <img src="https://images.unsplash.com/photo-1612950662573-546117a61e78?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" 
                             alt="Vue de l'atelier" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    <div style="aspect-ratio: 3/4; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg);">
                        <img src="https://images.unsplash.com/photo-1760681556856-e7e5e77a46ef?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" 
                             alt="Artisan travaillant" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    <div style="aspect-ratio: 3/4; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg);">
                        <img src="https://images.unsplash.com/photo-1633949840687-c9d9e0ca7892?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" 
                             alt="Produits finis" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                </div>
            </section>

            <section style="background-color: var(--color-secondary); color: white; border-radius: var(--radius-lg); padding: 3rem;">
                <div style="max-width: 48rem; margin: 0 auto; text-align: center;">
                    <h2 style="font-size: 2rem; color: var(--color-primary); margin-bottom: 1.5rem;">Notre Mission</h2>
                    <p style="font-size: 1.125rem; margin-bottom: 1.5rem;">
                        Préserver et promouvoir l'artisanat traditionnel ivoirien en le rendant accessible 
                        au monde entier grâce au digital, tout en soutenant les communautés d'artisans locaux 
                        et en transmettant leur savoir-faire aux générations futures.
                    </p>
                    <p style="color: #d1d5db;">
                        Chaque achat chez Galerie Sankofa contribue directement au développement de notre 
                        communauté artisanale et à la préservation de notre patrimoine culturel.
                    </p>
                </div>
            </section>
        </div>
    `;
}

