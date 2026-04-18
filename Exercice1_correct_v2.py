MAX_WIDTH = 100

phrases_data = {
    'bloc1_phrase1': {'texte': 'le code propre facilite la maintenance', 'afficher': True},
    'bloc2_phrase1': {'texte': 'tester souvent évite beaucoup d erreurs', 'afficher': True},
    'bloc2_phrase2': {'texte': 'cette phrase ne doit pas s afficher', 'afficher': False},
    'bloc3_phrase1': {'texte': 'cette phrase ne doit pas s afficher', 'afficher': False},
    'bloc3_phrase2': {'texte': 'un bon code doit rester simple et clair', 'afficher': False},
    'bloc3_phrase3': {'texte': 'la simplicité améliore la qualité du code', 'afficher': True},
    'bloc3_phrase4': {'texte': 'refactoriser améliore la compréhension', 'afficher': True},
}

blocs_structure = {
    'bloc1': ['bloc1_phrase1'],
    'bloc2': ['bloc2_phrase1', 'bloc2_phrase2'],
    'bloc3': ['bloc3_phrase1', 'bloc3_phrase2', 'bloc3_phrase3', 'bloc3_phrase4'],
}

affichage_order = ['bloc1', 'bloc2', 'bloc3']


def create_border_line():
    return '|' + '-' * (MAX_WIDTH - 2) + '|'


def create_text_line(text):
    text = text.lower()
    if len(text) <= MAX_WIDTH - 4:
        padding = MAX_WIDTH - len(text) - 4
        return '| ' + text + ' ' * padding + ' |'
    else:
        return '| ' + text[:MAX_WIDTH - 4] + ' |'


def display_block(block_id):
    phrases_list = blocs_structure[block_id]
    
    block_phrases = []
    for phrase_key in phrases_list:
        if phrases_data[phrase_key]['afficher']:
            block_phrases.append(phrases_data[phrase_key]['texte'])
    
    if not block_phrases:
        return
    
    print(create_border_line())
    
    for phrase in block_phrases:
        print(create_text_line(phrase))
    
    print(create_border_line())
    print()


for block_id in affichage_order:
    display_block(block_id)
