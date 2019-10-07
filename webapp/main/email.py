from flask import current_app
from flask_mail import Message
from webapp import mail

from threading import Thread

#Thread d'envoi de mail
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

#Fonction d'envoi de mail
def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()

