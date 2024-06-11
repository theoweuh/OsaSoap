from csv import DictReader
from flask import Flask
from flask_restplus import Api, Resource, fields

# Chargement des données Egapro depuis le fichier CSV
egapro_data = {}

with open("C:\Users\alexi\Documents\CSV\index-egalite-fh-utf8 1.csv") as csv_file:
    reader = DictReader(csv_file, delimiter=";", quotechar='"')
    for row in reader:
        if egapro_data.get(row["SIREN"]) is None:
            egapro_data[row["SIREN"]] = row
        elif egapro_data[row["SIREN"]]["Année"] < row["Année"]:
            egapro_data[row["SIREN"]].update(row)

application = Flask(__name__)
api = Api(application, version='1.0', title='Egapro Data API', description='API for accessing Egapro data')

# Définition du modèle pour la réponse JSON
egapro_model = api.model('EgaproData', {
    'SIREN': fields.String,
    'other_field': fields.String  # Ajoutez d'autres champs ici selon votre CSV
})


class EgaproData(Resource):
    @api.doc(responses={200: 'OK', 404: 'SIREN not found'})
    @api.marshal_with(egapro_model)
    def get(self, siren):
        """Récupère les données Egapro pour un SIREN donné."""
        response = egapro_data.get(siren)
        if response is None:
            api.abort(404, message="SIREN not found")
        return response, 200


api.add_resource(EgaproData, "/siren/<string:siren>")

if __name__ == "__main__":
    application.run(debug=True)
