# 🐙 Guide GitHub - Créer votre Repository Public

## Étape 1: Créer un Compte GitHub (si pas encore)

1. Aller sur https://github.com
2. Cliquer sur "Sign up"
3. Créer votre compte (username, email, password)
4. Vérifier votre email
5. ✅ Vous êtes prêt!

---

## Étape 2: Créer un Nouveau Repository

### Via le Site GitHub

1. Connectez-vous à GitHub
2. Cliquer sur le **"+"** en haut à droite
3. Sélectionner **"New repository"**

### Configuration du Repository

```
Repository name: gestion-factures
Description: Application Django de gestion de produits et factures
Visibility: PUBLIC (⭐ Important pour le test technique!)
```

### Options à Cocher
- ✅ Add a README file
- ✅ Add .gitignore (choisir Python)
- ✅ Choose a license (MIT recommandé)

4. Cliquer **"Create repository"**

---

## Étape 3: Cloner et Configurer Localement

### Copier votre Repository

```bash
# Sur la page GitHub de votre repo, cliquer le bouton vert "Code"
# Copier l'URL HTTPS (ou SSH si configuré)
# Par exemple: https://github.com/votre-username/gestion-factures.git
```

### Cloner le Repository

```bash
cd /home/claude
git clone https://github.com/votre-username/gestion-factures.git
cd gestion-factures
```

---

## Étape 4: Copier les Fichiers du Projet

```bash
# Copier tous les fichiers Django dans le repository cloné
cp -r /home/claude/gestion_factures/* /home/claude/gestion-factures/

# Vérifier que tout est là
ls -la /home/claude/gestion-factures/
# Doit montrer: config/, factures/, manage.py, db.sqlite3, etc.
```

---

## Étape 5: Configurer Git Localement

```bash
cd /home/claude/gestion-factures

# Configurer votre identité Git
git config user.name "Votre Nom"
git config user.email "votre-email@example.com"

# Vérifier la configuration
git config --list
```

---

## Étape 6: Faire le Premier Commit

```bash
# Ajouter tous les fichiers
git add .

# Vérifier les changements
git status

# Commiter
git commit -m "Initial commit: Application Django gestion factures"

# Vérifier le commit
git log --oneline
```

---

## Étape 7: Pousser vers GitHub

```bash
# Envoyer les fichiers vers GitHub
git push -u origin main

# (Ou 'master' si c'est votre branche par défaut)
# Vous devrez peut-être entrer vos identifiants GitHub
```

### Si Erreur d'Authentification

#### Avec Token (Recommandé)

```bash
# Générer un token sur GitHub:
# 1. Settings → Developer settings → Personal access tokens
# 2. Generate new token
# 3. Cocher "repo" et "admin:repo_hook"
# 4. Copier le token

# Utiliser le token comme password lors du push
git push -u origin main
# Username: votre-username
# Password: [Coller le token]
```

#### Avec SSH (Avancé)

```bash
# Générer une clé SSH
ssh-keygen -t ed25519 -C "votre-email@example.com"

# Ajouter la clé à l'agent SSH
ssh-add ~/.ssh/id_ed25519

# Copier la clé publique
cat ~/.ssh/id_ed25519.pub

# Sur GitHub: Settings → SSH and GPG keys → New SSH key
# Coller la clé et confirmer

# Puis pousser avec SSH
git remote set-url origin git@github.com:votre-username/gestion-factures.git
git push -u origin main
```

---

## Étape 8: Vérifier sur GitHub

1. Aller sur https://github.com/votre-username/gestion-factures
2. Vérifier que tous les fichiers sont visibles
3. Vérifier que le repository est PUBLIC ✅

---

## Étape 9: Ajouter un README Professionnel

Remplacer le contenu du README.md par celui-ci:

```markdown
# 📋 Gestion Factures - Application Django

> Une application web complète de gestion de produits et de génération de factures.

## 🚀 Démarrage Rapide

### Installation
\`\`\`bash
git clone https://github.com/votre-username/gestion-factures.git
cd gestion-factures
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
\`\`\`

### Accès
- App: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin (admin/admin123)

## ✨ Fonctionnalités

- ✅ CRUD Produits complet
- ✅ Gestion des Factures
- ✅ Pagination (5 éléments/page)
- ✅ Calculs automatiques
- ✅ Interface responsive

## 📁 Structure

\`\`\`
gestion-factures/
├── config/          # Configuration Django
├── factures/        # Application
├── manage.py        # Utilitaire Django
├── db.sqlite3       # Base de données
└── requirements.txt # Dépendances
\`\`\`

## 📖 Documentation

- [INSTALLATION.md](INSTALLATION.md)
- [EXPLICATIONS_ENFANT.md](EXPLICATIONS_ENFANT.md)
- [TESTS.md](TESTS.md)
- [ENTRETIEN_TECHNIQUE.md](ENTRETIEN_TECHNIQUE.md)

## 🧪 Tests

\`\`\`bash
python manage.py test factures
\`\`\`

## 📝 Licence

MIT License
```

Puis pousser les changements:

```bash
git add README.md
git commit -m "Update README"
git push
```

---

## Étape 10: Renommer la Branche (Optionnel)

Si vous voulez utiliser `main` au lieu de `master`:

```bash
git branch -M main
git push -u origin main
```

---

## Commandes Git Courantes

### Après Modifications Locales

```bash
# Voir les fichiers modifiés
git status

# Ajouter tous les fichiers
git add .

# Ou ajouter fichier par fichier
git add fichier.py

# Commiter avec message
git commit -m "Description des changements"

# Pousser vers GitHub
git push

# Vérifier l'historique
git log --oneline
```

### Créer des Branches (Optionnel)

```bash
# Créer une branche
git checkout -b feature/amelioration-1

# Faire des changements et commits...

# Pousser la branche
git push -u origin feature/amelioration-1

# Retour à main
git checkout main
```

---

## ⚡ Raccourci: Tous les Commits d'Affilée

```bash
# Exécuter cette suite de commandes:
cd /home/claude/gestion-factures
git add .
git commit -m "Initial commit: Gestion Factures"
git push -u origin main

# Vérifier sur GitHub: https://github.com/votre-username/gestion-factures
```

---

## 🎯 Checklist Finale

- [ ] Repository créé sur GitHub
- [ ] Repository est PUBLIC
- [ ] Cloned localement
- [ ] Tous les fichiers ajoutés
- [ ] Premier commit poussé
- [ ] README.md professionnel
- [ ] Lien copié: https://github.com/votre-username/gestion-factures

---

## 📧 Envoyer le Lien à votre Entreprise

Une fois que le repository est prêt et public:

```
Objet: Submission - Test Technique Gestion Factures

Bonjour,

Vous trouverez mon test technique à cette adresse:
https://github.com/votre-username/gestion-factures

Le repository contient:
✅ Code source complet
✅ Base de données SQLite
✅ Documentation exhaustive
✅ Guide d'installation
✅ Tests à effectuer
✅ Guide d'entretien technique

L'application est prête à être clonée et lancée.

Cordialement,
[Votre Nom]
[Votre Téléphone]
[Votre Email]
```

---

## 🚨 Attention: Les Fichiers Sensibles

### ⚠️ NE PAS commiter:
- `venv/` (environnement virtuel)
- `__pycache__/` (fichiers compilés)
- `.env` (variables sensibles)
- Fichiers de log

✅ Ils sont ignorés par `.gitignore`

---

## 🎉 Bravo!

Vous avez maintenant un repository public professionnel sur GitHub! 🚀

Points positifs pour votre recruteur:
✅ Utilisation correcte de Git
✅ Repository public et accessible
✅ Code bien organisé
✅ Documentation complète
✅ Prêt pour le clone et le test

---

**Besoin d'aide?**
- Consulter: https://docs.github.com/
- GitHub est très bien documenté!

Bonne chance! 🎓
