from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from webapp.auth.models import  login_admin_required
from webapp.gestibank import bp
from webapp.gestibank.form import AgentForm

#Renvoi la page d'index de l'administrateur
from webapp.gestibank.models.admin import Admin


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
    formulaire = AgentForm()
    formulaire2= AgentForm()
    if formulaire.validate_on_submit():
        try:
            Admin.cree_agent(formulaire)
            return redirect(url_for('gestibank.modifier_agent'))
        except ValueError as e:
            flash(e)
        else:
            flash('Enregistrement validée')
        return render_template('gestibank/admin/modifier_agent.html', title="Page Admin",list=(formulaire,formulaire2))

