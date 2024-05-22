# Utiliser l'image de base Python
FROM python:3.12

# Définir le répertoire de travail
WORKDIR /streamlit_project

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port 8501
EXPOSE 8501

# Définir la commande par défaut
CMD ["streamlit", "run", "app.py"]
