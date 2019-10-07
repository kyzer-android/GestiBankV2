# Creation du blue Print Gestibank
from flask import Blueprint
bp = Blueprint('gestibank',__name__)
from webapp.gestibank import gestibank_routes
from webapp.gestibank import admin_routes