from flask import Flask
from app.routes import posts  # Importamos el blueprint de posts
from app.utils.db import mongo  # Importamos la conexión a MongoDB

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Cargamos la configuración

    # Inicializamos la conexión a MongoDB
    mongo.init_app(app)

    # Registramos el blueprint de posts
    app.register_blueprint(posts.bp)

    return app