from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home() -> ResponseReturnValue:
    """Default route that displays Hello World."""
    return render_template('home.html')
