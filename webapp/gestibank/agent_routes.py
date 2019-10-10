from datetime import date

from flask import flash, render_template, url_for
from flask_login import current_user
from werkzeug.utils import redirect
from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.agents import Agent
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte
from webapp.gestibank.form import ValidedemandFrom
import logging




#Renvoi les nouvelles demande de création de l'Agent connecter (NONE)
@bp.route ('/nvldemande/')
@login_agent_required
def nvldemande():
        test = current_user.lister_demandecrea()
        list = DemandeCreacompte.list_param()
        logging.debug(test)
        return render_template('gestibank/agent/demande.html', title="Page demande affectée",
                               list_param=list , list_dict=test)

#Renvoi toutes les demandes affecté à l'agent (NONE/TRUE/FALSE)
@bp.route ('/demande/')
@login_agent_required
def demande():
        test = current_user.lister_demandecrea()
        list = DemandeCreacompte.list_param()
        logging.debug(test)
        return render_template('gestibank/agent/demande.html', title="Page demande affectée",
                               list_param=list , list_dict=test)

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

#Renvoi formualire valide demande creation
@bp.route ('/valid_demandcrea/<int:option>', methods=['get', 'post'])
@login_agent_required
def valid_demandcrea(option):
        demande = DemandeCreacompte.query.get(option)
        dict= demande.todict()
        formulaire= ValidedemandFrom()
        if formulaire.validate_on_submit():
                try:
                        if formulaire.valide.data == "True":
                                current_user.validation_Crea(demande, True)
                                return redirect(url_for('gestibank.demande'))
                        elif formulaire.valide.data == "False":
                                current_user.validation_Crea(demande, False)
                                return redirect(url_for('gestibank.demande'))
                except ValueError as e:
                        flash(e)
                else:
                        flash('Enregistrement validée')

                        return redirect(url_for('gestibank.demande'))
        return render_template('gestibank/agent/valid_demandcrea.html', title="Page validation demande ",
                               form=formulaire, dict = dict)
