from flask import flash, render_template

from webapp import db
from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.clients import Client
from flask import render_template, flash, url_for
from werkzeug.utils import redirect
from webapp.auth.models import  login_admin_required
from webapp.gestibank import bp
from webapp.gestibank.form import AgentForm, VirementForm, OperationForm, ContactForm, ChiquedemandFrom
from webapp.gestibank.models.admin import Admin
from webapp.gestibank.models.CompteBancaire import TypeCompte,Comptes
from datetime import date

from flask import flash, render_template
from flask_login import current_user

from webapp.auth.models import login_admin_required, login_agent_required, login_client_required
from webapp.gestibank import bp
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte
from webapp.gestibank.form import InscriptionForm
from webapp.gestibank.models.transaction import Transaction



#Renvoi la page des demande de création de l'Agent connecter
@bp.route ('/client/historique/')
@login_client_required
def historique():
   cl =current_user.lister_comptes()
   return render_template('gestibank/client/historique.html', cl=cl,keys=cl[0].keys())


@bp.route ('/client/liste_compte/')
@login_client_required
def liste_compte():
   cl =current_user.lister_comptes()

   return render_template('gestibank/client/liste_compte.html', cl=cl,keys=cl[0].keys())

#renvoi la page pour effectuer des operations
@bp.route('/client/operation/<int:id_compte>', methods=['get', 'post'])
@bp.endpoint('operation')
def operation(id_compte):
    compte =Comptes.query.get(id_compte)



    return render_template('gestibank/client/operation.html',title="Operation", compte=compte)

#renvoi la page pour contacter le conseiller
@bp.route('/client/contact/<int:id_compte>', methods=['get', 'post'])
def contact():
    formulaire = ContactForm()
    return render_template('gestibank/client/contact.html',title="Operation", form=formulaire)

@bp.route('/client/demande_cheque/<int:id_compte>', methods=['get', 'post'])
def demande_cheque():
    formulaire = ChiquedemandFrom()

    flash("Demande effectuer effectuer avec succés  ")
    return render_template('gestibank/client/demande_cheque.html', title="Demande_cheque", form=formulaire)

#renvoi la page formulaire de demande de virement
@bp.route('/client/virement/<int:id_compte>', methods=['get', 'post'])
def virement(id_compte):
    # x = Comptes.query.get(id_compte)
    formulaire = VirementForm()

    if formulaire.validate_on_submit() and  current_user.is_authenticated == True :
        try :

            Comptes.query.get(id_compte).virement_d(formulaire)


        except ValueError as e:
            flash(e)

    return render_template('gestibank/client/virement.html',title="Virement", form=formulaire)




@bp.route ('/client/historique_transaction/<int:id_compte>')
@login_client_required
def historique_transaction(id_compte):
   transaction=Transaction.lister_transaction(id_compte)

   return render_template('gestibank/client/historiquetransaction.html', transaction=transaction,list_param=transaction[0].keys())

@bp.route ('/client/compte_virement/')
@login_client_required
def compte_virement():
   cl =current_user.lister_comptes()
   return render_template('gestibank/client/compte_virement.html', cl=cl,keys=cl[0].keys())
