from flask import Blueprint

bp = Blueprint('edu_api', __name__)

from . import routes