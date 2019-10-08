from datetime import date
from flask_babel import lazy_gettext as _l
from flask import flash
from sqlalchemy.sql.functions import random
from webapp import db
import enum

from webapp.gestibank.models.user import User


class TypeCompte(enum.Enum):
    COURANT = 'Courant'
    DECOUVERT = 'Decouvert'
    INTERET = 'Interet'

#Class compte definissant un compte bancaire générique qui sera hérité par les different type de compte

class Comptes(db.Model):
    id_compte = db.Column(db.String(50), primary_key=True)
    id_client = db.Column(db.String(50), db.ForeignKey('client.id'))
    type_compte = db.Column(db.Enum(TypeCompte))
    rib = db.Column(db.String(50))
    solde = db.Column(db.Float(20))
    date_creation = db.Column(db.Date)

    @classmethod
    def creation_compteban(cls, id_client):
            client = User.query.get(id_client)
            if client is not None:
                this_comtpe=Comptes(
                id_compte = (random.randint(1000000000, 9999999999)),
                type_compte = 'COURANT',
                date_creation =  str (date.today()),
                rib = str(random.randint(1000000000, 9999999999)),
                solde = 0.0,
                id_client=id_client
                )
                User.populate(this_comtpe)
            else:
                flash(_l("Insertion Problem"))

    def solvabilite(self,valeur_virement=0):
        return self.sode >= valeur_virement