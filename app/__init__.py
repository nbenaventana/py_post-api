from flask import Flask
from app.routes import posts
from app.utils.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(posts.bp)

    return app
