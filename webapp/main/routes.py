from datetime import date
from flask import render_template
from flask_login import current_user, login_required
import os

from webapp.extension import login
from webapp.gestibank.models import User
from webapp.main import bp


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    if not current_user.is_anonymous:
        user = {'username': current_user.username}
    else:
        user = {'username': 'Guest'}
    return render_template('index.html', title="Page d'accueil et menu", user=user, date=date.today())


@login.user_loader
def user_loader(idt):
    return User.query.get(int(idt))
