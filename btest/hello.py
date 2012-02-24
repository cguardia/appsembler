from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
   return Response('Hello from appsembler, %(name)s!' % request.matchdict)

if __name__ == '__main__':
    port = int(os.getenv('VCAP_APP_PORT', '8000'))
    host = os.getenv('VCAP_APP_HOST', '0.0.0.0')
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server(host, port, app)
    server.serve_forever()
