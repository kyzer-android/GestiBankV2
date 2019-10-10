from flask import flash, render_template
from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.clients import Client
from flask import render_template, flash, url_for
from werkzeug.utils import redirect
from webapp.auth.models import  login_admin_required
from webapp.gestibank import bp
from webapp.gestibank.form import AgentForm, VirementForm
from webapp.gestibank.models.admin import Admin
from webapp.gestibank.models.CompteBancaire import TypeCompte,Comptes
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

#renvoi la page formulaire de demande de virement
@bp.route('/virement/<id_compte>', methods=['get', 'post'])
@bp.endpoint('virement')
def virement(id_compte):
    formulaire = VirementForm()
    if formulaire.validate_on_submit():
        try :
            current_user.compte.virement_d(formulaire.montant.data)
        except ValueError as e:
            flash(e)
        else :
            flash('Opération éffectue avec succés')

    return render_template('gestibank/client/virement.html',title="Virement", form=formulaire)