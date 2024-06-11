Projet Soap
Ce projet consiste en la mise en place de services API REST, API SOAP et RPC dans un environnement Docker, avec la documentation des API et l'intégration de Swagger pour l'API REST et WSDL pour l'API SOAP.

Architecture des fichiers
Le projet est organisé comme suit :

bash
Copier le code
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
Contenu du projet
docker-compose.yml : Fichier de configuration Docker Compose pour définir et exécuter les services Docker.
README.md : Ce fichier, expliquant l'organisation du projet et fournissant des instructions pour l'exécution.
Instructions d'exécution
Assurez-vous d'avoir Docker installé sur votre machine.
Clonez ce dépôt sur votre machine.
Assurez-vous que les ports requis (5000, 8000, 9000) ne sont pas déjà utilisés par d'autres applications sur votre machine.
Accédez au répertoire du projet dans votre terminal.
Exécutez la commande suivante pour démarrer les services :
Copier le code
docker-compose up
Une fois que les services sont démarrés, vous pouvez accéder aux différentes API via les ports spécifiés dans le fichier docker-compose.yml.
Documentation des API
L'API REST est documentée à l'aide de Swagger et est accessible à l'adresse : http://localhost:5000/swagger-ui/
L'API SOAP est documentée à l'aide de WSDL et est accessible à l'adresse : http://localhost:8000/?wsdl
