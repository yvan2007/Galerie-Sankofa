// ============================================
// GALERIE SANKOFA - DATA
// ============================================

// Products Data
const products = [
    {
        id: "1",
        name: "Poterie Traditionnelle",
        description: "Pot en argile fait main, motifs traditionnels ivoiriens",
        price: 45000,
        image: "https://images.unsplash.com/photo-1681381763285-1a4a72db80a7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Céramique",
        availability: true,
        details: "Cette poterie traditionnelle est fabriquée à la main avec de l'argile locale. Chaque pièce est unique et porte les motifs ancestraux de la culture ivoirienne. Parfait pour la décoration ou usage quotidien."
    },
    {
        id: "2",
        name: "Panier Tissé",
        description: "Panier artisanal en fibres naturelles, tressage traditionnel",
        price: 35000,
        image: "https://images.unsplash.com/photo-1567696154083-9547fd0c8e1d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Vannerie",
        availability: true,
        details: "Panier tissé à la main selon les techniques ancestrales. Fabriqué avec des fibres naturelles récoltées localement. Idéal pour le rangement ou comme élément décoratif."
    },
    {
        id: "3",
        name: "Textile Traditionnel",
        description: "Tissu artisanal aux motifs africains authentiques",
        price: 55000,
        image: "https://images.unsplash.com/photo-1655682597213-1fa005eb18b9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Textile",
        availability: true,
        details: "Tissu traditionnel authentique teint selon les méthodes ancestrales. Chaque motif raconte une histoire et représente un symbole culturel important."
    },
    {
        id: "4",
        name: "Sculpture en Bois",
        description: "Sculpture artisanale en bois noble, finition polie",
        price: 75000,
        image: "https://images.unsplash.com/photo-1633949840687-c9d9e0ca7892?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Sculpture",
        availability: true,
        details: "Sculpture en bois d'ébène sculptée à la main par nos artisans expérimentés. Finition polie à l'huile naturelle. Pièce unique qui apportera une touche d'authenticité à votre intérieur."
    },
    {
        id: "5",
        name: "Masque Décoratif",
        description: "Masque tribal en bois sculpté, peintures naturelles",
        price: 65000,
        image: "https://images.unsplash.com/photo-1757009400493-509e7b48c95d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Sculpture",
        availability: false,
        details: "Masque décoratif inspiré des traditions tribales ivoiriennes. Sculpté dans du bois noble et peint avec des pigments naturels. Chaque masque est une œuvre d'art unique."
    },
    {
        id: "6",
        name: "Bijoux Perlés",
        description: "Collier en perles traditionnelles, assemblage artisanal",
        price: 25000,
        image: "https://images.unsplash.com/photo-1757140448293-fa0de8f449e5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Bijouterie",
        availability: true,
        details: "Collier assemblé à la main avec des perles traditionnelles. Chaque perle est sélectionnée avec soin pour créer une harmonie de couleurs unique. Longueur ajustable."
    },
    {
        id: "7",
        name: "Vase en Céramique",
        description: "Grand vase décoratif en argile, motifs géométriques",
        price: 52000,
        image: "https://images.unsplash.com/photo-1695740633675-d060b607f5c4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Céramique",
        availability: true,
        details: "Vase en céramique façonné à la main avec des motifs géométriques inspirés de l'art traditionnel. Pièce décorative unique pour sublimer votre intérieur."
    },
    {
        id: "8",
        name: "Corbeille Tressée",
        description: "Corbeille artisanale multi-usage, fibres colorées",
        price: 28000,
        image: "https://images.unsplash.com/photo-1688240817677-d28b8e232dd4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Vannerie",
        availability: true,
        details: "Corbeille tressée à la main avec des fibres naturelles teintes. Idéale pour le rangement ou comme panier à provisions. Résistante et durable."
    },
    {
        id: "9",
        name: "Étoffe Kente",
        description: "Tissu Kente authentique, bandes tissées main",
        price: 68000,
        image: "https://images.unsplash.com/photo-1663044022726-889ee51a682e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Textile",
        availability: true,
        details: "Tissu Kente tissé selon la tradition ouest-africaine. Chaque bande est tissée individuellement puis assemblée. Symbole de prestige et d'héritage culturel."
    },
    {
        id: "10",
        name: "Statuette Ancestrale",
        description: "Sculpture représentant une figure ancestrale",
        price: 85000,
        image: "https://images.unsplash.com/photo-1760681556856-e7e5e77a46ef?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Sculpture",
        availability: true,
        details: "Statuette sculptée dans du bois noble représentant une figure ancestrale. Symbole de sagesse et de protection. Finition soignée avec patine naturelle."
    },
    {
        id: "11",
        name: "Bracelet Artisanal",
        description: "Bracelet traditionnel fait main",
        price: 18000,
        image: "https://images.unsplash.com/photo-1758995116383-f51775896add?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Bijouterie",
        availability: true,
        details: "Bracelet artisanal martelé à la main selon les techniques ancestrales. Motifs gravés représentant des symboles traditionnels. Ajustable."
    },
    {
        id: "12",
        name: "Poterie Décorée",
        description: "Pot en argile décoré à la main, style traditionnel",
        price: 32000,
        image: "https://images.unsplash.com/photo-1582140099533-11fe4d348e01?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Céramique",
        availability: false,
        details: "Poterie décorative en terre cuite avec motifs traditionnels peints à la main. Parfaite pour la décoration ou comme pièce fonctionnelle lors d'occasions spéciales."
    },
    {
        id: "13",
        name: "Panier Décoratif",
        description: "Panier tressé coloré, finition artisanale",
        price: 22000,
        image: "https://images.unsplash.com/photo-1572796078439-ad087023b3b9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Vannerie",
        availability: true,
        details: "Panier tressé à la main avec des fibres naturelles. Design élégant et résistant. Idéal pour le rangement ou comme élément décoratif."
    },
    {
        id: "14",
        name: "Tissu Batik",
        description: "Tissu batik artisanal, teinture à la cire",
        price: 42000,
        image: "https://images.unsplash.com/photo-1652355008626-22da23215341?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Textile",
        availability: true,
        details: "Tissu en batik créé selon la technique traditionnelle de teinture à la cire. Motifs uniques et couleurs vibrantes. Tissu polyvalent pour vêtements ou décoration."
    },
    {
        id: "15",
        name: "Tambour Djembé",
        description: "Djembé artisanal sculpté, peau de chèvre",
        price: 95000,
        image: "https://images.unsplash.com/photo-1760310509425-66b613515006?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        category: "Sculpture",
        availability: true,
        details: "Djembé traditionnel sculpté à la main dans un tronc d'arbre. Peau de chèvre authentique tendue. Son riche et profond. Pièce fonctionnelle et décorative."
    }
];

// Orders Data
const orders = [
    {
        id: "CMD001",
        customerName: "Konan Kouassi",
        product: "Poterie Traditionnelle",
        quantity: 2,
        status: "en cours",
        date: "2025-10-20",
        total: 90000,
        phone: "+225 07 00 00 00 01",
        address: "Abidjan, Cocody"
    },
    {
        id: "CMD002",
        customerName: "Aya Traoré",
        product: "Textile Traditionnel",
        quantity: 1,
        status: "livrée",
        date: "2025-10-18",
        total: 55000,
        phone: "+225 07 00 00 00 02",
        address: "Abidjan, Plateau"
    },
    {
        id: "CMD003",
        customerName: "Mamadou Diallo",
        product: "Panier Tissé",
        quantity: 3,
        status: "en attente",
        date: "2025-10-21",
        total: 105000,
        phone: "+225 07 00 00 00 03",
        address: "Yamoussoukro"
    }
];

// Helper Functions
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
