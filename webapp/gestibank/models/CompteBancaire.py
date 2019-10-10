from datetime import date
from flask_babel import lazy_gettext as _l
from flask import flash
import random
from webapp import db
import enum


from webapp.gestibank.models.user import User


class TypeCompte(enum.Enum):
    COURANT = 'Courant'
    DECOUVERT = 'Decouvert'
    INTERET = 'Interet'

#Class compte definissant un compte bancaire générique qui sera hérité par les different type de compte

class Comptes(db.Model):
    __tablename__ = 'compte'
    id_compte = db.Column(db.String(50), primary_key=True)
    id_client = db.Column(db.String(50), db.ForeignKey('client.id'))
    type_compte = db.Column(db.Enum(TypeCompte))
    rib = db.Column(db.String(50),unique=True)
    solde = db.Column(db.Float(20))
    date_creation = db.Column(db.Date)


    @classmethod
    def creation_compteban(cls, client):
            if client is not None:
                this_comtpe=Comptes(
                id_compte = (random.randint(1000000000, 9999999999)),
                type_compte = 'COURANT',
                date_creation = date.today(),
                rib = str(random.randint(1000000000, 9999999999)),
                solde = str(random.randint(1000, 9999)),
                id_client=client.id
                )
                User.populate(this_comtpe)
            else:
                flash(_l("Insertion Problem"))




    def to_dict(self):
        return {
                "id_compte": self.id_compte,
                "id_client":self.id_client,
                "type_compte":str(self.type_compte),
                "rib":self.rib,
                "solde": str(self.solde) +(' € '),
                "date_creation": self.date_creation,

                }

    def virement_d(self, montant):
        if (self.solde < montant):

            flash("Solde insufissant pour effectuer le virement ")
            flash('Votre Solde Actuel =  ' + str(self.solde) + ' € ')

        else:
            self.solde = (self.solde) - (montant)
            print("Opération effectuer avec succés ")
            print('le montant actuel : ',self.solde)
            flash('Operation effectuée avec succès \n')
            flash('Votre Solde Actuel =  ' + str(self.solde) + ' € ')

            return self.solde

