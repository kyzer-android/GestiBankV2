from flask import render_template
from webapp.main.email import send_mail
#Fonction qui recoit comme paramètre un utilisateur et lui envoi un email de réinit
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail(subject='Réinitialiser votre mot de passe',
              sender='noreply@gestibank.com',
              recipients=[user.email],
              text_body=render_template('auth/email/reset_password.txt',
                                        user=user, token=token),
              html_body=render_template('auth/email/reset_password.html',
                                        user=user, token=token))
