# Fichier rpc_service.py
import rpyc

class MyService(rpyc.Service):
    def exposed_get_answer(self):  # this is an exposed method
        return 42

    def get_question(self):  # while this method is not exposed
        return "what is the airspeed velocity of an unladen swallow?"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=9000)
    t.start()
