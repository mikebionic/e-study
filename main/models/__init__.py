from flask import Blueprint

bp = Blueprint('models', __name__)

from .main import models as main_models
from .edu import models as edu_models
from .user import models as user_models