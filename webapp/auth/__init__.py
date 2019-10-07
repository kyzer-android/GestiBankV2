#Creation du blueprint d'autentification

from flask import Blueprint
bp = Blueprint('auth',__name__)
from webapp.auth import auth
