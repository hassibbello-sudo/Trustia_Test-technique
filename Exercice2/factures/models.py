from django.db import models
from django.utils import timezone

# ============================================================================
# MODÈLE 1 : PRODUIT
# ============================================================================
# Comme une fiche de produit dans un magasin
class Produit(models.Model):
    """
    Représente un produit avec :
    - id : identifiant unique (créé automatiquement)
    - nom : le nom du produit
    - prix : le prix en euros
    - date_peremption : quand le produit expire
    """
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()
    
    class Meta:
        ordering = ['-id']  # Afficher les plus récents en premier
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
    
    def __str__(self):
        return f"{self.nom} ({self.prix}€)"


# ============================================================================
# MODÈLE 2 : FACTURE
# ============================================================================
# Comme un reçu de magasin
class Facture(models.Model):
    """
    Représente une facture contenant :
    - id : identifiant unique
    - date_creation : quand la facture a été créée
    - produits : la liste des produits dans la facture
    """
    id = models.AutoField(primary_key=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit, through='LigneFacture')
    
    class Meta:
        ordering = ['-date_creation']  # Les plus récentes en premier
        verbose_name = "Facture"
        verbose_name_plural = "Factures"
    
    def __str__(self):
        return f"Facture #{self.id} - {self.date_creation.strftime('%d/%m/%Y')}"
    
    def total_produits(self):
        """Calcule le nombre total de produits"""
        return sum(ligne.quantite for ligne in self.lignefacture_set.all())
    
    def total_paye(self):
        """Calcule le total à payer"""
        return sum(ligne.total_ligne() for ligne in self.lignefacture_set.all())


# ============================================================================
# MODÈLE 3 : LIGNEFACTURE
# ============================================================================
# C'est l'intermédiaire entre Produit et Facture
# (Chaque produit peut avoir une quantité différente dans chaque facture)
class LigneFacture(models.Model):
    """
    Représente une ligne dans une facture :
    - produit : quel produit
    - facture : dans quelle facture
    - quantite : combien de ce produit
    """
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ('facture', 'produit')  # Un produit une seule fois par facture
    
    def __str__(self):
        return f"{self.produit.nom} x{self.quantite}"
    
    def total_ligne(self):
        """Calcule le total de cette ligne (prix x quantité)"""
        return self.produit.prix * self.quantite
