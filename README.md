# Smart Trash : Application de Prédiction de Recyclabilité des objets dans des images

Ce projet est une application web construite avec **Streamlit** permettant de télécharger une image et de prédire si elle est recyclable ou non. L'application utilise une API FastAPI qui effectue la prédiction en utilisant un modèle de machine learning au format `.h5`. L'ensemble du projet est conteneurisé à l'aide de **Docker** et géré avec **Docker Compose** pour faciliter le déploiement.

## Fonctionnalités

- Téléchargement d'images via l'interface Streamlit.
- Envoi de l'image à une API FastAPI pour effectuer une prédiction de recyclabilité.
- Le modèle de machine learning (au format `.h5`) analyse l'image et renvoie une prédiction.
- Interface simple et intuitive pour l'utilisateur.
- Conteneurisation via Docker Compose pour une configuration rapide et flexible.

## Prérequis

Avant de lancer l'application, assurez-vous d'avoir les outils suivants installés sur votre machine :

- **Docker** (https://www.docker.com/)
- **Docker Compose** (https://docs.docker.com/compose/)

## Installation

1. Clonez ce repository :
2. Construisez et lancez les services Docker via Docker Compose :
   ```bash
   docker-compose up --build
   ```
   
   Cette commande va :

    - Construire l'image Docker pour l'API FastAPI.
    - Construire l'image Docker pour l'application Streamlit.
    - Lancer les deux services (API et Streamlit) dans des conteneurs séparés.
      
3. Une fois l'application lancée, vous pouvez accéder à l'interface Streamlit dans votre navigateur à l'adresse suivante :
   ```bash
   http://localhost:8501
   ```

## Utilisation

1. Ouvrez votre navigateur et accédez à l'URL locale de Streamlit.
2. Téléchargez une image via l'interface Streamlit.
3. L'image sera envoyée à l'API FastAPI, qui effectuera la prédiction.
4. Le résultat de la prédiction indiquera si l'image est recyclable ou non avec une probabilite.

## Structure du projet

Le projet est organisé comme suit :
   ```bash
   ├── app/
   │   ├── api/               # Contient l'API FastAPI
   │   ├── model/             # Modèle ML au format .h5
   │   └── streamlit_app/     # Application Streamlit
   ├── docker-compose.yml     # Fichier de configuration Docker Compose
   └── README.md              # Ce fichier
   ```

## Technologies utilisées

    - FastAPI pour l'API REST
    - Streamlit pour l'interface utilisateur
    - TensorFlow/Keras pour le modèle de machine learning
    - Docker pour la conteneurisation



