# ============================================================================
# EXERCICE : Afficher des blocs de texte encadrés
# ============================================================================

# ÉTAPE 1 : Définir la largeur maximale 
LARGEUR_MAX = 100

# ÉTAPE 2 : Créer un dictionnaire avec toutes les phrases
phrases = {
    "bloc1_ligne1": "Le code propre facilite la maintenance",
    
    "bloc2_ligne1": "Tester souvent évite beaucoup d erreurs",
    "bloc2_cachee": "Cette phrase ne doit pas s'afficher",
    
    "bloc3_cachee1": "Cette phrase ne doit pas s'afficher",
    "bloc3_ligne1": "Un bon code doit rester simple et clair",
    "bloc3_ligne2": "La simplicité améliore la qualité du code",
    "bloc3_ligne3": "Refactoriser améliore la compréhension",
}

# ÉTAPE 3 : Définir l'ordre d'affichage des blocs
# Chaque bloc est une liste de clés du dictionnaire
blocs_a_afficher = [
    ["bloc1_ligne1"],  # Bloc 1 : une seule ligne
    ["bloc2_ligne1"],  # Bloc 2 : une seule ligne (on omet bloc2_cachee)
    ["bloc3_ligne2", "bloc3_ligne3"],  # Bloc 3 : deux lignes (on omet bloc3_cachee1 et bloc3_ligne1)
]

# ============================================================================
# ÉTAPE 4 : Créer les fonctions pour afficher les blocs
# ============================================================================

def convertir_en_minuscules(texte):
    return texte.lower()

def creer_ligne_separator(largeur):
    return "|" + "-" * (largeur - 2) + "|"

def creer_ligne_texte(texte, largeur):
    # Convertir en minuscules
    texte = convertir_en_minuscules(texte)
    
    # Calculer les espaces
    largeur_interieure = largeur - 2  # -2 pour les deux |
    espace_total = largeur_interieure - len(texte)
    espace_gauche = espace_total // 2
    espace_droit = espace_total - espace_gauche
    
    return "|" + " " * espace_gauche + texte + " " * espace_droit + "|"

def afficher_bloc(liste_cles, dictionnaire, largeur):
    """Affiche un bloc avec un cadre"""
    # Ligne supérieure
    print(creer_ligne_separator(largeur))
    
    # Lignes de texte
    for cle in liste_cles:
        texte = dictionnaire[cle]
        print(creer_ligne_texte(texte, largeur))
    
    # Ligne inférieure
    print(creer_ligne_separator(largeur))

# ============================================================================
# ÉTAPE 5 : Afficher tous les blocs
# ============================================================================

print("\n")  # Un peu d'espace au début
for bloc in blocs_a_afficher:
    afficher_bloc(bloc, phrases, LARGEUR_MAX)
    print()  # Une ligne vide entre les blocs