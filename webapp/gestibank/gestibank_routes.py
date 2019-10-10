from flask import flash, render_template
from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte
from webapp.gestibank.form import InscriptionForm
from webapp.gestibank.models.clients import Client

#renvoi la page formulaire de demande de creation de compte
@bp.route('/inscription', methods=['get', 'post'])
def inscription():
    formulaire = InscriptionForm()
    if formulaire.validate_on_submit():
        try :
           DemandeCreacompte.add_demande(formulaire)
        except ValueError as e:
            flash(e)
        else :
            flash('Enregistrement validée')

    return render_template('gestibank/inscription.html',title="Inscription", form=formulaire)

#Renvoi la page d'index de l'administrateur
@bp.route ('/admin/<int:param>')
@login_admin_required
def admin(param=None):
        return render_template('gestibank/admin/index.html', title="Page Admin", param=param)


#Renvoi la page d'index de l'Agent connecter
@bp.route ('/agent/<int:param>')
@login_agent_required
def agent(param=None):
        return render_template('gestibank/agent/index.html', title="Page Agent", param=param)

#Renvoi la page d'index de l'Agent connecter
@bp.route ('/client/<int:param>')
@login_client_required
def client(param=None):
        return render_template('gestibank/client/index.html', title="Page client", param=param)

#Renvoi la page d'index de l'Agent connecter
@bp.route ('/enconstruction/')

def enconstruction(param=None):
        return render_template('gestibank/enconstruction.html', title="Page construction", param=param)
