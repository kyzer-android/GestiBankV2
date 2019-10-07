#Class demandecreacompte definissant une de damande de creation de compte  utilisateur et bancaire,
#contenant les methode : affectation d'un agent,validation d'un compte,creation d'un comte user,ajout d'une deamande
#a la base de données
import logging

from webapp import db
from webapp.gestibank.models.user import User
from webapp.gestibank.models.clients import Client

class DemandeCreacompte(db.Model):
    id_compte = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(120))
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    tel = db.Column(db.String(20))
    adresse = db.Column(db.String(140))
    justificatif = db.Column(db.String(20))
    affect = db.Column(db.String(50))
    valide = db.Column(db.Boolean)

    #fonction renvoyant les information contenut dans une demande sous forme d'une chaine de charactère
    def __repr__(self):
        test = (
            self.id_compte,
            self.username,
            self.password,
            self.nom,
            self.prenom,
            self.mail,
            self.tel,
            self.adresse,
            self.justificatif,
            self.valide,
            self.affect
        )
        return str(test)
    #fonction recevant un id agent et l'affectant a la objet demande en cours
    def affectation(self, agent_id):  # l'admin affect un client a un agent
        self.affect = agent_id
        db.session.commit()
        db.session.close()

    # fonction recevant un boolean et l'insert dans la validation de l'objet demande en cours
    def validation(self, valide):  # L'agent valide le client
        self.valide = valide
        db.session.commit(self)
        db.session.close()
    #fonction utilisant les variables de l'objet demandecrea en cours pour crée un nouelles utilisateur
    # def creation_compte_User(self):
    #     user=Client(
    #               username = self.username,
    #               password_hash = self.password,
    #               nom = self.nom,
    #               prenom = self.prenom,
    #               email = self.mail,
    #               tel=self.tel,
    #               adresse=self.adresse,
    #               justificatif=self.justificatif,
    #              )
    #     User.populate(user)
    #Methode de Classe permettant l'ajout d'une nouvelle demande dans la tables demandecreacompte
    @classmethod
    def add_demande(cls,formulaire):  # Stocakge d'une demmande dans la base de donnee (table demande)
        demande = DemandeCreacompte(

            username=formulaire.username.data,
            nom=formulaire.nom.data,
            prenom=formulaire.prenom.data,
            password=User.password(formulaire.password.data),
            mail=formulaire.mail.data,
            tel=formulaire.tel.data,
            adresse=formulaire.adresse.data,
            justificatif=formulaire.justificatif.data
        )
        User.populate(demande)
