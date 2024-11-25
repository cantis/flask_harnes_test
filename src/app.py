from flask import Flask
from .routes.home import home_bp

def create_app() -> Flask:
    """Create a Flask app."""
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    return app