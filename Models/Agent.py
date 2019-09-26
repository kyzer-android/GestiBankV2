from Models.login import TypeUser
from webapp import db
from flask_login import UserMixin



class Agents(UserMixin,db.Model):
    __tablename__ = 'agent'
    username = db.Column(db.String(50), primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    tel = db.Column(db.String(20))
    debut_contrat = db.Column(db.Date)
    client = db.relationship('Clients', backref='client', lazy='dynamic')
    password = db.Column(db.String(50))
    type_user = db.Column(db.Enum(TypeUser))

