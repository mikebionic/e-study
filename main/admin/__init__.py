from flask import Blueprint

bp = Blueprint('admin', __name__)

from . import routes