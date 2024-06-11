# Utiliser une image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 9000

# Définir la commande pour exécuter l'application
CMD ["python", "rpc_service.py"]
