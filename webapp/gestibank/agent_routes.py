from datetime import date

from flask import flash, render_template
from flask_login import current_user

from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte
from webapp.gestibank.form import InscriptionForm




#Renvoi la page des demande de création de l'Agent connecter
@bp.route ('/demande/')
@login_agent_required
def demande():
        a = current_user.filtre_compte()
        return render_template('gestibank/agent/demande.html', title="Page demande affectée", list = a)

#Renvoi la page des nouvelles demande de création de l'Agent connecter
@bp.route ('/nvldemande/')
@login_agent_required
def nvldemande():
        return render_template('gestibank/agent/nouvelledemande.html', title="Page nouvelle demande affectées")

#Renvoi la page des demande de chéquier de ses clients
@bp.route ('/demandechequier/')
@login_agent_required
def demandechequier():
        return render_template('gestibank/agent/demandechequier.html', title="Page demande chequier ")

#Renvoi la liste clients
@bp.route ('/listeclients/')
@login_agent_required
def listeclients():
        a = current_user.filtre_clients()
        return render_template('gestibank/agent/listeclients.html', title="Page demande chequier ", list = a)

