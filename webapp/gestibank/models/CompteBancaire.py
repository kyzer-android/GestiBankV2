import logging
import os.path
from datetime import date
from flask_babel import lazy_gettext as _l
from flask import flash, current_app
import random
import matplotlib.pyplot as plt
from sqlalchemy import asc
from webapp.extension import db

#from webapp import Chemin
import enum


from webapp.gestibank.models.transaction import Transaction
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
                "type_compte":(self.type_compte).name,
                "rib":self.rib,
                "solde": str(self.solde) +(' € '),
                "date_creation": self.date_creation,

                }

    def virement_d(self, formulaire):
        montant=formulaire.montant.data
        destinataire=Comptes.query.filter_by(rib=formulaire.rib.data).first()

        if (montant>0):
            if (self.solde <  montant):

                flash("Solde insufissant pour effectuer le virement ")
                flash('Votre Solde Actuel =  ' + str(self.solde) + ' € ')

            elif destinataire is not None :

                self.solde -= montant
                destinataire.solde += montant
                print("Opération effectuée avec succés ")
                print('Le montant actuel : ', self.solde)
                flash('Operation effectuée avec succès \n')
                flash('Votre Solde Actuel =  ' + str(self.solde) + ' € ')
                #transaction de l'emeteur
                transaction = Transaction(montant_operation=-montant,
                                        libeler_operation=formulaire.motif.data, nouveau_solde=self.solde,
                                         personne_tiers=formulaire.destinataire.data, id_compte=self.id_compte,
                                          type_operation='virement',date_operation=date.today())
                db.session.add(transaction)
                #transaction du destinataire
                transaction2 = Transaction(montant_operation=montant,
                                          libeler_operation=formulaire.motif.data, nouveau_solde=destinataire.solde,
                                          personne_tiers=formulaire.username.data, id_compte=destinataire.id_compte,
                                          type_operation='virement', date_operation=date.today())

                db.session.add(transaction2)

                db.session.commit()


        else :
                flash('Erreur de montant')

    def graph_transaction(self):
        transaction = db.session.query(Transaction).filter(Transaction.id_compte == self.id_compte).order_by(asc(Transaction.date_operation)).all()
        list_transaction = []
        liste_date_transaction = []
        for trans in transaction:
            list_transaction.append(trans.todict()['nouveau_solde'])

            liste_date_transaction.append(trans.todict()['date_operation'])
        logging.info("solde", list_transaction)
        logging.info("date", liste_date_transaction)
        plt.figure(figsize=(13, 4))
        plt.plot(liste_date_transaction, list_transaction)
        plt.xlabel('date')
        plt.ylabel('solde')
        chemin= os.path.join(current_app.chemin+"\static\img\img_compte\\",self.id_compte+".png")
        plt.savefig(chemin)
        return(chemin)
