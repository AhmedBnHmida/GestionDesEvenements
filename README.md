# 🎯 GestionEvenement - Application de Gestion d'Événements  

Une application web Django complète pour la gestion d'événements avec frontoffice et backoffice.

---

## 📋 Description du Projet  
L'objectif de cet atelier est de développer une application web de **gestion des évènements** en utilisant le Framework Django.

---

## 🏗️ Architecture  
- **Projet Django** : `Gestion Evenement`  
- **Applications** :  
  - `Event`  
  - `Person`  

---

## 📊 Modèle de Données  
Ce projet est basé sur le diagramme de classe d'analyse fourni.

### Event  
- `id`  
- `title`  
- `description`  
- `image`  
- `category`  
- `state`  
- `nbe_participant`  
- `evt_date`  
- `creation_date`  
- `update_date`  

### Person  
- `cin`  
- `email`  

### Participation  
- `participation_date`  

---

## 🚀 Installation et Démarrage  

### Prérequis  
- **Python 3.11** (Requis pour la mise en place du projet)  
- **Django 4.1** (Requis pour la mise en place du projet)  

### 1. Environnement Virtuel  
L'environnement virtuel (`virtualenv`) est utilisé pour installer des versions spécifiques de paquets pour ce projet spécifique, évitant ainsi les conflits.  
Le nom de l'environnement virtuel doit être **`venv`**.

```bash
# Installer virtualenv (si ce n'est pas déjà fait)
pip install virtualenv

# Création de l'environnement virtuel
virtualenv venv

# Activation (Linux/macOS)
source venv/bin/activate

# Activation (Windows)
venv\Scripts\activate

# (Remarque : Pour désactiver l'environnement, utilisez la commande deactivate.)
```

### 2. Installation de Django  
Installez la version requise de Django dans l'environnement virtuel activé.

```bash
pip install Django==4.1
```

### 3. Configuration du Projet  
```bash
# Création du projet nommé 'Gestion Evenement'
django-admin startproject Gestion_Evenement

# Création des applications 'Event' et 'Person'
python manage.py startapp Event
python manage.py startapp Person

# Migrations de la base de données (Étapes futures)
# python manage.py makemigrations
# python manage.py migrate

# Création du superutilisateur (Étapes futures)
# python manage.py createsuperuser
```

### 4. Lancement du Serveur  
Lancez le serveur de développement.

```bash
python manage.py runserver
```

Accédez à l'application : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👑 Administration Django
### Accès à l'Interface d'Administration
- URL Admin : http://127.0.0.1:8000/admin/

- Superutilisateur créé :

  - Username: admin

  - Email: admin@gmail.com

  - Password: admin123

### Fonctionnalités Back-Office Implémentées
🔧 Administration des Personnes
- Recherche par username

- Gestion complète des profils

🎯 Administration des Événements
- Affichage personnalisé avec list_display

- Filtres avancés :

  - Par titre d'événement

  - Par nombre de participants ("No participants", "There are participants")

  - Par date ("Past Events", "Upcoming Events", "Today Events")

- Actions personnalisées : "Accepter/Refuser" les événements

- Pagination (10 éléments par page)

- Formulaire organisé avec fieldsets

- Inline des participations

- Auto-complete pour la sélection des organisateurs

---

## 📁 Structure du Projet  
```
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
```

---

## 📚 Documentation  
La documentation détaillée est disponible dans le dossier `doc/` :  
- **1_Document.pdf** - Présentation générale du projet

- **2_Etude_de_cas_Generation_de_la_BD.pdf** - Génération de la base de données et modèles

- **3_Etude_de_cas_Dashboard_Admin.pdf** - Configuration du Back-Office et administration

- **1ere_etape_environnement_de_developpement.pdf** - Environnement virtuel

- **2eme_etape_installation_de_Django.pdf** - Installation de Django

- **3eme_etape_creation_d_une_application.pdf** - Création des applications

---

## 🔧 Développement  
Commandes Django utiles :  

```bash
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
```
---

✅ État du Projet
- ✅ Environnement de développement configuré

- ✅ Modèles de données implémentés avec toutes les contraintes

- ✅ Base de données générée avec nom personnalisé

- ✅ Back-Office complet avec toutes les fonctionnalités demandées

- ✅ Superutilisateur créé et fonctionnel

- ✅ Documentation complète et organisée

---

## 👥 Auteur  
Ahmed Ben Hmida

---
