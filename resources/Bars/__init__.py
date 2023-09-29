from flask_smorest import Blueprint

bp = Blueprint('bars', __name__, url_prefix='/Bars')

from . import routes