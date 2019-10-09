import logging
import random
from datetime import date
from flask import flash
from werkzeug.security import generate_password_hash
from webapp import db
from webapp.auth.email import send_first_password_reset_email
from webapp.gestibank.models.agents import Agent
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte
from webapp.gestibank.models.user import User

#Classe administrateur  héritant du compte User et contenant les methodes:
#lister les demande de creation de compte,affecter une demande de creation de compte,
#création,modification,supression d'un agent un compte agent
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
        pwd=str(random. randint(10000, 50000))
        agent = Agent(
            username=formulaire.username.data,
            nom=formulaire.nom.data,
            prenom=formulaire.prenom.data,
            password_hash=generate_password_hash(pwd),
            email=formulaire.mail.data,
            tel=formulaire.tel.data,
            debut_contrat=date.today()
       )
        db.session.add(agent)
        db.session.commit()
        send_first_password_reset_email(agent)
        flash ("compte crée et email envoyer")
        db.session.close()

    @classmethod
    def modifier_agent(cls,formulaire,agent):  # Stocakge d'une demmande dans la base de donnee (table demande)
        logging.debug(formulaire)
        if formulaire.username.data is not '':
             agent.username=formulaire.username.data
        if formulaire.nom.data is not '':
            agent.nom=formulaire.nom.data
        if formulaire.prenom.data is not '':
             agent.prenom=formulaire.prenom.data
        if formulaire.mail.data is not '':
            agent.email=formulaire.mail.data
        if formulaire.tel.data is not '':
            agent.tel = formulaire.tel.data
        db.session.commit()
        flash("compte Agent Modifier")

    @classmethod
    def lister_agent(cls):
        agents=Agent.query.all()
        list_agents=[]
        for agent in agents:
            list_agents.append(agent.todict())
            param=agent.list_param()
        list=(param,list_agents)
        return list

