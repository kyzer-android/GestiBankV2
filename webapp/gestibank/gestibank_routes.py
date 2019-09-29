from datetime import date

from flask import flash, render_template
from flask_login import current_user

from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models import DemandeCreacompte
from webapp.gestibank.form import InscriptionForm


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


@bp.route ('/admin/<int:param>')
@login_admin_required
def admin(param=None):
        return render_template('gestibank/admin.html', title="Page Admin", param=param)


@bp.route ('/agent/<int:param>')
@login_agent_required
def agent(param=None):
        return render_template('gestibank/agent.html', title="Page Agent", param=param)


@bp.route ('/client/<int:param>')
@login_client_required
def client(param=None):
        return render_template('gestibank/client.html', title="Page Client", param=param)
