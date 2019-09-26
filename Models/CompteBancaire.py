from webapp import db
import enum

class TypeCompte(enum.Enum):
    COURANT = 'Courant'
    DECOUVERT = 'Decouvert'
    INTERET = 'Interet'


class Comptes(db.Model):
    id_compte = db.Column(db.String(50), primary_key=True)
    id_client = db.Column(db.String(50), db.ForeignKey('client.username'))
    type_compte = db.Column(db.Enum(TypeCompte))
    rib = db.Column(db.String(50))
    solde = db.Column(db.Float(20))
    date_creation = db.Column(db.Date)


