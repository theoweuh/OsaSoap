from csv import DictReader
from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


egapro_data = {}

with open("index-egalite-fh-utf8.csv") as csv_file:
    reader = DictReader(csv_file, delimiter=";", quotechar='"')
    for row in reader:
        if egapro_data.get(row["SIREN"]) is None:
            egapro_data[row["SIREN"]] = row
        elif egapro_data[row["SIREN"]]["Année"] < row["Année"]:
            egapro_data[row["SIREN"]].update(row)



class EgaProService(ServiceBase):
    @rpc(Integer, _returns=Unicode)
    def getEgaProData(ctx, siren):
        """
        Renvoie les données EgaPro pour un numéro de SIREN donné.
        Un message d'erreur est renvoyé si le SIREN n'est pas trouvé.

        :param siren: Numéro de SIREN en tant qu'entier
        :return: Les données correspondantes sous forme de chaîne JSON
        """
        data = egapro_data.get(str(siren))
        if data is None:
            return "SIREN not found"
        return str(data)

soap_app = Application([EgaProService],
                       tns='namespace',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

wsgi_app = WsgiApplication(soap_app)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Server is running at http://localhost:8000/?wsdl")
    server.serve_forever()