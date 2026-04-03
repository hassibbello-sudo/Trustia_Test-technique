# 🚀 Guide Installation & Déploiement

## 📋 Table des Matières
1. [Installation Locale](#installation-locale)
2. [Lancer l'Application](#lancer-lapplication)
3. [Structure des Fichiers](#structure-des-fichiers)
4. [Dépannage](#dépannage)
5. [Déploiement](#déploiement)

---

## Installation Locale

### Prérequis
```
- Python 3.8+
- pip (gestionnaire de paquets Python)
- Navigateur web moderne
```

### Étape 1 : Télécharger et Extraire
```bash
# Si vous avez un ZIP
unzip gestion_factures.zip
cd gestion_factures

# Ou cloner depuis Git
git clone <url-du-repo>
cd gestion_factures
```

### Étape 2 : Installer Django
```bash
# Installation simple
pip install django

# Ou avec requirements.txt (si créé)
pip install -r requirements.txt
```

### Étape 3 : Initialiser la Base de Données
```bash
# Créer les migrations (structure BD)
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate
```

### Étape 4 : Créer un Super-Utilisateur (Admin)
```bash
python manage.py createsuperuser
# Suivre les prompts:
# Nom d'utilisateur: admin
# Email: admin@example.com
# Mot de passe: admin123
```

### Étape 5 : Charger les Données de Test (Optionnel)
```bash
python manage.py shell
```

Puis dans le shell:
```python
from factures.models import Produit, Facture, LigneFacture
from datetime import datetime, timedelta

# Créer des produits de test
produits_data = [
    {'nom': 'Pommes', 'prix': 2.50, 'date_peremption': (datetime.now() + timedelta(days=30)).date()},
    {'nom': 'Bananes', 'prix': 1.80, 'date_peremption': (datetime.now() + timedelta(days=20)).date()},
]

for data in produits_data:
    Produit.objects.create(**data)

print("✅ Données créées!")
```

---

## Lancer l'Application

### Option 1 : Script de Lancement (Recommandé)
```bash
./run.sh
```

### Option 2 : Commande Directe
```bash
python manage.py runserver
```

### Option 3 : Lancer sur un Port Différent
```bash
python manage.py runserver 8001
# Accès: http://127.0.0.1:8001
```

### Option 4 : Lancer pour Accès Réseau
```bash
python manage.py runserver 0.0.0.0:8000
# Accessible depuis d'autres machines via http://<votre-ip>:8000
```

---

## Structure des Fichiers

### Fichiers Importants

```
gestion_factures/
│
├── manage.py
│   └── Utilitaire principal Django
│       Usage: python manage.py <commande>
│
├── db.sqlite3
│   └── Base de données SQLite
│       ⚠️ Ne pas commiter sur Git
│       ⚠️ Contient toutes les données
│
├── config/
│   ├── settings.py
│   │   └── Configuration globale Django
│   │       - INSTALLED_APPS (quelles apps activer)
│   │       - DATABASES (connexion BD)
│   │       - MIDDLEWARE (filtres de requête)
│   │       - TEMPLATES (localisation HTML)
│   │
│   ├── urls.py
│   │   └── Routage global
│   │       Inclut les URLs de l'app factures
│   │
│   └── wsgi.py
│       └── Interface serveur (production)
│
├── factures/
│   ├── models.py
│   │   └── 3 modèles:
│   │       - Produit
│   │       - Facture
│   │       - LigneFacture
│   │
│   ├── views.py
│   │   └── 11 fonctions (logique métier)
│   │       - liste_produits()
│   │       - creer_produit()
│   │       - modifier_produit()
│   │       - supprimer_produit()
│   │       - liste_factures()
│   │       - etc...
│   │
│   ├── forms.py
│   │   └── 3 formulaires
│   │       - ProduitForm
│   │       - FactureForm
│   │       - LigneFactureForm
│   │
│   ├── urls.py
│   │   └── Routage de l'app (11 routes)
│   │
│   ├── admin.py
│   │   └── Configuration interface admin
│   │       Enregistrement des modèles
│   │
│   ├── apps.py
│   │   └── Configuration de l'app
│   │
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   │   └── Création initiale des tables
│   │   │
│   │   └── __init__.py
│   │
│   └── templates/
│       ├── base.html
│       │   └── Template de base (navbar, footer)
│       │
│       └── factures/
│           ├── produits/
│           │   ├── liste.html (afficher tous)
│           │   ├── creer.html (formulaire création)
│           │   ├── modifier.html (formulaire modification)
│           │   └── confirmer_suppression.html
│           │
│           └── factures/
│               ├── liste.html
│               ├── creer.html
│               ├── detail.html (voir facture + produits)
│               ├── ajouter_produit.html
│               ├── modifier_produit.html
│               ├── confirmer_suppression_ligne.html
│               └── confirmer_suppression.html
│
├── static/ (optionnel)
│   ├── css/
│   ├── js/
│   └── images/
│
├── run.sh
│   └── Script de lancement
│
├── README.md
│   └── Documentation principale
│
├── EXPLICATIONS_ENFANT.md
│   └── Explications simplifiées
│
└── TESTS.md
    └── Checklist de test
```

---

## Dépannage

### ❌ Erreur : "No module named 'django'"

**Solution** :
```bash
pip install django
```

### ❌ Erreur : "ModuleNotFoundError: No module named 'factures'"

**Solutions** :
```bash
# Vérifier que 'factures' est dans INSTALLED_APPS
grep "factures" config/settings.py

# Vérifier la structure des dossiers
ls factures/
# Doit contenir: models.py, views.py, forms.py, etc.
```

### ❌ Erreur : "OperationalError: no such table"

**Solution** :
```bash
# La BD n'est pas initialisée
python manage.py migrate
```

### ❌ Erreur : "TemplateDoesNotExist"

**Solution** :
```bash
# Vérifier le chemin des templates
ls factures/templates/factures/produits/

# Vérifier settings.py
grep TEMPLATES config/settings.py
```

### ❌ Port 8000 déjà utilisé

**Solution** :
```bash
# Utiliser un autre port
python manage.py runserver 8001

# Ou trouver quel processus utilise le port
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows
```

### ❌ Admin ne fonctionne pas

**Solution** :
```bash
# Créer un superuser
python manage.py createsuperuser

# Ou en ligne de commande
python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
>>> exit()
```

### ❌ Données de test non chargées

**Solution** :
```bash
python manage.py shell < init_data.py
```

---

## Déploiement

### Déploiement Simple (Heroku)

#### 1️⃣ Créer un compte Heroku
```bash
# Installer Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

heroku login
```

#### 2️⃣ Créer requirements.txt
```bash
pip freeze > requirements.txt
```

#### 3️⃣ Créer Procfile
```bash
echo "web: gunicorn config.wsgi" > Procfile
```

#### 4️⃣ Installer gunicorn
```bash
pip install gunicorn
pip freeze > requirements.txt
```

#### 5️⃣ Déployer
```bash
heroku create mon-app-factures
git push heroku main
heroku run python manage.py migrate
```

### Déploiement PythonAnywhere

1. Créer compte sur https://www.pythonanywhere.com
2. Uploader les fichiers
3. Configurer l'application
4. Accéder via https://monapp.pythonanywhere.com

### Déploiement AWS/Azure

Nécessite plus de configuration avancée. Consulter la documentation Django.

---

## Variables d'Environnement

Pour la production, créer un fichier `.env` :

```bash
# .env
SECRET_KEY=votre-clé-secrète
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

Puis modifier `settings.py` :

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
```

---

## Commandes Utiles

### Gestion de la BD

```bash
# Voir l'état des migrations
python manage.py showmigrations

# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Vider la BD (ATTENTION!)
python manage.py flush

# Sauvegarder les données
python manage.py dumpdata > backup.json

# Restaurer les données
python manage.py loaddata backup.json
```

### Gestion des Utilisateurs

```bash
# Créer un superuser
python manage.py createsuperuser

# Lister les utilisateurs
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> exit()

# Changer le mot de passe
python manage.py changepassword admin
```

### Tests

```bash
# Lancer tous les tests
python manage.py test

# Lancer les tests d'une app
python manage.py test factures

# Avec plus de détails
python manage.py test factures -v 2
```

### Autres

```bash
# Vérifier la configuration
python manage.py check

# Collecte des fichiers statiques (production)
python manage.py collectstatic

# Créer un fichier dump SQL
python manage.py dumpdata > dump.json
```

---

## Fichiers à Ignorer (.gitignore)

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# Django
db.sqlite3
*.log
*.pot
/media/
/static/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environnement
.env
.env.local
```

---

## Production Checklist

- [ ] `DEBUG = False` dans settings.py
- [ ] `SECRET_KEY` unique et sécurisé
- [ ] `ALLOWED_HOSTS` configuré
- [ ] HTTPS activé
- [ ] Base de données PostgreSQL (pas SQLite)
- [ ] Fichiers statiques collectés
- [ ] Logs configurés
- [ ] Sauvegardes BD automatisées
- [ ] CSRF et sécurité activés
- [ ] Dépendances pinées (requirements.txt)

---

## Support

Si vous rencontrez des problèmes :

1. **Documentation Django** : https://docs.djangoproject.com/
2. **Stack Overflow** : Chercher votre erreur sur SO
3. **Django Discord** : Community support
4. **ChatGPT** : "Django [votre erreur]"

---

**✅ Vous êtes prêt à déployer votre application !** 🎉
