# Classe Agent  héritant du compte User et contenant les methodes:
# Valider et cree  les demande de creation de compte,filtrer les demandes d'ouvertures de comptes,
# Configurer et modifier les comptes client, effectuer des recherche aves et sans filtres sur les compte client,
# Afficher les opperation d'un client sur les 12 derniers mois,valider les demande de chequier et les facilité de caisses

from webapp import db
from webapp.gestibank.models.CompteBancaire import Comptes
from webapp.gestibank.models.clients import Client
from webapp.gestibank.models.user import User
from webapp.gestibank.models.demandecreacompte import DemandeCreacompte


class Agent(User):
    __tablename__ = 'agent'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    tel = db.Column(db.String(20))
    debut_contrat = db.Column(db.Date)
    # client = db.relationship('Clients', backref='client', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'agent',
    }

    def todict(self):
        test = {
           'id': str(self.id),
           'username': self.username,
           'nom': self.nom,
           'prenom': self.prenom,
           'email':self.email,
           'type': self.type,
           'tel': self.tel,
           'debut_contrat': str(self.debut_contrat)
        }
        return test

    #Liste les demandes de créations OK
    def lister_demandecrea(self):
        demandecrea = db.session.query(DemandeCreacompte).filter(DemandeCreacompte.affect == self.id).all()
        list_demandecrea=[]
        for demande in demandecrea:
            list_demandecrea.append(demande.todict())
        return list_demandecrea

    # Retourne les clients gérée par l'agent NOK
    def filtre_clients(self):
        return db.session.query(DemandeCreacompte).filter(DemandeCreacompte.affect == self.id,
                                                          DemandeCreacompte.valide != True ).all()

    # Validation création d'ouverture de compte NOK
    def validation_Crea(self, objet_demandecrea, valid_crea: bool):
        objet_demandecrea.validation(valid_crea)
        if objet_demandecrea.valide is True:  # Si la demande est validé, création du compte, envoi un mail avec login/mdp + mis en True
            client = self.cree_client(objet_demandecrea) #Creer un client
            db.session.add(client)
            db.session.commit()
            Comptes.creation_compteban(client)  # Création compte banquaire
            # TODO envoi de mail avec id/mdp
            return True
        elif objet_demandecrea.valide is False:  # Si la demande n'est pas valider = envoi de mail demande info + mis en False
            pass  # TODO envoi de mail avec une demande d'info supplementaire
            return True
        else:  # Erreur
            return  False

    #Création du compte Client à partir des données du de demandecrecompte NOK
    def cree_client(self, objet_demandecrea):
        client = Client(
            username=objet_demandecrea.username,
            password_hash = objet_demandecrea.password,
            nom = objet_demandecrea.nom,
            prenom = objet_demandecrea.prenom,
            email=objet_demandecrea.mail,
            tel=objet_demandecrea.tel,
            adresse=objet_demandecrea.adresse,
            justificatif=objet_demandecrea.justificatif,
            id_agent=self.id
             )
        return client


    #
    #
    #     def modif_compte_User(self):  # Modification compte client
    #         pass
    #
    #     def valid_cheque(self):  # Validation demande chéquier
    #         pass
    #
    #     def valid_facilite(self):  # Validation facilité de caisse
    #         pass
    # """

