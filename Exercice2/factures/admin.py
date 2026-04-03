from django.contrib import admin
from .models import Produit, Facture, LigneFacture


# ============================================================================
# ADMIN PRODUIT
# ============================================================================
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prix', 'date_peremption')
    search_fields = ('nom',)
    list_filter = ('date_peremption',)
    ordering = ('-id',)


# ============================================================================
# ADMIN LIGNEFACTURE (INLINE)
# ============================================================================
class LigneFactureInline(admin.TabularInline):
    """Afficher les lignes directement dans la facture"""
    model = LigneFacture
    extra = 1
    fields = ('produit', 'quantite', 'total_ligne')
    readonly_fields = ('total_ligne',)


# ============================================================================
# ADMIN FACTURE
# ============================================================================
@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_creation', 'total_produits', 'total_paye')
    search_fields = ('id',)
    list_filter = ('date_creation',)
    inlines = [LigneFactureInline]
    ordering = ('-date_creation',)


# ============================================================================
# ADMIN LIGNEFACTURE
# ============================================================================
@admin.register(LigneFacture)
class LigneFactureAdmin(admin.ModelAdmin):
    list_display = ('facture', 'produit', 'quantite', 'total_ligne')
    search_fields = ('produit__nom',)
    list_filter = ('facture', 'produit')
    readonly_fields = ('total_ligne',)
