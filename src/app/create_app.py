from flask import Flask
from .config import Config
from .routes.health import health_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(health_bp)

    return app
