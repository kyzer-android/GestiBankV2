from flask import Blueprint
bp = Blueprint('api',__name__,url_prefix='/api')
from webapp.api import user