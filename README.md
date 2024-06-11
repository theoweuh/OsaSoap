Egapro Data API

Ces codes Python implémentent une API REST permettant d'accéder aux données Egapro (Index de l'égalité professionnelle entre les femmes et les hommes) à partir d'un fichier CSV. L'API est construite en utilisant le framework Flask et Flask-RESTful pour fournir une interface simple et intuitive.
Fonctionnalités

    GET /siren/<siren>: Récupère les données Egapro pour un SIREN donné.

Utilisation

    Assurez-vous d'avoir Python installé sur votre système.
    Installez les dépendances requises en exécutant pip install -r requirements.txt.
    Exécutez le script Python correspondant à votre choix.
Premier Code (Sans Swagger)

python Exo15ApiRest.py

Deuxième Code (Avec Swagger)

python Exo15swagger.py

L'API sera accessible localement à l'adresse http://127.0.0.1:5000/.
Exemple d'utilisation

GET /siren/<siren>

Pour récupérer les données Egapro pour un SIREN spécifique, envoyez une requête GET à l'URL suivante :

http

GET http://127.0.0.1:5000/siren/<siren>

Replacez <siren> par le numéro SIREN souhaité.
