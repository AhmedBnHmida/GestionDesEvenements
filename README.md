🎯 GestionDesEvenements - Application de Gestion d'Événements
Une application web Django complète pour la gestion d'événements avec frontoffice et backoffice.

📋 Description du Projet
L'objectif de cet atelier est de développer une application web de gestion des évènements en utilisant le Framework Django pour les deux parties FrontOffice et BackOffice.

🏗️ Architecture
Projet Django : GestionDesEvenements

Applications :

Event - Gestion des événements

Person - Gestion des utilisateurs et organisateurs

📊 Modèle de Données
Ce projet est basé sur le diagramme de classe d'analyse fourni.

Event
id - Identifiant unique

title - Titre de l'événement

description - Description détaillée (TextField)

image - Image de l'événement (ImageField avec Pillow)

category - Catégorie (Musique, Cinéma, Sport)

state - État de l'événement (booléen, default=False)

nbe_participant - Nombre de participants

evt_date - Date de l'événement

creation_date - Date de création

update_date - Date de mise à jour

Person
cin - Carte d'identité nationale (8 caractères, clé primaire)

email - Adresse email (doit se terminer par @esprit.tn)

Participation
participation_date - Date de participation (valeur par défaut: date système)

🚀 Installation et Démarrage
Prérequis
Python 3.11+

Django 4.2

1. Environnement Virtuel
bash
# Création de l'environnement virtuel
python -m venv djangoenv

# Activation (Windows)
djangoenv\Scripts\activate

# Vérification de l'activation (vous devriez voir (djangoenv) devant votre prompt)
(djangoenv) PS C:\5TWIN5\django\GestionDesEvenements>
2. Installation des Dépendances
bash
# Installation de Django
pip install Django==4.2

# Installation de Pillow pour gérer les images
pip install Pillow

# Vérification de l'installation
python -m django --version
3. Configuration du Projet
bash
# Migrations de la base de données
python manage.py makemigrations
python manage.py migrate

# Création du superutilisateur
python manage.py createsuperuser
4. Lancement du Serveur
bash
python manage.py runserver
Accédez à l'application : http://127.0.0.1:8000/

👑 Administration Django
Accès à l'Interface d'Administration
URL Admin : http://127.0.0.1:8000/admin/

Superutilisateur créé :

Username: admin

Email: admin@gmail.com

Password: admin123

Fonctionnalités Back-Office Implémentées
🔧 Administration des Personnes
Recherche par username avec ResearchPerson et search_fields=['username']

Gestion complète des profils

🎯 Administration des Événements
Affichage personnalisé avec list_display

Fonction de comptage des participants

Champs en lecture seule : creation_date et update_date

Pagination avec list_per_page = 10

Filtres avancés :

Par titre d'événement

Par nombre de participants ("No participants", "There are participants")

Par date ("Past Events", "Upcoming Events", "Today Events")

Actions personnalisées : "Accepter/Refuser" les événements

Formulaire organisé avec fieldsets

Inline des participations avec ParticipationAdmin (TabularInline)

Auto-complete pour la sélection des organisateurs avec autocomplete_fields=['organizer']

📁 Structure du Projet
text
GestionDesEvenements/
├── doc/                           # Documentation complète
│   ├── 1_Document.pdf
│   ├── 2_Etude_de_cas_Generation_de_la_BD.pdf
│   ├── 3_Etude_de_cas_Dashboard_Admin.pdf
│   ├── 1ere_etape_environnement_de_developpement.pdf
│   ├── 2eme_etape_installation_de_Django.pdf
│   └── 3eme_etape_creation_d_une_application.pdf
├── djangoenv/                     # Environnement virtuel
├── Event/                         # Application Event
│   ├── migrations/
│   ├── admin.py                   # Configuration admin personnalisée
│   ├── models.py                  # Modèles Event et Participation
│   └── ...
├── Person/                        # Application Person
│   ├── migrations/
│   ├── admin.py                   # Administration des personnes
│   ├── models.py                  # Modèle Person
│   └── ...
├── GestionDesEvenements/          # Projet Django principal
│   ├── settings.py                # Configuration avec nom de BD personnalisé
│   ├── urls.py                    # Routes URLs
│   └── ...
├── images/                        # Dossier pour les images uploadées
├── 5TWINSDIANGO.db               # Base de données (nom de classe personnalisé)
├── db.sqlite3                     # Base de données SQLite
├── manage.py                      # Script de gestion Django
└── README.md                      # Documentation principale
📚 Documentation
La documentation détaillée est disponible dans le dossier doc/ :

1_Document.pdf - Présentation générale du projet

2_Etude_de_cas_Generation_de_la_BD.pdf - Génération de la base de données et modèles

3_Etude_de_cas_Dashboard_Admin.pdf - Configuration du Back-Office et administration

1ere_etape_environnement_de_developpement.pdf - Environnement virtuel

2eme_etape_installation_de_Django.pdf - Installation de Django

3eme_etape_creation_d_une_application.pdf - Création des applications

🔧 Développement
Commandes Django utiles :

bash
# Créer les migrations
python manage.py makemigrations Event
python manage.py makemigrations Person

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur de développement
python manage.py runserver

# Lancer le serveur sur un port spécifique
python manage.py runserver 8080
✅ État du Projet
✅ Environnement de développement configuré

✅ Modèles de données implémentés avec toutes les contraintes

✅ Base de données générée avec nom personnalisé

✅ Back-Office complet avec toutes les fonctionnalités demandées

✅ Superutilisateur créé et fonctionnel

✅ Documentation complète et organisée

👥 Auteur
Ahmed Ben Hmida

