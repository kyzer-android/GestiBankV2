from datetime import datetime
import json
from webapp import create_app
from webapp.gestibank.models.admin import Admin
from webapp.extension import db
from webapp.gestibank.models.agents import Agent
from webapp.gestibank.models.transaction import Transaction
from webapp.gestibank.models.user import User
from webapp.gestibank.models.clients import Client
from webapp.gestibank.models.CompteBancaire import Comptes
import random

class Peuplement():
    app = create_app()
    app_context = app.app_context()
    app_context.push()

    @classmethod
    def peuplement_agent(cls):


        admin=Admin(username="admin",nom='durant',prenom='pierre',password_hash=User.password('123456789'),email='admin@gestibank.com')
        db.session.add(admin)
        db.session.commit()
        db.session.close()

        strDate = '2/4/18'
        agent1=Agent(username="agent01",nom='duteil',prenom='mark',password_hash=User.password('123456789'),
                     email='mark.duteil@gestibank.com',tel='0398742365',debut_contrat=datetime.strptime(strDate, '%m/%d/%y'))
        db.session.add(agent1)
        db.session.commit()
        db.session.close()

        strDate = '8/24/02'
        agent2 = Agent(username="agent02", nom='philips', prenom='Maurice', password_hash=User.password('123456789'),
                       email='maurice.philips@gestibank.com',tel='0678954125',debut_contrat=datetime.strptime(strDate, '%m/%d/%y'))
        db.session.add(agent2)
        db.session.commit()
        db.session.close()

        strDate = '6/12/08'
        agent3 = Agent(username="agent03", nom='lamotte', prenom='jean', password_hash=User.password('123456789'),
                       email='jean.lamotte@gestibank.com',tel='014256983519',debut_contrat=datetime.strptime(strDate, '%m/%d/%y'))
        db.session.add(agent3)
        db.session.commit()
        db.session.close()

        strDate = '12/21/10'
        agent4 = Agent(username="agent04", nom='Moore', prenom='pascal', password_hash=User.password('123456789'),
                       email='pascal.Moore@gestibank.com',tel='0135986570',debut_contrat=datetime.strptime(strDate, '%m/%d/%y'))
        db.session.add(agent4)
        db.session.commit()
        db.session.close()

        strDate = '8/15/06'
        agent5 = Agent(username="agent06", nom='Macqueen', prenom='steeve', password_hash=User.password('123456789'),
                       email='steeve.Macqueen@gestibank.com', tel='0698426598',
                       debut_contrat=datetime.strptime(strDate, '%m/%d/%y'))
        db.session.add(agent5)
        db.session.commit()
        db.session.close()

        strDate = '8/4/12'
        agent6 = Agent(username="agent05", nom='lecocq', prenom='yves', password_hash=User.password('123456789'),
                       email='yves.lecocq@gestibank.com',tel='0698753695',debut_contrat=datetime.strptime(strDate, '%m/%d/%y'))
        db.session.add(agent6)
        db.session.commit()
        db.session.close()



    @classmethod
    def peuplement_user(cls):
        with open('client.json', 'r') as JSON:
            json_dict = json.load(JSON)
        for dict in json_dict:
            client = Client(username=dict['nom'], nom=dict['nom'], prenom=dict['prenom'], password_hash=User.password('123456789'),
                            email=dict['email'], tel=dict['tel'], adresse=dict['adresse'],id_agent=dict['id_agent'])
            db.session.add(client)
            db.session.commit()
            Comptes.creation_compteban(client)
            Comptes.creation_compteban(client)
            db.session.close()

    @classmethod
    def peuplement_transaction(cls):
        list=Comptes.query.all()
        id_compte_list=[]
        for lst in list:
          id_compte_list.append(lst.to_dict()['id_compte'])

        with open('transaction.json', 'r') as JSON:
            json_dict = json.load(JSON)
           
        for dict in json_dict:
            num_compte=random.choice(id_compte_list)
            compte=Comptes.query.get(num_compte)
            compte.solde=compte.solde-dict['montant_operation']
            transaction = Transaction(montant_operation=dict['montant_operation'], libeler_operation=dict['libeller_operation'], nouveau_solde=compte.solde,
                            personne_tiers=dict['personne_tiers'], id_compte=num_compte,type_operation=dict['type_operation'])
            db.session.add(transaction)
            db.session.commit()
            db.session.close()



if __name__ == "__main__":
    Peuplement.peuplement_agent()
    Peuplement.peuplement_user()
    Peuplement.peuplement_transaction()