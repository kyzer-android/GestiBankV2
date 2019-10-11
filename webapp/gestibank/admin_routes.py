import logging
from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from webapp import db
from webapp.auth.models import  login_admin_required
from webapp.gestibank import bp
from webapp.gestibank.form import AgentForm, ModifagentForm, AffectdemandFrom
from webapp.gestibank.models.admin import Admin


#Renvoi la page d'index de l'administrateur
from webapp.gestibank.models.agents import Agent
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte


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
         if not formulaire.delete.data :
             try:
                 Admin.modifier_agent(formulaire,agent)
                 return redirect(url_for('gestibank.modifier_agent'))
             except ValueError as e:
                 flash(e)
                 return redirect(url_for('gestibank.modifier_agent'))
             else:
                 flash('Enregistrement validée')
         else :
             db.session.delete(agent)
             db.session.commit()
             flash('Utilisateur Supprimé')
             return redirect(url_for('gestibank.modifier_agent'))

     return render_template('gestibank/admin/modif_agent.html',form=formulaire, title="Page Admin",dict=dict)



@bp.route ('/admin/lister_demande_crea', methods=['get', 'post'])
@login_admin_required
def lister_demande_crea():
        test=Admin.lister_Demande_Crea()
        return render_template('gestibank/admin/historique.html', title="Page Admin",list_param=test[0].keys(),list_dict=test)


@bp.route ('/admin/lister_demande', methods=['get', 'post'])
@login_admin_required
def lister_demande_non_affecter():
        test=Admin.lister_demande_non_affecter()
        try :
            test [0]
        except :
            flash('Tous les compte sont affecter')
            return redirect(url_for('gestibank.lister_demande_crea'))
        else:
            return render_template('gestibank/admin/lister_demande.html', title="Page Admin", list_param=test[0].keys(),
                                   list_dict=test)


#Renvoi formualire valide demande creation
@bp.route ('/affect_demandcrea/<int:optionadmin>', methods=['get', 'post'])
@login_admin_required
def affect_demandcrea(optionadmin):
        demande = DemandeCreacompte.query.get(optionadmin)
        dict= demande.todict()
        formulaire= AffectdemandFrom()
        list =Admin.Choicelist_agent()
        formulaire.affect.choices=list

        if formulaire.validate_on_submit():
                try:
                         demande.affectation(formulaire.affect.data)
                         return redirect(url_for('gestibank.lister_demande_non_affecter'))
                except ValueError as e:
                        flash(e)
                else:
                        flash('Enregistrement validée')

        return render_template('gestibank/admin/affecter_demande_crea.html', title="Page validation demande ",
                               form=formulaire, dict = dict)