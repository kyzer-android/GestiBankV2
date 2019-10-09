from flask import flash, render_template
from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.clients import Client
from flask import render_template, flash, url_for
from werkzeug.utils import redirect
from webapp.auth.models import  login_admin_required
from webapp.gestibank import bp
from webapp.gestibank.form import AgentForm
from webapp.gestibank.models.admin import Admin
from datetime import date

from flask import flash, render_template
from flask_login import current_user

from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte
from webapp.gestibank.form import InscriptionForm




#Renvoi la page des demande de création de l'Agent connecter
@bp.route ('/historique/')
@login_client_required
def historique():
   cl =current_user.lister_comptes()

   cl=cl*5

   return render_template('gestibank/client/historique.html', cl=cl,keys=cl[0].keys())