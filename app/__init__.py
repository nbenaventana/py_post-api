from flask import Flask
from app.routes import posts
from app.utils.db import init_app

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize the database
    init_app(app)

    # Register blueprints
    app.register_blueprint(posts.bp)

    return app