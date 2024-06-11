from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield f'Hello, {name}'

application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, wsgi_application)
    server.serve_forever()
