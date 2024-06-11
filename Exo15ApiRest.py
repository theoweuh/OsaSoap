from csv import DictReader
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

egapro_data = {}

with open("C:\Users\alexi\Documents\CSV\index-egalite-fh-utf8 1.csv") as csv_file:
    reader = DictReader(csv_file, delimiter=";", quotechar='"')
    for row in reader:
        if egapro_data.get(row["SIREN"]) is None:
            egapro_data[row["SIREN"]] = row
        elif egapro_data[row["SIREN"]]["Année"] < row["Année"]:
            egapro_data[row["SIREN"]].update(row)

application = Flask(__name__)
api = Api(application)


class EgaproData(Resource):
    def get(self, siren):
        response = egapro_data.get(siren)
        if response is None:
            return {"error": "SIREN not found"}, 404
        return response, 200


api.add_resource(EgaproData, "/siren/<string:siren>")

if __name__ == "__main__":
    application.run(debug=True)
