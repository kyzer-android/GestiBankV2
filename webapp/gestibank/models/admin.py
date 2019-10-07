
#Classe administrateur  héritant du compte User et contenant les methodes:
#lister les demande de creation de compte,affecter une demande de creation de compte,
#création,modification,supression d'un agent un compte agent
from webapp import db
from webapp.gestibank.models.user import User


class Admin(User):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }
    # #lister toute les demande de compte
    # def lister_demand_crea(self):
    #     return DemandeCreacompte.query.all()
    #
    # #affecter une demande
    # def affecter_demande(self, demande, agent):
    #     demande.affectation(agent)

