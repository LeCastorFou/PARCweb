from PARC import create_app
import socket
from PARC.controller import  pwa

app = create_app()

app.register_blueprint(pwa.bp)
# Pour ne pas passer par les variables d'environement

app.jinja_env.cache = {}


if socket.gethostname() in ['scw-01d95d','scw-c83777'] :
    if __name__ == '__main__':
        app.run(debug=False,host= '0.0.0.0', port = 80)
else:
    if __name__ == '__main__':
        app.run(debug=True, port = 5000)
