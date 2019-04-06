from flask import Flask
from config import Config


def create_app(configuration=Config):
    """Flask App Instance"""
    # Create app and load configuration
    app = Flask(__name__)
    app.config.from_object(configuration)

    # Import extensions
    from app.models import db, csrf, migrate

    # Register extensions
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints
    from app.views.base import base

    # Register blueprints
    app.register_blueprint(base)
    return app
