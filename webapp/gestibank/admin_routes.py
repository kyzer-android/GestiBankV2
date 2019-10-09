import logging
from flask import render_template, flash, url_for
from werkzeug.utils import redirect
from webapp.auth.models import  login_admin_required
from webapp.gestibank import bp
from webapp.gestibank.form import AgentForm
from webapp.gestibank.models.admin import Admin


#Renvoi la page d'index de l'administrateur
@bp.route ('/admin/gestion_agent', methods=['get', 'post'])
@login_admin_required
def gestion_agent():
    formulaire = AgentForm()
    if formulaire.validate_on_submit():
        try :
           Admin.cree_agent(formulaire)
           return redirect(url_for('gestibank.admin', param=0))
        except ValueError as e:
            flash(e)
        else :
            flash('Enregistrement validée')
            return  redirect(url_for('gestibank.admin',param=0))

    return render_template('gestibank/admin/gestion_agent.html', title="Page Admin" , form=formulaire)


@bp.route ('/admin/modifier_agent', methods=['get', 'post'])
@login_admin_required
def modifier_agent():
        test=Admin.lister_agent()
        logging.debug(test)

        return render_template('gestibank/admin/modifier_agent.html', title="Page Admin",list_param=test[0],list_dict=test[1])

