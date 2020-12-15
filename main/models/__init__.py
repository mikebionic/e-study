from flask import Blueprint

bp = Blueprint('models', __name__)

from .main import models as main_models
from .users import models as users_models