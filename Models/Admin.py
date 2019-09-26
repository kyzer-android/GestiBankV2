from flask_login import UserMixin

from webapp import db



class Admin(UserMixin,db.Model):
    __tablename__ = 'admin'
    username = db.Column(db.String(50), primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    password = db.Column(db.String(50))
    type_user = db.Column(db.Enum(TypeUser))
