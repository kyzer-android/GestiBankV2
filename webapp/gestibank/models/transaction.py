
import enum

from webapp import db


class TypeOP(enum.Enum):
    cb = 'CB'
    cheque = 'chèque'
    virement = 'virement'

class Transaction(db.Model):
    id_operation = db.Column(db.Integer, primary_key=True)
    montant_operation=db.Column(db.Integer)
    libeler_operation=db.Column(db.String(50))
    nouveau_solde=db.Column(db.Integer)
    type_operation=db.Column(db.Enum(TypeOP))
    personne_tiers=db.Column(db.String(50))
    id_compte = db.Column(db.Integer, db.ForeignKey('compte.id_compte'))
    date_operation = db.Column(db.Date)


    def todict(self):
        return {
                "id_operation": self.id_operation,
                "montant_operation":self.montant_operation,
                "libeler_operation":self.libeler_operation,
                "nouveau_solde":self.nouveau_solde,
                "type_operation": self.type_operation,
                "personne_tiers": self.personne_tiers,
                "date_operation":str(self.date_operation)

                }

    @classmethod
    def lister_transaction(cls,id_compte):
        clients = db.session.query(Transaction).filter(Transaction.id_compte == id_compte).all()
        list_transaction=[]
        for demande in clients:
            list_transaction.append(demande.todict())
        return list_transaction