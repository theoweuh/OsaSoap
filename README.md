Diagramme de sequence du project: ![image](https://github.com/theoweuh/OsaSoap/assets/39169618/6dddf702-67bd-42fb-b229-663d6b87cd60)

 # README

Ce projet contient un service SOAP simple réalisé avec Spyne dans un environnement virtuel Python.

## Configuration de l'environnement virtuel

1. **Installation de Python**: Si Python n'est pas déjà installé, téléchargez et installez la version recommandée par Spyne depuis le site officiel de Python : https://www.python.org/downloads/

2. **Création d'un environnement virtuel**: Utilisez la commande suivante pour créer un nouvel environnement virtuel nommé `myenv` dans le répertoire du projet : py -m venv myenv
   

3. **Activation de l'environnement virtuel**: Activez l'environnement virtuel avec la commande appropriée selon votre système d'exploitation : 
Sur Windows : myenv\Scripts\activate

4. **Installation des dépendances**: Une fois l'environnement virtuel activé, installez Spyne et les autres dépendances nécessaires avec la commande suivante : py -m pip install spyne

5. ## Exécution du service SOAP

Une fois l'environnement virtuel configuré et Spyne installé, vous pouvez démarrer le service SOAP en exécutant le fichier `soap_service.py`. py soap_service.py

Le service SOAP sera accessible à l'adresse http://localhost:8000/?wsdl par défaut.

Assurez-vous de consulter la documentation de Spyne pour plus d'informations sur la création de services SOAP et la configuration de votre environnement : https://spyne.io/docs/2.14/index.html
