
#Classe administrateur  héritant du compte User et contenant les methodes:
#lister les demande de creation de compte,affecter une demande de creation de compte,
#création,modification,supression d'un agent un compte agent
import random
from datetime import date

from webapp import db
from webapp.auth.email import send_password_reset_email
from webapp.gestibank.models.agents import Agent
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte
from webapp.gestibank.models.user import User


class Admin(User):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }
    #lister toute les demande de compte
    def lister_demand_crea(self):
        return DemandeCreacompte.query.all()

    #affecter une demande
    @classmethod
    def affecter_demande(cls, demande, agent_id):
        demande.affectation(agent_id)


    @classmethod
    def cree_agent(cls, formulaire):  # Stocakge d'une demmande dans la base de donnee (table demande)
        pwd=str(random.randint(10000, 50000))
        agent = Agent(
            username=formulaire.username.data,
            nom=formulaire.nom.data,
            prenom=formulaire.prenom.data,
            password=User.password(pwd),
            email=formulaire.mail.data,
            tel=formulaire.tel.data,
            debut_contrat=date.today()
       )
        db.session.add(agent)
        db.session.commit()
        db.session.close()
        # send_password_reset_email(agent)
