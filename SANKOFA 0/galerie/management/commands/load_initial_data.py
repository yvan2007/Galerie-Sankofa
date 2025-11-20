from django.core.management.base import BaseCommand
from galerie.models import Category, Product


class Command(BaseCommand):
    help = 'Charge les données initiales (catégories et produits)'

    def handle(self, *args, **options):
        # Créer les catégories
        categories_data = [
            {'name': 'Céramique', 'description': 'Poterie et céramique traditionnelle'},
            {'name': 'Vannerie', 'description': 'Paniers et objets tressés'},
            {'name': 'Textile', 'description': 'Tissus et étoffes traditionnels'},
            {'name': 'Sculpture', 'description': 'Sculptures en bois et autres matériaux'},
            {'name': 'Bijouterie', 'description': 'Bijoux artisanaux'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Catégorie créée: {category.name}'))

        # Créer les produits
        products_data = [
            {
                'name': 'Poterie Traditionnelle',
                'description': 'Pot en argile fait main, motifs traditionnels ivoiriens',
                'details': 'Cette poterie traditionnelle est fabriquée à la main avec de l\'argile locale. Chaque pièce est unique et porte les motifs ancestraux de la culture ivoirienne. Parfait pour la décoration ou usage quotidien.',
                'price': 45000,
                'category': 'Céramique',
                'image_url': 'https://images.unsplash.com/photo-1681381763285-1a4a72db80a7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080',
                'availability': True,
            },
            {
                'name': 'Panier Tissé',
                'description': 'Panier artisanal en fibres naturelles, tressage traditionnel',
                'details': 'Panier tissé à la main selon les techniques ancestrales. Fabriqué avec des fibres naturelles récoltées localement. Idéal pour le rangement ou comme élément décoratif.',
                'price': 35000,
                'category': 'Vannerie',
                'image_url': 'https://images.unsplash.com/photo-1567696154083-9547fd0c8e1d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080',
                'availability': True,
            },
            {
                'name': 'Textile Traditionnel',
                'description': 'Tissu artisanal aux motifs africains authentiques',
                'details': 'Tissu traditionnel authentique teint selon les méthodes ancestrales. Chaque motif raconte une histoire et représente un symbole culturel important.',
                'price': 55000,
                'category': 'Textile',
                'image_url': 'https://images.unsplash.com/photo-1655682597213-1fa005eb18b9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080',
                'availability': True,
            },
            {
                'name': 'Sculpture en Bois',
                'description': 'Sculpture artisanale en bois noble, finition polie',
                'details': 'Sculpture en bois d\'ébène sculptée à la main par nos artisans expérimentés. Finition polie à l\'huile naturelle. Pièce unique qui apportera une touche d\'authenticité à votre intérieur.',
                'price': 75000,
                'category': 'Sculpture',
                'image_url': 'https://images.unsplash.com/photo-1633949840687-c9d9e0ca7892?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080',
                'availability': True,
            },
            {
                'name': 'Masque Décoratif',
                'description': 'Masque tribal en bois sculpté, peintures naturelles',
                'details': 'Masque décoratif inspiré des traditions tribales ivoiriennes. Sculpté dans du bois noble et peint avec des pigments naturels. Chaque masque est une œuvre d\'art unique.',
                'price': 65000,
                'category': 'Sculpture',
                'image_url': 'https://images.unsplash.com/photo-1757009400493-509e7b48c95d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080',
                'availability': False,
            },
            {
                'name': 'Bijoux Perlés',
                'description': 'Collier en perles traditionnelles, assemblage artisanal',
                'details': 'Collier assemblé à la main avec des perles traditionnelles. Chaque perle est sélectionnée avec soin pour créer une harmonie de couleurs unique. Longueur ajustable.',
                'price': 25000,
                'category': 'Bijouterie',
                'image_url': 'https://images.unsplash.com/photo-1757140448293-fa0de8f449e5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080',
                'availability': True,
            },
        ]

        for prod_data in products_data:
            category = categories[prod_data.pop('category')]
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    **prod_data,
                    'category': category
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Produit créé: {product.name}'))

        self.stdout.write(self.style.SUCCESS('\nDonnées initiales chargées avec succès !'))

