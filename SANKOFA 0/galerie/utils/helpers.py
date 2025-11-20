"""Fonctions utilitaires pour l'application galerie"""


def format_price(price):
    """Formate un prix en XOF"""
    return f"{int(price):,} XOF".replace(',', ' ')


def get_status_badge_html(status):
    """Retourne le HTML du badge de statut"""
    badges = {
        'en attente': '<span class="badge badge-warning">En attente</span>',
        'en cours': '<span class="badge badge-primary">En cours</span>',
        'livrée': '<span class="badge" style="background-color: #10b981; color: white;">Livrée</span>',
        'annulée': '<span class="badge" style="background-color: #ef4444; color: white;">Annulée</span>',
    }
    return badges.get(status, f'<span class="badge">{status}</span>')

