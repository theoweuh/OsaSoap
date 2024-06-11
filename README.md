# Projet SOAP, REST et RPC

Ce projet vise à implémenter des services API REST, API SOAP et RPC dans un environnement Docker. Il comprend la documentation des API et l'intégration de Swagger pour l'API REST et de WSDL pour l'API SOAP.

## Architecture des fichiers

Le projet est organisé comme suit :

├── rest_service/ # Service API REST
│ ├── app.py # Code source du service API REST
│ ├── requirements.txt # Fichier des dépendances Python pour le service REST
│ └── Dockerfile # Dockerfile pour construire l'image Docker du service REST
│
├── soap_service/ # Service API SOAP
│ ├── soap_service.py # Code source du service API SOAP
│ ├── requirements.txt # Fichier des dépendances Python pour le service SOAP
│ └── Dockerfile # Dockerfile pour construire l'image Docker du service SOAP
│
└── rpc_service/ # Service RPC
├── rpc_service.py # Code source du service RPC
├── requirements.txt # Fichier des dépendances Python pour le service RPC
└── Dockerfile # Dockerfile pour construire l'image Docker du service RPC

markdown
Copier le code

## Contenu du projet

- **docker-compose.yml** : Fichier de configuration Docker Compose pour définir et exécuter les services Docker.
- **README.md** : Ce fichier, expliquant l'organisation du projet et fournissant des instructions pour l'exécution.

## Instructions d'exécution

1. Assurez-vous d'avoir Docker installé sur votre machine.
2. Clonez ce dépôt sur votre machine.
3. Assurez-vous que les ports requis (7777, 8000, 9000) ne sont pas déjà utilisés par d'autres applications sur votre machine.
4. Accédez au répertoire du projet dans votre terminal.
5. Exécutez la commande suivante pour démarrer les services :

```sh
docker-compose up --build
Documentation des API
API REST : Documentée à l'aide de Swagger, accessible à l'adresse : http://localhost:7777/swagger-ui/
API SOAP : Documentée à l'aide de WSDL, accessible à l'adresse : http://localhost:8000/?wsdl
bash
Copier le code

Cela devrait être prêt à être ajouté à votre fichier README.md dans votre projet.
