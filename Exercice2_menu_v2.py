menu_data = {
    'entrees': [
        {'nom': 'salade cesar', 'prix': 8, 'disponible': True},
        {'nom': 'soupe du jour', 'prix': 6, 'disponible': False},
    ],
    'plats': [
        {'nom': 'steak frites', 'prix': 15, 'disponible': True},
        {'nom': 'poisson grille', 'prix': 14, 'disponible': True},
        {'nom': 'plat du chef', 'prix': 18, 'disponible': False},
    ],
    'desserts': [
        {'nom': 'tiramisu', 'prix': 7, 'disponible': True},
        {'nom': 'glace', 'prix': 5, 'disponible': True},
        {'nom': 'dessert mystere', 'prix': 9, 'disponible': False},
    ],
}

category_names = {
    'entrees': 'entrees',
    'plats': 'plats',
    'desserts': 'desserts',
}


def display_menu():
    for category_key, category_name in category_names.items():
        print(f'--- {category_name} ---')
        
        category_items = menu_data[category_key]
        
        for item in category_items:
            if item['disponible']:
                nom = item['nom'].lower()
                prix = item['prix']
                print(f'{nom} - {prix}€')
        
        print()


display_menu()
