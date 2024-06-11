# Projet Soap

Ce projet consiste en la mise en place de services API REST, API SOAP et RPC dans un environnement Docker, avec la documentation des API et l'intégration de Swagger pour l'API REST et WSDL pour l'API SOAP.

## Architecture des fichiers

Le projet est organisé comme suit :

```bash
├── rest_service/           # Service API REST
│   ├── app.py              # Code source du service API REST
│   ├── requirements.txt    # Fichier des dépendances Python pour le service REST
│   └── Dockerfile          # Dockerfile pour construire l'image Docker du service REST
│
├── soap_service/           # Service API SOAP
│   ├── soap_service.py     # Code source du service API SOAP
│   ├── requirements.txt    # Fichier des dépendances Python pour le service SOAP
│   └── Dockerfile          # Dockerfile pour construire l'image Docker du service SOAP
│
└── rpc_service/            # Service RPC
    ├── rpc_service.py      # Code source du service RPC
    ├── requirements.txt    # Fichier des dépendances Python pour le service RPC
    └── Dockerfile          # Dockerfile pour construire l'image Docker du service RPC
