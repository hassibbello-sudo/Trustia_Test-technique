from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Produit, Facture, LigneFacture
from .forms import ProduitForm, FactureForm, LigneFactureForm


# ============================================================================
# VUES DES PRODUITS
# ============================================================================

def liste_produits(request):
    """
    Affiche la liste de tous les produits avec pagination.
    Chaque page affiche 5 produits.
    """
    # Récupérer tous les produits
    tous_les_produits = Produit.objects.all()
    
    # Créer un paginator (5 produits par page)
    paginator = Paginator(tous_les_produits, 5)
    page_number = request.GET.get('page', 1)
    produits = paginator.get_page(page_number)
    
    return render(request, 'factures/produits/liste.html', {
        'produits': produits,
        'paginator': paginator,
    })


def creer_produit(request):
    """
    Permet de créer un nouveau produit.
    GET : affiche le formulaire
    POST : enregistre le produit
    """
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = form.save()
            messages.success(request, f"✅ Produit '{produit.nom}' créé avec succès !")
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    
    return render(request, 'factures/produits/creer.html', {'form': form})


def modifier_produit(request, pk):
    """
    Permet de modifier un produit existant.
    """
    produit = get_object_or_404(Produit, pk=pk)
    
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            produit = form.save()
            messages.success(request, f"✅ Produit '{produit.nom}' modifié avec succès !")
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    
    return render(request, 'factures/produits/modifier.html', {
        'form': form,
        'produit': produit
    })


def supprimer_produit(request, pk):
    """
    Supprime un produit (après confirmation).
    """
    produit = get_object_or_404(Produit, pk=pk)
    
    if request.method == 'POST':
        nom = produit.nom
        produit.delete()
        messages.success(request, f"✅ Produit '{nom}' supprimé avec succès !")
        return redirect('liste_produits')
    
    return render(request, 'factures/produits/confirmer_suppression.html', {
        'produit': produit
    })


# ============================================================================
# VUES DES FACTURES
# ============================================================================

def liste_factures(request):
    """
    Affiche la liste de toutes les factures avec pagination.
    Chaque page affiche 5 factures.
    """
    # Récupérer toutes les factures
    toutes_les_factures = Facture.objects.all()
    
    # Créer un paginator (5 factures par page)
    paginator = Paginator(toutes_les_factures, 5)
    page_number = request.GET.get('page', 1)
    factures = paginator.get_page(page_number)
    
    return render(request, 'factures/factures/liste.html', {
        'factures': factures,
        'paginator': paginator,
    })


def creer_facture(request):
    """
    Crée une nouvelle facture vide.
    """
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save()
            messages.success(request, f"✅ Facture #{facture.id} créée !")
            return redirect('detail_facture', pk=facture.pk)
    else:
        form = FactureForm()
    
    return render(request, 'factures/factures/creer.html', {'form': form})


def detail_facture(request, pk):
    """
    Affiche le détail d'une facture :
    - Liste des produits
    - Quantités
    - Total à payer
    """
    facture = get_object_or_404(Facture, pk=pk)
    lignes = LigneFacture.objects.filter(facture=facture)
    
    return render(request, 'factures/factures/detail.html', {
        'facture': facture,
        'lignes': lignes,
    })


def ajouter_produit_facture(request, facture_pk):
    """
    Ajoute un produit à une facture.
    """
    facture = get_object_or_404(Facture, pk=facture_pk)
    
    if request.method == 'POST':
        form = LigneFactureForm(request.POST)
        if form.is_valid():
            ligne = form.save(commit=False)
            ligne.facture = facture
            
            # Vérifier si le produit n'est pas déjà dans la facture
            try:
                ligne_existante = LigneFacture.objects.get(
                    facture=facture,
                    produit=ligne.produit
                )
                # Si existe, ajouter à la quantité
                ligne_existante.quantite += ligne.quantite
                ligne_existante.save()
                messages.info(request, "Quantité augmentée pour ce produit")
            except LigneFacture.DoesNotExist:
                # Sinon, créer une nouvelle ligne
                ligne.save()
                messages.success(request, f"✅ Produit ajouté à la facture !")
            
            return redirect('detail_facture', pk=facture.pk)
    else:
        form = LigneFactureForm()
    
    return render(request, 'factures/factures/ajouter_produit.html', {
        'form': form,
        'facture': facture
    })


def modifier_ligne_facture(request, facture_pk, ligne_pk):
    """
    Modifie la quantité d'un produit dans une facture.
    """
    facture = get_object_or_404(Facture, pk=facture_pk)
    ligne = get_object_or_404(LigneFacture, pk=ligne_pk, facture=facture)
    
    if request.method == 'POST':
        form = LigneFactureForm(request.POST, instance=ligne)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Quantité modifiée !")
            return redirect('detail_facture', pk=facture.pk)
    else:
        form = LigneFactureForm(instance=ligne)
    
    return render(request, 'factures/factures/modifier_produit.html', {
        'form': form,
        'facture': facture,
        'ligne': ligne
    })


def supprimer_ligne_facture(request, facture_pk, ligne_pk):
    """
    Supprime un produit d'une facture.
    """
    facture = get_object_or_404(Facture, pk=facture_pk)
    ligne = get_object_or_404(LigneFacture, pk=ligne_pk, facture=facture)
    
    if request.method == 'POST':
        produit_nom = ligne.produit.nom
        ligne.delete()
        messages.success(request, f"✅ {produit_nom} supprimé de la facture !")
        return redirect('detail_facture', pk=facture.pk)
    
    return render(request, 'factures/factures/confirmer_suppression_ligne.html', {
        'facture': facture,
        'ligne': ligne
    })


def supprimer_facture(request, pk):
    """
    Supprime une facture (après confirmation).
    """
    facture = get_object_or_404(Facture, pk=pk)
    
    if request.method == 'POST':
        facture_id = facture.id
        facture.delete()
        messages.success(request, f"✅ Facture #{facture_id} supprimée !")
        return redirect('liste_factures')
    
    return render(request, 'factures/factures/confirmer_suppression.html', {
        'facture': facture
    })
