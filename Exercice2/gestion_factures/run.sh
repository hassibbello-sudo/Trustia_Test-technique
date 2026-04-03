#!/bin/bash

# ============================================================================
# SCRIPT DE LANCEMENT - Application Gestion Factures
# ============================================================================

echo "🚀 Démarrage de l'application Gestion Factures..."
echo ""
echo "📋 Informations :"
echo "   - URL: http://127.0.0.1:8000"
echo "   - Admin: http://127.0.0.1:8000/admin"
echo "   - Identifiant: admin"
echo "   - Mot de passe: admin123"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo "-----------------------------------------------------------"
echo ""

cd "$(dirname "$0")" && python manage.py runserver
