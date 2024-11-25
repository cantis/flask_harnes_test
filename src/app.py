from flask import Flask

def create_app() -> Flask:
    """Create a Flask app."""
    app = Flask(__name__)
    return app