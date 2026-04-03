# 🧪 Guide de Test - Gestion Factures

## ✅ Checklist de Test Technique

Utilisez ce guide pour tester toutes les fonctionnalités de l'application.

---

## 🚀 Démarrage de l'Application

```bash
cd gestion_factures
python manage.py runserver
```

**URL d'accès** : http://127.0.0.1:8000

---

## 📋 TEST 1 : AFFICHAGE DE LA LISTE DES PRODUITS

### ✅ À tester :
- [ ] La page s'affiche sans erreur
- [ ] 5 produits affichés (pagination)
- [ ] Les colonnes sont : ID, Nom, Prix, Date, Actions
- [ ] Les produits sont triés par ID décroissant (les plus récents en premier)
- [ ] Bouton "➕ Ajouter un produit" visible et cliquable
- [ ] Pagination visible si > 5 produits

### 📸 Résultat attendu :
```
┌─────────────────────────────────────────────┐
│ 📦 Gestion des Produits                     │
│ ➕ Ajouter un produit                        │
├─────────────────────────────────────────────┤
│ ID │ Nom            │ Prix │ Date │ Actions │
├─────────────────────────────────────────────┤
│ 7  │ Carottes       │ 1.50€│ ...  │ ✏️ 🗑️  │
│ 6  │ Tomates        │ 2.20€│ ...  │ ✏️ 🗑️  │
│ 5  │ Fraises        │ 5.00€│ ...  │ ✏️ 🗑️  │
└─────────────────────────────────────────────┘
Pagination: ⏮️ ⬅️ 1 2 ➡️ ⏭️
```

---

## 📋 TEST 2 : CRÉER UN PRODUIT

### ✅ À tester :
- [ ] Cliquer sur "➕ Ajouter un produit"
- [ ] Formulaire s'affiche avec 3 champs
- [ ] Champs : Nom du produit, Prix (€), Date de péremption
- [ ] Les champs ont des placeholder explicites
- [ ] Remplir les champs avec :
  - Nom: "Raisins"
  - Prix: 3.75
  - Date: 2025-06-15
- [ ] Cliquer "✅ Créer le Produit"
- [ ] Message de succès : "✅ Produit 'Raisins' créé avec succès !"
- [ ] Redirection automatique vers la liste des produits
- [ ] Le produit apparaît dans la liste

### ❌ À tester aussi (erreurs) :
- [ ] Laisser un champ vide → message d'erreur
- [ ] Mettre une lettre dans le prix → message d'erreur
- [ ] Mettre une date invalide → message d'erreur

---

## 📋 TEST 3 : MODIFIER UN PRODUIT

### ✅ À tester :
- [ ] Dans la liste, cliquer sur ✏️ (modifier)
- [ ] Le formulaire pré-remplit les données
- [ ] Modifier la valeur du prix (ex: 2.50 → 2.99)
- [ ] Cliquer "✅ Enregistrer les modifications"
- [ ] Message de succès
- [ ] Redirection vers la liste
- [ ] Le prix a changé dans la liste ✨

---

## 📋 TEST 4 : SUPPRIMER UN PRODUIT

### ✅ À tester :
- [ ] Dans la liste, cliquer sur 🗑️ (supprimer)
- [ ] Page de confirmation s'affiche
- [ ] Message : "Êtes-vous sûr de vouloir supprimer le produit 'XXX' ?"
- [ ] Deux boutons : "🗑️ Oui, supprimer" et "❌ Annuler"
- [ ] Cliquer "Oui"
- [ ] Message de succès
- [ ] Redirection vers la liste
- [ ] Le produit n'est plus dans la liste ✨

### ❌ À tester aussi :
- [ ] Cliquer "Annuler" → revenir à la liste, rien n'est supprimé

---

## 📋 TEST 5 : PAGINATION DES PRODUITS

### ✅ À tester :
- [ ] Page 1 affiche produits 1-5
- [ ] Cliquer "Suivante ➡️" → Page 2 affiche produits 6-7 (si 7 produits)
- [ ] Les boutons actifs/désactivés changent correctement
- [ ] Cliquer "⏮️ Première" → revenir à page 1
- [ ] Cliquer sur le numéro de page → aller directement à cette page

---

## 📋 TEST 6 : AFFICHAGE DE LA LISTE DES FACTURES

### ✅ À tester :
- [ ] Cliquer sur "📄 Factures" dans la navbar
- [ ] La page s'affiche sans erreur
- [ ] Les colonnes sont : ID, Date, Nombre produits, Total, Actions
- [ ] Au moins 1 facture visible (celle créée lors de l'initialisation)
- [ ] Bouton "➕ Créer une facture" visible
- [ ] Le total s'affiche correctement (ex: "16.10€")

---

## 📋 TEST 7 : CRÉER UNE FACTURE

### ✅ À tester :
- [ ] Cliquer sur "➕ Créer une facture"
- [ ] Page avec message "Une nouvelle facture vide va être créée"
- [ ] Cliquer "✅ Créer la Facture"
- [ ] Une nouvelle facture est créée
- [ ] Redirection automatique vers le détail de la facture
- [ ] La facture est vide (aucun produit)
- [ ] URL contient l'ID de la facture (ex: /factures/2/)

---

## 📋 TEST 8 : AJOUTER UN PRODUIT À UNE FACTURE

### ✅ À tester :
- [ ] Être sur la page détail d'une facture
- [ ] Cliquer "➕ Ajouter un produit"
- [ ] Formulaire s'affiche avec 2 champs :
  - Dropdown pour choisir un produit
  - Champ quantité (nombre)
- [ ] Choisir un produit (ex: "Pommes Gala")
- [ ] Entrer une quantité (ex: 5)
- [ ] Cliquer "✅ Ajouter à la facture"
- [ ] Le produit apparaît dans la tableau
- [ ] Le total s'affiche correctement

### 🧮 Vérification du calcul :
```
Pommes Gala = 2.50€
Quantité = 5
Sous-total = 2.50€ × 5 = 12.50€ ✅
```

---

## 📋 TEST 9 : DÉTAIL D'UNE FACTURE

### ✅ À tester :
- [ ] La facture affiche un tableau avec colonnes :
  - Produit
  - Prix unitaire
  - Quantité
  - Total (prix × quantité)
  - Actions (✏️ 🗑️)
- [ ] La partie "💰 Résumé" affiche :
  - Nombre de produits (somme des quantités)
  - Nombre de lignes (nombre de produits différents)
  - **Total à payer**
- [ ] Le total est calculé correctement
- [ ] La date de création s'affiche

### 📊 Exemple :
```
┌────────────────────────────────────────────────┐
│ 📋 Produits de la facture                      │
├────────────────────────────────────────────────┤
│ Produit    │ Prix  │ Quantité │ Total         │
├────────────────────────────────────────────────┤
│ Pommes     │ 2.50€ │    3     │ 7.50€         │
│ Bananes    │ 1.80€ │    2     │ 3.60€         │
│ Fraises    │ 5.00€ │    1     │ 5.00€         │
└────────────────────────────────────────────────┘

💰 Résumé :
Nombre de produits : 6
Nombre de lignes : 3
Total à payer : 16.10€ ✅
```

---

## 📋 TEST 10 : MODIFIER LA QUANTITÉ D'UN PRODUIT

### ✅ À tester :
- [ ] Sur le détail d'une facture, cliquer ✏️ (modifier)
- [ ] Le formulaire s'ouvre
- [ ] Le produit est affichés en lecture seule
- [ ] Le champ "Quantité" est pré-rempli
- [ ] Modifier la quantité (ex: 3 → 5)
- [ ] Cliquer "✅ Enregistrer"
- [ ] Message de succès
- [ ] Retour au détail de la facture
- [ ] La quantité a changé ✨
- [ ] Le total s'est recalculé automatiquement 🧮

---

## 📋 TEST 11 : SUPPRIMER UN PRODUIT D'UNE FACTURE

### ✅ À tester :
- [ ] Sur le détail d'une facture, cliquer 🗑️ (supprimer)
- [ ] Page de confirmation s'affiche
- [ ] Message : "Êtes-vous sûr de vouloir supprimer 'XXX' (x3)?"
- [ ] Cliquer "🗑️ Oui, supprimer"
- [ ] Message de succès
- [ ] Le produit disparaît du tableau
- [ ] Le total se recalcule ✨

---

## 📋 TEST 12 : SUPPRIMER UNE FACTURE

### ✅ À tester :
- [ ] Sur la liste des factures, cliquer 🗑️
- [ ] Page de confirmation s'affiche
- [ ] Message : "Êtes-vous sûr de vouloir supprimer la facture #X ?"
- [ ] Affiche le nombre de produits
- [ ] Cliquer "🗑️ Oui, supprimer"
- [ ] Message de succès
- [ ] Redirection vers la liste
- [ ] La facture n'est plus visible

---

## 📋 TEST 13 : AJOUTER DEUX FOIS LE MÊME PRODUIT

### ✅ À tester :
- [ ] Sur une facture, ajouter "Pommes" × 3
- [ ] Ajouter à nouveau "Pommes" × 2
- [ ] **Résultat attendu** : Quantité augmente à 5 (3 + 2)
- [ ] Message : "Quantité augmentée pour ce produit"
- [ ] Une seule ligne "Pommes" dans le tableau
- [ ] Pas deux lignes séparées

---

## 📋 TEST 14 : NAVIGATION

### ✅ À tester :
- [ ] Cliquer sur le logo "📋 Gestion Factures" (navbar) → accueil (liste produits)
- [ ] Cliquer "📦 Produits" → liste produits
- [ ] Cliquer "📄 Factures" → liste factures
- [ ] Sur un produit, cliquer "← Retour" ou lien de navigation
- [ ] Tous les liens fonctionnent sans erreur 404

---

## 📋 TEST 15 : MESSAGES DE FEEDBACK

### ✅ À tester :
- [ ] Création de produit → Message vert ✅
- [ ] Suppression → Message vert ✅
- [ ] Erreur formulaire → Message rouge ❌
- [ ] Messages disparaissent après 5 secondes (optionnel)
- [ ] Bouton ✕ sur les messages fonctionne

---

## 📋 TEST 16 : ADMIN DJANGO

### ✅ À tester :
- [ ] Aller sur http://127.0.0.1:8000/admin
- [ ] Login avec admin / admin123
- [ ] Voir "Produits" dans le menu
- [ ] Voir "Factures" dans le menu
- [ ] Cliquer sur Produits → voir tous les produits
- [ ] Cliquer sur un produit → voir les détails
- [ ] Cliquer sur Factures → voir toutes les factures
- [ ] Voir le détail avec les produits listés

---

## 📋 TEST 17 : RESPONSIVE DESIGN

### ✅ À tester sur PC (1920px) :
- [ ] Navigation bien organisée
- [ ] Tableau lisible en largeur
- [ ] Tous les boutons accessibles

### ✅ À tester sur Téléphone (375px) :
- [ ] Menu s'effondre (hamburger menu ☰)
- [ ] Tableau s'adapte (scrollable ou empilé)
- [ ] Boutons toujours accessibles
- [ ] Pas de débordement horizontal

---

## 📋 TEST 18 : CALCULS PRÉCIS

### 🧮 Tester les calculs :

**Cas 1** :
```
Facture avec:
  - Pommes: 2.50€ × 3 = 7.50€
  - Bananes: 1.80€ × 2 = 3.60€
  - Oranges: 3.00€ × 1 = 3.00€
  
Total attendu: 14.10€
Vérifier que c'est exactement 14.10€ ✅
```

**Cas 2** :
```
Vérifier la précision avec des décimales
Ex: 3.33€ × 3 = 9.99€
```

---

## 📋 TEST 19 : PAGINATION CORRECTE

### ✅ À tester :
- [ ] Page 1 affiche 5 produits (1-5)
- [ ] Page 2 affiche les produits 6-10 (ou moins si < 10 produits)
- [ ] Total des pages correct
- [ ] "1 sur 2" s'affiche (si 2 pages)
- [ ] Les boutons "Première" et "Dernière" activés/désactivés

---

## 📋 TEST 20 : VALIDATION DES FORMULAIRES

### ✅ À tester :
- [ ] Créer produit sans nom → erreur
- [ ] Créer produit avec prix négatif → erreur
- [ ] Créer produit avec date invalide → erreur
- [ ] Les messages d'erreur sont clairs et utiles
- [ ] Le formulaire garde les données valides

---

## 🧪 Cas Limites à Tester

### 1️⃣ Facture sans produits
```
Créer facture vide
Vérifier que le total affiche 0€
Ne pas crash si aucun produit
```

### 2️⃣ Très grande quantité
```
Ajouter 999 exemplaires du même produit
Vérifier que le calcul est correct
```

### 3️⃣ Très long nom de produit
```
Créer produit avec nom de 200 caractères
Vérifier que l'affichage ne crash pas
```

### 4️⃣ Deux utilisateurs simultanés
```
Ouvrir deux onglets
Créer facture dans l'un
Actualiser l'autre
Les données doivent être synchronisées
```

---

## 🎯 Résumé des Points d'Évaluation

```
✅ Modèles (Models)
  - [x] Produit avec id, nom, prix, date_peremption
  - [x] Facture avec date_creation
  - [x] LigneFacture pour quantités

✅ Fonctionnalités CRUD
  - [x] Créer produit
  - [x] Lire (afficher) produit
  - [x] Modifier produit
  - [x] Supprimer produit
  - [x] Créer facture
  - [x] Afficher facture
  - [x] Supprimer facture

✅ Pagination
  - [x] Liste des produits paginée (5/page)
  - [x] Liste des factures paginée (5/page)
  - [x] Navigation correcte (⏮️ ⬅️ 1 2 3 ➡️ ⏭️)

✅ Factures Avancées
  - [x] Ajouter produits à facture
  - [x] Modifier quantités
  - [x] Supprimer produits
  - [x] Calcul automatique total

✅ Interface
  - [x] HTML/CSS/Bootstrap
  - [x] Responsive design
  - [x] Messages de feedback
  - [x] Navigation intuitive

✅ Code Quality
  - [x] Code lisible et commenté
  - [x] Séparation Models/Views/Templates
  - [x] Sécurité CSRF tokens
  - [x] Validation des données
```

---

## 📊 Résultats

Une fois tous les tests passés ✅, l'application est **PRÊTE POUR LA SUBMISSION** ! 🎉

---

**Bonne chance pour votre test technique!** 🚀
