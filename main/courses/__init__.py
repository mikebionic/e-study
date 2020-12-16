from flask import Blueprint

bp = Blueprint('courses', __name__)

from . import routes