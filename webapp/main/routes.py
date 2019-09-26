from datetime import date
from flask import render_template, flash
from flask_login import current_user,  login_required
from webapp.main import models
import os
from webapp.main import bp
from webapp.main.CreaCompte import add_demande
from webapp.main.form import InscriptionForm


@bp.route('/')
@bp.route('/index')
def index():
    if not current_user.is_anonymous:
        user = {'username': current_user.username}
    else:
        user = {'username': 'Guest'}
    return render_template('index.html', title="Page d'accueil et menu", user=user,date=date.today())




@bp.route('/maliste')
@login_required
def maliste():
    maliste = os.listdir('c:/')
    return render_template('maliste.html', title='Madliste', myliste=maliste)


@bp.route('/madb')
def madb():
    liste = models.select_all()
    myliste = []
    for entiter in liste:
        myliste.append(entiter.lister())
    print(myliste)
    return render_template('madb.html', title='Madeb', mydbliste=myliste)


@bp.route('/inscription', methods=['get', 'post'])
def inscription():
    formulaire = InscriptionForm()
    if formulaire.validate_on_submit():
        try :
           add_demande(formulaire)
        except ValueError as e:
            flash(e)
        else :
            flash('Enregistrement validée')

    return render_template('inscription.html',title="Inscription", form=formulaire)



