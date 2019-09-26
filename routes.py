import Models.CreaCompte as demande
from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from webapp import app
import os
from webapp.form import InscriptionForm


@app.route('/')
@app.route('/index')
def index():
    if not current_user.is_anonymous:
        user = {'username': current_user.username}
    else:
        user = {'username': 'Guest'}
    return render_template('index.html', title="Page d'accueil et menu", user=user)





@app.route('/login', methods=['get', 'post'])
def login():
    pass


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


