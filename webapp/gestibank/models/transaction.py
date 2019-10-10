
import enum

from webapp import db


class TypeOP(enum.Enum):
    cb = 'CB'
    cheque = 'chèque'
    virement = 'virement'

class transaction(db.Model):
    id_operation = db.Column(db.Integer, primary_key=True)
    Montant_operation=db.Column(db.Integer)
    libeler_operation=db.Column(db.String(50))
    nouveau_solde=db.Column(db.Integer)
    type_operation=db.Column(db.Enum(TypeOP))
    personne_tiers=db.Column(db.String(50))
    id_compte = db.Column(db.Integer, db.ForeignKey('compte.id_compte'))

