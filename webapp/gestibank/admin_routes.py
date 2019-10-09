import logging
from flask import render_template, flash, url_for
from werkzeug.utils import redirect
from webapp.auth.models import  login_admin_required
from webapp.gestibank import bp
from webapp.gestibank.form import AgentForm,ModifagentForm
from webapp.gestibank.models.admin import Admin


#Renvoi la page d'index de l'administrateur
from webapp.gestibank.models.agents import Agent


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

@bp.route ('/admin/modif_agent/<int:parametre>', methods=['get', 'post'])
@login_admin_required
def modif_agent(parametre):
     agent=Agent.query.get(parametre)
     dict=agent.todict()
     formulaire=ModifagentForm()
     if formulaire.validate_on_submit():
         try:
             Admin.modifier_agent(formulaire,agent)
             return redirect(url_for('gestibank.modifier_agent'))
         except ValueError as e:
             flash(e)
             return redirect(url_for('gestibank.modifier_agent'))
         else:
             flash('Enregistrement validée')


     return render_template('gestibank/admin/modif_agent.html',form=formulaire, title="Page Admin",dict=dict)



@bp.route ('/admin/lister_demande_crea', methods=['get', 'post'])
@login_admin_required
def lister_demande_crea():
        test=Admin.lister_Demande_Crea()
        return render_template('gestibank/admin/lister_demande.html', title="Page Admin",list_param=test[0],list_dict=test[1])


@bp.route ('/admin/lister_demande', methods=['get', 'post'])
@login_admin_required
def lister_demande_non_affecter():
        test=Admin.lister_demande_non_affecter()
        return render_template('gestibank/admin/lister_demande.html', title="Page Admin",list_param=test[0],list_dict=test[1])

