from datetime import date

from flask import flash, render_template, url_for
from flask_login import current_user
from werkzeug.utils import redirect
from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.clients import Client
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte
from webapp.gestibank.form import ValidedemandFrom
import logging




#Renvoi les nouvelles demande de création de l'Agent connecter (NONE)
@bp.route ('/agent/nvldemande/')
@login_agent_required
def nvldemande():
        list_demandes = current_user.lister_demandecrea()
        list = DemandeCreacompte.list_param()
        list_dict_final=[]
        for demande in list_demandes:
             if demande['valide'] ==None:
                 list_dict_final.append(demande)
        logging.debug(list_dict_final)
        return render_template('gestibank/agent/demande.html', title="Page demande affectée",
                               list_param=list , list_dict=list_dict_final)

#Renvoi toutes les demandes affecté à l'agent (FALSE)
@bp.route ('/agent/demandeenattente/')
@login_agent_required
def demandeenattente():
    list_demandes = current_user.lister_demandecrea()
    list = DemandeCreacompte.list_param()
    list_dict_final = []
    for demande in list_demandes:
        if demande['valide'] == False:
            list_dict_final.append(demande)
    logging.debug(list_dict_final)
    return render_template('gestibank/agent/demande.html', title="Page demande affectée",
                           list_param=list, list_dict=list_dict_final)


#Renvoi toutes les demandes affecté à l'agent (NONE/TRUE/FALSE)
@bp.route ('/agent/demande/')
@login_agent_required
def demande():
        test = current_user.lister_demandecrea()
        list = DemandeCreacompte.list_param()
        logging.debug(test)
        return render_template('gestibank/agent/historique.html', title="Page demande affectée",
                               list_param=list , list_dict=test)

#Renvoi la page des demande de chéquier de ses clients
@bp.route ('/agent/demandechequier/')
@login_agent_required
def demandechequier():
        return render_template('gestibank/agent/demandechequier.html', title="Page demande chequier ")

#Renvoi la liste clients
@bp.route ('/agent/listeclients/')
@login_agent_required
def listeclients():
        list_agent= current_user.lister_les_clients()
        return render_template('gestibank/agent/listeclients.html', title="Page demande chequier ", dict = list_agent,list=list_agent[0].keys())

#Renvoi la fiche d'un client
@bp.route ('/agent/client/<int:client_id>')
@login_agent_required
def client(client_id):
        client=Client.query.get(client_id)
        dict_client=client.to_dict()
        return render_template('gestibank/agent/client.html', title="Page demande chequier ", name=dict_client['nom'])

#Renvoi formualire valide demande creation
@bp.route ('/agent/valid_demandcrea/<int:option>', methods=['get', 'post'])
# @login_agent_required
def valid_demandcrea(option):
        demande = DemandeCreacompte.query.get(option)
        dict= demande.todict()
        formulaire= ValidedemandFrom()
        print("avant")
        if formulaire.validate_on_submit():
                try:
                        if formulaire.valide.data == "True":
                                print("test1")
                                current_user.validation_Crea(demande, True)
                                return redirect(url_for('gestibank.demande'))
                        elif formulaire.valide.data == "False":
                                current_user.validation_Crea(demande, False)
                                print("test12")
                                return redirect(url_for('gestibank.demande'))

                except ValueError as e:
                        flash(e)
                else:
                        print("test13")
                        flash('Enregistrement validée')

                        return redirect(url_for('gestibank.demande'))

        return render_template('gestibank/agent/valid_demandcrea.html', title="Page validation demande ",
                               form=formulaire, dict = dict)

