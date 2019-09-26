from datetime import date

from flask import render_template, url_for, redirect, flash, Blueprint, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from webapp.auth.email import send_password_reset_email
from webapp.main.models import User
from webapp import db
from webapp.auth.form import LoginForm, ResetPasswordRequestForm, ResetPasswordForm
from webapp.auth import bp
@bp.route('/login', methods=['get', 'post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    formulaire = LoginForm()
    if formulaire.validate_on_submit():
        utilisateur = User.query.filter_by(username=formulaire.username.data).first()

        if (utilisateur is None) or (not utilisateur.check_pwd(formulaire.password.data)):
            flash('Login ou mot de passe invalide')
            return redirect(url_for('auth.login'))
        login_user(utilisateur, remember=formulaire.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='login', form=formulaire)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/reset_password_req', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    formulaire = ResetPasswordRequestForm()

    if formulaire.validate_on_submit():
        utilisateur = User.query.filter_by(email=formulaire.email.data).first()
        if (utilisateur is None):
            flash('Email innconu!!!!')
        else:
            send_password_reset_email(utilisateur)
            flash('Email Envoyer!!!!')
            return redirect(url_for('auth.login'))
    return render_template("auth/newMDP.html", title='reinitialisation', form=formulaire)


@bp.route('/reset_password/<token>', methods=['get', 'post'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)

    if  user is None:
        flash("Lien invalide!!")
        return redirect(url_for("main.index"))
    else:
        formulaire = ResetPasswordForm()
        if formulaire.validate_on_submit():
           if user.set_pwd(formulaire.password.data):
                db.session.commit()
                flash('nouveau MDP')
                return redirect(url_for("main.index"))
           else :
                return redirect(url_for('auth.reset_password',token=token))
        return render_template("auth/resetPassword.html", title="Reset Password", form=formulaire)
