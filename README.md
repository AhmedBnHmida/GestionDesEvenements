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
- `User` (Hérite de Person)  
- `Organizer` (Relation avec Event)  

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

## 📁 Structure du Projet  
```
GestionEvenement/
├── doc/                           # Documentation complète
│   ├── 1ere etape environnement de developpement.pdf
│   ├── 2eme etape Installation de Django.pdf
│   ├── 3eme etape  création d'une application.pdf
│   └── Document.pdf
├── venv/                          # Environnement virtuel (Nom requis)
├── manage.py                      # Script de gestion du projet Django
└── Gestion_Evenement/             # Projet Django principal (Nom requis)
    ├── __init__.py                # Considérez le répertoire comme un package python
    ├── settings.py                # Configuration du projet
    ├── urls.py                    # Déclaration des urls du site
    ├── wsgi.py
    └── asgi.py
```

---

## 📚 Documentation  
La documentation détaillée est disponible dans le dossier `doc/` :  
- **1ère étape : ENVIRONNEMENT DE DÉVELOPPEMENT: VIRUALENV**  
  - Installation et activation de l'environnement virtuel.  
- **2ème étape : Installation de Django**  
  - Installation du framework et création du projet.  
- **3ème étape : création d'une application**  
  - Commande de création et fichiers générés (`models.py`, `views.py`, etc.).  
- **Document.pdf**  
  - Étude de cas, énoncé et Diagramme de classe d'analyse.  

---

## 🔧 Développement  
Commandes Django utiles :  

```bash
# Créer une nouvelle application
python manage.py startapp <Nom_Application>

# Lancer le serveur de développement
python manage.py runserver

# Lancer le serveur sur un port spécifique
python manage.py runserver 8080

# Vérifier la version de Django installée
python -m django-version
```

---

## 👥 Auteur  
Ahmed Ben Hmida
