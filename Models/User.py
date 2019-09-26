from _py_abc import ABCMeta
from webapp import db
from sqlalchemy.ext.declarative import declarative_base, ConcreteBase

from webapp import db
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class CommonUser(Base):
    __tablename__ = 'commonuser'
    # __metaclass__= ABCMeta
    username = db.Column(db.String(50), primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    mail = db.Column(db.String(50))

    def __repr__(self):
        return '<Utilisateur {}>'.format(self.username)

# class Admin(CommonUser):
#     __tablename__ = 'admin'
#     username = db.Column(db.String(50), primary_key=True)
#     nom = db.Column(db.String(50))
#     prenom = db.Column(db.String(50))
#     mail = db.Column(db.String(50))
#     __mapper_args__ = {"polymorphic_identity": "admin", "concrete": True}




