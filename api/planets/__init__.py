from flask import Blueprint

planets = Blueprint('planets', __name__)

from . import routes