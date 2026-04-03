# 📋 Gestion Factures - Application Django

Une application web complète pour gérer des produits et générer des factures, built with Django.

## 📋 Fonctionnalités

### ✅ Gestion des Produits
- ✏️ Créer un produit (nom, prix, date de péremption)
- 👁️ Afficher la liste de tous les produits
- ✏️ Modifier un produit existant
- 🗑️ Supprimer un produit
- 📄 **Pagination**: 5 produits par page

### ✅ Gestion des Factures
- ➕ Créer une facture vide
- 👁️ Afficher la liste de toutes les factures
- 📄 **Pagination**: 5 factures par page
- 👁️ Voir le détail d'une facture avec tous les produits
- 🗑️ Supprimer une facture

### ✅ Gestion des Produits dans Factures
- ➕ Ajouter un produit à une facture
- 📊 Définir la quantité d'un produit
- ✏️ Modifier la quantité d'un produit
- 🗑️ Supprimer un produit d'une facture

### ✅ Détail d'une Facture
- 📋 Liste complète des produits
- 🔢 Nombre total de produits
- 💰 Total à payer (auto-calculé)
- 📊 Détail de chaque ligne (produit, prix unitaire, quantité, total)

---

## 🛠️ Stack Technique

```
Django 6.0         # Framework web Python
SQLite 3           # Base de données
Bootstrap 5        # CSS Framework
HTML5 / CSS3       # Markup et styling
Python 3.11+       # Langage
```

---

## 🚀 Démarrage Rapide

### 1️⃣ Installation

```bash
cd gestion_factures
pip install django
python manage.py migrate
```

### 2️⃣ Lancer le serveur

**Option A - Avec le script :**
```bash
./run.sh
```

**Option B - Directement :**
```bash
python manage.py runserver
```

### 3️⃣ Accès à l'application

- **Application** : http://127.0.0.1:8000
- **Admin Django** : http://127.0.0.1:8000/admin
- **Login admin** : `admin` / `admin123`

---

## 📁 Structure du Projet

```
gestion_factures/
├── config/                           # Configuration Django
│   ├── settings.py                   # Paramètres (INSTALLED_APPS, BD, etc.)
│   ├── urls.py                       # Routes principales
│   └── wsgi.py                       # Interface WSGI
│
├── factures/                         # Application principale
│   ├── models.py                     # Modèles BD (Produit, Facture, LigneFacture)
│   ├── views.py                      # Logique métier (vues)
│   ├── forms.py                      # Formulaires Django
│   ├── urls.py                       # Routes de l'app
│   ├── admin.py                      # Configuration admin Django
│   │
│   ├── migrations/                   # Versions de la BD
│   │   └── 0001_initial.py
│   │
│   └── templates/                    # Templates HTML
│       ├── base.html                 # Template de base (navigation)
│       └── factures/
│           ├── produits/
│           │   ├── liste.html        # Liste des produits
│           │   ├── creer.html        # Créer un produit
│           │   ├── modifier.html     # Modifier un produit
│           │   └── confirmer_suppression.html
│           │
│           └── factures/
│               ├── liste.html        # Liste des factures
│               ├── creer.html        # Créer une facture
│               ├── detail.html       # Détail d'une facture
│               ├── ajouter_produit.html
│               ├── modifier_produit.html
│               └── confirmer_suppression*.html
│
├── manage.py                         # Utilitaire Django
├── db.sqlite3                        # Base de données (créée après migrate)
├── run.sh                            # Script de lancement
└── README.md                         # Cette documentation
```

---

## 🗄️ Modèles de Données

### 1️⃣ Produit
```python
class Produit:
    - id (AutoField)          # Identifiant unique
    - nom (CharField)         # Nom du produit
    - prix (DecimalField)     # Prix en euros
    - date_peremption (DateField)  # Date de péremption
```

### 2️⃣ Facture
```python
class Facture:
    - id (AutoField)                # Identifiant unique
    - date_creation (DateTimeField) # Date/heure de création
    - produits (ManyToMany)         # Relation vers Produit via LigneFacture
    
    Méthodes:
    - total_produits()              # Nombre total de produits
    - total_paye()                  # Montant total à payer
```

### 3️⃣ LigneFacture (Intermédiaire)
```python
class LigneFacture:
    - facture (ForeignKey)  # Lien vers Facture
    - produit (ForeignKey)  # Lien vers Produit
    - quantite (Integer)    # Quantité du produit
    
    Méthodes:
    - total_ligne()         # Prix x Quantité
```

---

## 🔍 Explications pour Enfants

### Imagine un magasin... 🏪

**Les Produits** 📦
- C'est comme les articles sur les étagères
- Chacun a un nom (ex: "Pommes"), un prix, une date limite

**Les Factures** 📄
- C'est comme ta liste d'achat à la caisse
- Tu mets dedans les produits que tu veux acheter

**Les Quantités** 🔢
- Si tu veux 3 pommes et 2 bananes, c'est la quantité
- La facture te calcule automatiquement le total!

**La Pagination** 📖
- Avec 1000 produits, c'est difficile d'afficher tout!
- Django les divise en pages (5 par page)
- Tu navigues avec "Suivante" et "Précédente"

---

## 📝 Fonctionnalités Clés Expliquées

### ✅ Pagination
```html
Chaque liste affiche 5 éléments par page
Boutons: ⏮️ Première | ⬅️ Précédente | 1 2 3 | Suivante ➡️ | Dernière ⏭️
```

### ✅ Calcul Automatique
```
Total d'une ligne = Prix unitaire × Quantité
Total facture = Somme de tous les totaux des lignes
```

### ✅ Relations Complexes
```
Une facture peut contenir PLUSIEURS produits
Un produit peut être dans PLUSIEURS factures
(Mais chaque produit une seule fois par facture)
```

### ✅ Messages de Feedback
```
✅ Produit 'Pommes' créé avec succès !
⚠️ Confirmez avant de supprimer
```

---

## 🎯 Cas d'Usage Pratiques

### Créer un produit
1. Aller à **📦 Produits** → **➕ Ajouter un produit**
2. Remplir : Nom, Prix, Date péremption
3. Cliquer **✅ Créer le Produit**

### Créer une facture
1. Aller à **📄 Factures** → **➕ Créer une facture**
2. La facture est créée vide
3. Cliquer sur la facture pour voir le détail
4. Cliquer **➕ Ajouter un produit**
5. Choisir un produit et sa quantité
6. Le total s'affiche automatiquement! 💰

### Modifier une facture
1. Aller au détail de la facture
2. Pour modifier la quantité : cliquer sur **✏️**
3. Pour supprimer un produit : cliquer sur **🗑️**

---

## 🔐 Admin Django

L'admin Django permet de :
- Voir et modifier les données directement
- Trier, filtrer les produits/factures
- Ajouter/supprimer en masse
- **URL** : http://127.0.0.1:8000/admin
- **Login** : admin / admin123

---

## 📊 Données de Test

Des données de test sont pré-chargées :

**Produits** :
- Pommes Gala (2.50€)
- Bananes (1.80€)
- Oranges Valencia (3.00€)
- Raisin blanc (4.50€)
- Fraises (5.00€)
- Tomates (2.20€)
- Carottes (1.50€)

**Facture** :
- Facture #1 avec 6 produits = 16.10€

---

## 🛠️ Commandes Utiles

```bash
# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Accès à la console Python avec la BD
python manage.py shell

# Créer un superuser
python manage.py createsuperuser

# Vider la BD
python manage.py flush

# Tester l'application
python manage.py test

# Lancer le serveur
python manage.py runserver
```

---

## ✨ Points Forts du Code

✅ **Séparation des préoccupations**
- Models = BD
- Views = Logique
- Forms = Validation
- Templates = Affichage

✅ **DRY (Don't Repeat Yourself)**
- Template de base réutilisé partout
- Modèles avec méthodes pour les calculs

✅ **Sécurité**
- CSRF tokens sur tous les formulaires
- Validation des données
- Pagination pour éviter les surcharges

✅ **Scalabilité**
- Facile d'ajouter des champs aux produits
- Facile de créer de nouvelles pages
- Base de données flexible

---

## 🚨 Dépannage

### La page 404 apparaît
```
Vérifier que vous êtes sur http://127.0.0.1:8000 (pas /admin)
```

### "Template not found"
```
Vérifier le dossier factures/templates/ existe
```

### "No Produit matches the given query"
```
Créer un produit d'abord dans Produits
```

### Port 8000 déjà utilisé
```bash
python manage.py runserver 8001  # Utiliser le port 8001
```

---

## 📚 Documentation

- Django Official: https://docs.djangoproject.com/
- Django Models: https://docs.djangoproject.com/en/6.0/topics/db/models/
- Django Views: https://docs.djangoproject.com/en/6.0/topics/http/views/
- Django Templates: https://docs.djangoproject.com/en/6.0/topics/templates/

---

## 🎓 Test Technique - Critères Évalués

✅ **Modèles**
- [x] Produit avec id, nom, prix, date_peremption
- [x] Facture avec date_creation et relation aux produits
- [x] LigneFacture pour gérer les quantités

✅ **Fonctionnalités CRUD**
- [x] Créer/Modifier/Supprimer/Afficher produits
- [x] Créer/Supprimer/Afficher factures

✅ **Pagination**
- [x] Listes paginées (5 éléments par page)

✅ **Calculs**
- [x] Total produits par facture
- [x] Total à payer

✅ **Interface**
- [x] HTML/CSS/Bootstrap moderne
- [x] Formulaires avec validation
- [x] Messages de feedback

---

## 👤 Auteur

Créé pour le test technique d'alternance

---

## 📝 License

MIT - Libre d'utilisation et de modification

---

**🎉 Bonne chance pour votre alternance !**
