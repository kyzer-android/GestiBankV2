from flask_login import UserMixin
from Models.login import TypeUser
from webapp import db


class Clients(UserMixin,db.Model):
    __tablename__ = 'client'
    username = db.Column(db.String(50), primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    tel = db.Column(db.String(20))
    adresse = db.Column(db.String(140))
    justificatif = db.Column(db.String(20))
    id_agent = db.Column(db.String(50), db.ForeignKey('agent.username'))
    compte = db.relationship('Comptes', backref='compte', lazy='dynamic')
    password = db.Column(db.String(50))
    type_user = db.Column(db.Enum(TypeUser))
