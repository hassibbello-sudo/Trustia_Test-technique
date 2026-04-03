from django.urls import path
from . import views

urlpatterns = [
    # ========== PAGE D'ACCUEIL ==========
    path('', views.liste_produits, name='accueil'),
    
    # ========== GESTION DES PRODUITS ==========
    # Afficher, créer, modifier, supprimer
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/creer/', views.creer_produit, name='creer_produit'),
    path('produits/<int:pk>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('produits/<int:pk>/supprimer/', views.supprimer_produit, name='supprimer_produit'),
    
    # ========== GESTION DES FACTURES ==========
    # Afficher, créer, voir détail, supprimer
    path('factures/', views.liste_factures, name='liste_factures'),
    path('factures/creer/', views.creer_facture, name='creer_facture'),
    path('factures/<int:pk>/', views.detail_facture, name='detail_facture'),
    path('factures/<int:pk>/supprimer/', views.supprimer_facture, name='supprimer_facture'),
    
    # ========== GESTION DES PRODUITS DANS UNE FACTURE ==========
    # Ajouter, modifier, supprimer un produit d'une facture
    path('factures/<int:facture_pk>/ajouter-produit/', views.ajouter_produit_facture, name='ajouter_produit_facture'),
    path('factures/<int:facture_pk>/produit/<int:ligne_pk>/modifier/', views.modifier_ligne_facture, name='modifier_ligne_facture'),
    path('factures/<int:facture_pk>/produit/<int:ligne_pk>/supprimer/', views.supprimer_ligne_facture, name='supprimer_ligne_facture'),
]
