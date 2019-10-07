from datetime import date
from flask import render_template
from flask_login import current_user

from webapp.extension import login
from webapp.gestibank.models import User
from webapp.main import bp

#Renvoi la page d'index générale
@bp.route('/')
@bp.route('/index')
def index():
    if not current_user.is_anonymous:
        user = {'username': current_user.username}
    else:
        user = {'username': 'Guest'}
    return render_template('index.html', title="Page d'accueil et menu", user=user, date=date.today())


#fonction de verification de l'utilisateur connecter necessaire au module login
@login.user_loader
def user_loader(idt):
    return User.query.get(int(idt))
