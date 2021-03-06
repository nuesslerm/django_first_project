from .server import app
from livereload import Server

app.debug = True

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve(port=5555, debug=True)
