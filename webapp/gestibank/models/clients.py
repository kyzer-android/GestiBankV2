#Classe Client  héritant du compte User et contenant les methodes:
#Afficher les compte bancaires,Réaliser des virements,afficher historique des transaction
#sur un mois donné,imprimer des transactions
from webapp import db
from webapp.gestibank.models.user import User


class Client(User):
    __tablename__ = 'client'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    tel = db.Column(db.String(20))
    adresse = db.Column(db.String(140))
    justificatif = db.Column(db.String(20))
    # id_agent = db.Column(db.String(50), db.ForeignKey('agent.id'))
    # compte = db.relationship('Comptes', backref='compte', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity':'client',
    }
