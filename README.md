# 🎯 GestionEvenement - Application de Gestion d'Événements  

Une application web Django complète pour la gestion d'événements avec frontoffice et backoffice.

---

## 📋 Description du Projet  
L'objectif de cet atelier est de développer une application web de **gestion des évènements** en utilisant le Framework Django.

---

## 🏗️ Architecture  
- **Projet Django** : `GestionDesEvenements`
- **Applications** :
  - `Event` - Gestion des événements
  - `Person` - Gestion des utilisateurs et organisateurs

---

## 🛠️ Technologies Utilisées
- **Backend** : Django 4.2
- **Base de données** : SQLite3
- **Templating** : Django Templates
- **Authentification** : Django Auth System
- **Gestion des images** : Pillow
- **Interface admin** : Django Admin personnalisé
- **Styling** : Bootstrap 5

---

## 📊 Modèle de Données
Ce projet est basé sur le diagramme de classe d'analyse fourni.

### Event
- `id` - Identifiant unique
- `title` - Titre de l'événement
- `description` - Description détaillée (TextField)
- `image` - Image de l'événement (ImageField avec Pillow)
- `category` - Catégorie (Musique, Cinéma, Sport)
- `state` - État de l'événement (booléen, default=False)
- `nbe_participant` - Nombre de participants
- `evt_date` - Date de l'événement
- `creation_date` - Date de création
- `update_date` - Date de mise à jour

### Person
- `cin` - Carte d'identité nationale (8 caractères, clé primaire)
- `email` - Adresse email (doit se terminer par @esprit.tn)

### Participation
- `participation_date` - Date de participation (valeur par défaut: date système)

---


## 🚀 Installation et Démarrage  

### Prérequis
- **Python 3.11+**
- **Django 4.2**

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

## 🌐 URLs Disponibles

### **Pages Publiques**
- `/` - Page d'accueil avec "Bonjour 5TWIN"
- `/Person/register/` - Création de compte
- `/Person/login/` - Connexion utilisateur

### **Pages Protégées** (nécessitent une connexion)
- `/Event/bonjour/<classe>/` - Interface dynamique (ex: `/Event/bonjour/5TWIN/`)
- `/Person/logout/` - Déconnexion

### **Administration**
- `/admin/` - Interface d'administration Django

---

## 🎯 Fonctionnalités Implémentées

### **Front-Office (Utilisateurs)**
- ✅ Page d'accueil avec message de bienvenue
- ✅ Interface dynamique avec variable de classe
- ✅ Système complet d'inscription/connexion
- ✅ Affichage conditionnel selon l'état de connexion
- ✅ Protection des pages réservées aux utilisateurs connectés
- ✅ Interface responsive avec Bootstrap
- ✅ Messages de feedback utilisateur

### **Back-Office (Administration)**
- ✅ Gestion complète des événements et participants
- ✅ Filtres avancés (date, participants, état)
- ✅ Actions batch (accepter/refuser les événements)
- ✅ Interface organisée avec fieldsets
- ✅ Pagination (10 éléments par page) et recherche
- ✅ Inline des participations
- ✅ Auto-complete pour la sélection des organisateurs

---

## 👑 Administration Django
### Accès à l'Interface d'Administration
- URL Admin : http://127.0.0.1:8000/admin/

- Superutilisateur créé :

  - Username: admin

  - Email: admin@gmail.com

  - Password: admin123

---

## 📁 Structure du Projet  
```
GestionDesEvenements/
├── doc/ # Documentation complète
│ ├── 1_Document.pdf
│ ├── 2_Etude_de_cas_Generation_de_la_BD.pdf
│ ├── 3_Etude_de_cas_Dashboard_Admin.pdf
│ ├── 4_Etude_de_cas_Gestion_Utilisateur.pdf
│ ├── 1ere_etape_environnement_de_developpement.pdf
│ ├── 2eme_etape_installation_de_Django.pdf
│ └── 3eme_etape_creation_d_une_application.pdf
├── templates/ # Templates HTML
│ ├── base.html
│ ├── home.html
│ ├── login.html
│ └── register.html
├── djangoenv/ # Environnement virtuel
├── Event/ # Application Event
│ ├── migrations/
│ ├── admin.py # Configuration admin personnalisée
│ ├── models.py # Modèles Event et Participation
│ ├── views.py # Vues Front-Office
│ ├── urls.py # URLs de l'application
│ └── ...
├── Person/ # Application Person
│ ├── migrations/
│ ├── admin.py # Administration des personnes
│ ├── models.py # Modèle Person
│ ├── views.py # Vues d'authentification
│ ├── urls.py # URLs d'authentification
│ └── ...
├── GestionDesEvenements/ # Projet Django principal
│ ├── settings.py # Configuration avec nom de BD personnalisé
│ ├── urls.py # Routes URLs principales
│ └── ...
├── images/ # Dossier pour les images uploadées
├── 5TWINSDIANGO.db # Base de données (nom de classe personnalisé)
├── db.sqlite3 # Base de données SQLite
├── manage.py # Script de gestion Django
└── README.md # Documentation principale
```

---

## 📚 Documentation  
La documentation détaillée est disponible dans le dossier `doc/` :  
- **1_Document.pdf** - Présentation générale du projet

- **2_Etude_de_cas_Generation_de_la_BD.pdf** - Génération de la base de données et modèles

- **3_Etude_de_cas_Dashboard_Admin.pdf** - Configuration du Back-Office et administration

- **4_Etude_de_cas_Gestion_Utilisateur.pdf** - Gestion des utilisateurs et authentification

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

## 🧪 Guide de Test

### **Test du Front-Office**
1. **Accédez à la page d'accueil** : http://127.0.0.1:8000/
2. **Créez un compte** : Cliquez sur "Inscription"
3. **Connectez-vous** : Utilisez vos identifiants
4. **Accédez à l'interface dynamique** : Cliquez sur le lien protégé
5. **Déconnectez-vous** : Testez la déconnexion

### **Test du Back-Office**
1. **Accédez à l'admin** : http://127.0.0.1:8000/admin/
2. **Connectez-vous** avec :
   - Username: `admin`
   - Password: `admin123`
3. **Testez les fonctionnalités** :
   - Filtres par date et participants
   - Actions "Accepter/Refuser"
   - Inline des participations
   - Auto-complete des organisateurs

---

## ✅ État du Projet
- ✅ **Environnement de développement** configuré
- ✅ **Modèles de données** implémentés avec toutes les contraintes
- ✅ **Base de données** générée avec nom personnalisé
- ✅ **Back-Office complet** avec toutes les fonctionnalités demandées
- ✅ **Superutilisateur** créé et fonctionnel
- ✅ **Front-Office** - Système d'authentification implémenté
- ✅ **Gestion des utilisateurs** - Pages d'accueil, login, register
- ✅ **Interface dynamique** avec contrôle d'accès
- ✅ **Documentation** complète et organisée

---

## 👥 Auteur  
Ahmed Ben Hmida

---
