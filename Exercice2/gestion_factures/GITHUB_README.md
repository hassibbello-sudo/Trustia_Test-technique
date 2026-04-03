# 📋 Gestion Factures - Application Django

> Une application web complète de gestion de produits et de génération de factures, développée avec Django.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](#license)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](#)

## 📸 Aperçu

### Gestion des Produits
- ✅ CRUD complet (Créer, Afficher, Modifier, Supprimer)
- ✅ Pagination (5 produits par page)
- ✅ Recherche et filtrage
- ✅ Interface responsive

### Gestion des Factures
- ✅ Création de factures
- ✅ Ajout de produits avec quantités
- ✅ Calcul automatique des totaux
- ✅ Détail complet avec historique

## 🚀 Démarrage Rapide

### Prérequis
```bash
Python 3.8+
pip ou conda
```

### Installation

1. **Cloner le repository**
```bash
git clone https://github.com/votre-user/gestion-factures.git
cd gestion-factures
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Initialiser la base de données**
```bash
python manage.py migrate
python manage.py createsuperuser  # Créer un admin
```

5. **Charger les données de test (optionnel)**
```bash
python manage.py shell < scripts/load_test_data.py
```

6. **Lancer le serveur**
```bash
python manage.py runserver
```

7. **Accéder à l'application**
- **App** : http://127.0.0.1:8000
- **Admin** : http://127.0.0.1:8000/admin

## 📁 Structure du Projet

```
gestion-factures/
├── config/                  # Configuration Django
│   ├── settings.py         # Paramètres (INSTALLED_APPS, BD, etc)
│   ├── urls.py             # Routes principales
│   └── wsgi.py             # Interface WSGI
│
├── factures/                # Application principale
│   ├── models.py           # 3 modèles (Produit, Facture, LigneFacture)
│   ├── views.py            # 11 vues (logique métier)
│   ├── forms.py            # 3 formulaires avec validation
│   ├── urls.py             # Routes de l'app
│   ├── admin.py            # Configuration admin Django
│   │
│   ├── migrations/          # Versions de la BD
│   │   └── 0001_initial.py
│   │
│   └── templates/           # 13 templates HTML
│       ├── base.html
│       └── factures/
│           ├── produits/   (4 templates)
│           └── factures/   (8 templates)
│
├── static/                  # Fichiers statiques (CSS, JS, images)
├── manage.py               # Utilitaire Django
├── db.sqlite3              # Base de données
├── requirements.txt        # Dépendances Python
├── .gitignore              # Fichiers à ignorer
├── run.sh                  # Script de lancement
│
└── docs/                   # Documentation
    ├── README.md
    ├── INSTALLATION.md
    ├── EXPLICATIONS_ENFANT.md
    ├── TESTS.md
    ├── ENTRETIEN_TECHNIQUE.md
    ├── AMELIORATIONS.md
    └── ENVOI_TEST.md
```

## 💡 Fonctionnalités

### 🛒 Gestion des Produits
- **Créer** : Ajouter de nouveaux produits (nom, prix, date péremption)
- **Afficher** : Liste paginée de tous les produits
- **Modifier** : Éditer les informations d'un produit
- **Supprimer** : Supprimer un produit (avec confirmation)

### 📄 Gestion des Factures
- **Créer** : Créer une nouvelle facture
- **Ajouter produits** : Ajouter des produits avec quantités
- **Modifier quantités** : Ajuster les quantités
- **Voir détail** : Afficher la facture avec tous les produits et le total

### 📊 Fonctionnalités Avancées
- **Pagination** : Navigation fluide avec 5 éléments par page
- **Calculs automatiques** : Total et quantités calculés en temps réel
- **Validation** : Formulaires avec validation côté serveur
- **Responsive Design** : Interface adaptée à tous les appareils (Bootstrap 5)

## 🗄️ Modèles de Données

### Produit
```python
- id (AutoField)
- nom (CharField)
- prix (DecimalField)
- date_peremption (DateField)
```

### Facture
```python
- id (AutoField)
- date_creation (DateTimeField)
- produits (ManyToMany via LigneFacture)

Méthodes:
- total_produits() : Nombre total de produits
- total_paye() : Montant total à payer
```

### LigneFacture (Intermédiaire)
```python
- facture (ForeignKey)
- produit (ForeignKey)
- quantite (PositiveIntegerField)

Méthodes:
- total_ligne() : Prix × Quantité
```

## 🔧 Commandes Utiles

```bash
# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Accès à la console Django
python manage.py shell

# Créer un superuser
python manage.py createsuperuser

# Lancer les tests
python manage.py test

# Lancer le serveur
python manage.py runserver

# Lancer sur un port différent
python manage.py runserver 8001

# Collecte des fichiers statiques (production)
python manage.py collectstatic
```

## 📖 Documentation

La documentation complète se trouve dans le dossier `docs/` :

- **[INSTALLATION.md](docs/INSTALLATION.md)** - Instructions d'installation détaillées
- **[EXPLICATIONS_ENFANT.md](docs/EXPLICATIONS_ENFANT.md)** - Explications simples du code
- **[TESTS.md](docs/TESTS.md)** - 20+ tests à effectuer
- **[ENTRETIEN_TECHNIQUE.md](docs/ENTRETIEN_TECHNIQUE.md)** - Q&A pour l'entretien
- **[AMELIORATIONS.md](docs/AMELIORATIONS.md)** - 10 idées d'évolution future

## 🧪 Tests

Effectuer les tests listés dans `docs/TESTS.md` :

```bash
# Lancer tous les tests
python manage.py test factures

# Lancer avec détails
python manage.py test factures -v 2
```

## 📊 Points Forts

✅ **Respect des Contraintes**
- CRUD complet pour produits et factures
- Pagination fonctionnelle
- Calculs automatiques
- Stack Django + Python + HTML/CSS

✅ **Code Professionnel**
- Architecture clean (séparation Models/Views/Templates)
- Code lisible et commenté
- Gestion des erreurs
- Sécurité (CSRF tokens, validation)

✅ **Interface Moderne**
- Bootstrap 5
- Responsive design
- Messages de feedback
- Navigation intuitive

✅ **Documentation Exhaustive**
- 8 fichiers de documentation
- Explications détaillées
- Guides d'installation et de déploiement
- Q&A pour l'entretien technique

## 🚀 Déploiement

### Déploiement Simple avec Heroku

```bash
# 1. Créer requirements.txt
pip freeze > requirements.txt

# 2. Créer Procfile
echo "web: gunicorn config.wsgi" > Procfile

# 3. Installer gunicorn
pip install gunicorn

# 4. Déployer
heroku create mon-app-factures
git push heroku main
heroku run python manage.py migrate
```

### Autres plateformes
- **PythonAnywhere** : https://www.pythonanywhere.com
- **AWS** / **Azure** : Voir la documentation Django
- **DigitalOcean** : Droplets + Gunicorn + Nginx

## 🔐 Sécurité

- ✅ CSRF Protection avec tokens Django
- ✅ Validation des données avec formulaires
- ✅ Gestion des erreurs 404
- ✅ Authentification admin sécurisée
- ✅ Protection contre les injections SQL (ORM Django)

## 📝 Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

## 👤 Auteur

Test technique d'alternance - Avril 2025

## 🤝 Contribution

Les contributions sont bienvenues! Pour contribuer:

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 💬 Support

Pour toute question ou problème :
- Consulter la [documentation](docs/)
- Vérifier la section [INSTALLATION.md](docs/INSTALLATION.md#dépannage)
- Ouvrir une Issue sur GitHub

## 📈 Feuille de Route

### ✅ Fonctionnalités Implémentées
- CRUD Produits
- CRUD Factures
- Pagination
- Calculs automatiques
- Interface responsive
- Admin Django

### 🔄 Fonctionnalités Futures
- Authentification utilisateurs
- Génération de PDF
- Export Excel
- Graphiques de ventes
- API REST
- Notifications email

Voir [AMELIORATIONS.md](docs/AMELIORATIONS.md) pour la liste complète.

---

**Prêt à utiliser!** 🎉 Téléchargez, testez et déployez. Bonne chance! 🚀
