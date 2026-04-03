from django import forms
from .models import Produit, Facture, LigneFacture


# ============================================================================
# FORMULAIRE 1 : CRÉER/MODIFIER UN PRODUIT
# ============================================================================
class ProduitForm(forms.ModelForm):
    """
    Formulaire pour créer ou modifier un produit.
    L'utilisateur remplit : nom, prix, date de péremption
    """
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'date_peremption']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Pommes'
            }),
            'prix': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 2.50',
                'step': '0.01'
            }),
            'date_peremption': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'nom': 'Nom du produit',
            'prix': 'Prix (€)',
            'date_peremption': 'Date de péremption',
        }


# ============================================================================
# FORMULAIRE 2 : CRÉER UNE FACTURE
# ============================================================================
class FactureForm(forms.ModelForm):
    """
    Formulaire pour créer une facture.
    L'utilisateur ne spécifie rien, la date est créée automatiquement.
    """
    class Meta:
        model = Facture
        fields = []  # Pas de champ à remplir, tout est automatique


# ============================================================================
# FORMULAIRE 3 : AJOUTER UN PRODUIT À UNE FACTURE
# ============================================================================
class LigneFactureForm(forms.ModelForm):
    """
    Formulaire pour ajouter un produit à une facture.
    L'utilisateur choisit un produit et sa quantité.
    """
    class Meta:
        model = LigneFacture
        fields = ['produit', 'quantite']
        widgets = {
            'produit': forms.Select(attrs={
                'class': 'form-control',
            }),
            'quantite': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'type': 'number'
            }),
        }
        labels = {
            'produit': 'Choisir un produit',
            'quantite': 'Quantité',
        }
