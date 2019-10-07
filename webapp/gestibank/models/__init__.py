from time import time
from flask_babel import gettext as _
import jwt
from flask import flash, current_app, url_for
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect
from webapp.extension import db


#Class compte definissant un compte bancaire utilisateur qui sera hérité par les different type de compte
class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(150))
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    email = db.Column(db.String(50))
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }


    #Methode de la classe User permetant la generation d'un mot de passe
    @classmethod
    def password(self, pwd):
        return generate_password_hash(pwd)

    def __repr__(self):
        return '<Utilisateur {}>'.format(self.username)
    #Methode de la classe User permetant la mise a jour de la base de donnée
    @classmethod
    def populate(cls,*args):
        for user in args:
            db.session.add(user)
        db.session.commit()
        db.session.close()
        #TODO raise exeption

    #Fonction de verification du token de réinistalisation de mot de passe
    @classmethod
    def verify_reset_password_token(self, token):
        try:
            password_check = jwt.decode(token, current_app.config['SECRET_KEY'],
                                        algorithms=['HS256'])
        except:
            flash("Erreur decodage tokken!!!!")
            return redirect(url_for('index'))
        finally:
            user = User.query.get(int(password_check['reset_password']))
            if password_check['password'] == user.password_hash:
                return (user)
            else:
                flash('token Déjà utilisé')

    # focntion de mise a jour de la base de donnée
    def update(self):
        db.session.commit()
        db.session.close()

    # focntion retournant tous les informations d'un utilisateur de types users sous forme d'une liste
    def lister(self):
        liste = [self.type,self.id, self.username,self.nom,self.prenom, self.email]
        return liste

    #fonction de génération de mot de passe
    def set_pwd(self, pwd):
        if not self.check_pwd(pwd):
            self.password_hash = generate_password_hash(pwd)
            return True
        else:
            flash(_('This password has allredy been used'))
            return False

    # fonction de verification du mot de passe utilisateur
    def check_pwd(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    #fonction de creation du token de réinitialisation de mot de passe
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'password': self.password_hash, 'exp': time() + expires_in},
                          current_app.config['SECRET_KEY'],
                          algorithm='HS256').decode('utf-8')


#Classe administrateur  héritant du compte User et contenant les methodes:
#lister les demande de creation de compte,affecter une demande de creation de compte,
#création,modification,supression d'un agent un compte agent
class Admin(User):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    # def lister_demand_crea(self,formulaire):
    #     return DemandeCreacompte.add_demande(formulaire)
    #
    # def affecter_demande(self, demande, agent):
    #     demande.affectation(agent)


#Classe Agent  héritant du compte User et contenant les methodes:
#Valider et cree  les demande de creation de compte,filtrer les demandes d'ouvertures de comptes,
#Configurer et modifier les comptes client, effectuer des recherche aves et sans filtres sur les compte client,
#Afficher les opperation d'un client sur les 12 derniers mois,valider les demande de chequier et les facilité de caisses
class Agent(User):
    __tablename__ = 'agent'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    tel = db.Column(db.String(20))
    debut_contrat = db.Column(db.Date)
    # client = db.relationship('Clients', backref='client', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'agent',
    }

    

    # def flitre_compte(self):  # Retourne les demande de création de compte avec le id agent
    #     return self.query.filter_by(self.id)
    #
    # def validation_Crea(self, objet_demandecrea, valid_crea: bool):  # Validation création d'ouverture de compte
    #     objet_demandecrea.validation(valid_crea)
    #     if objet_demandecrea.valide is True:  # Si la demande est validé, création du compte, envoi un mail avec login/mdp + mis en True
    #         # TODO envoi de mail avec id/mdp
    #         # TODO création de compte banquaire
    #         objet_demandecrea.creation_compte_User()
    #     elif objet_demandecrea.valide is False:  # Si la demande n'est pas valider = envoi de mail demande info + mis en False
    #         pass  # TODO envoi de mail avec une demande d'info supplementaire
    #     else:  # Erreur
    #         print("Erreur/En attente")
    #
    # """
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
#Classe Client  héritant du compte User et contenant les methodes:
#Afficher les compte bancaires,Réaliser des virements,afficher historique des transaction
#sur un mois donné,imprimer des transactions

class Client(User):
    __tablename__ = 'client'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    tel = db.Column(db.String(20))
    adresse = db.Column(db.String(140))
    justificatif = db.Column(db.String(20))
    # id_agent = db.Column(db.String(50), db.ForeignKey('agent.id'))
    # compte = db.relationship('Comptes', backref='compte', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity':'client',
    }


#Class demandecreacompte definissant une de damande de creation de compte  utilisateur et bancaire,
#contenant les methode : affectation d'un agent,validation d'un compte,creation d'un comte user,ajout d'une deamande
#a la base de données
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
            self.id,
            self.username,
            self.password,
            self.nom,
            self.prenom,
            self.mail,
            self.tel,
            self.adresse,
            self.justificatif,
            self.valid,
            self.affect
        )
        return str(test)
    #fonction recevant un id agent et l'affectant a la objet demande en cours
    def affectation(self, agent):  # l'admin affect un client a un agent
        self.affect = agent
        db.session.commit(self)
        db.session.close()

    # fonction recevant un boolean et l'insert dans la validation de l'objet demande en cours
    def validation(self, valide):  # L'agent valide le client
        self.valide = valide
        db.session.commit(self)
        db.session.close()
    #fonction utilisant les variables de l'objet demandecrea en cours pour crée un nouelles utilisateur
    def creation_compte_User(self):
        user=Client(
                  username = self.username,
                  password_hash = self.password,
                  nom = self.nom,
                  prenom = self.prenom,
                  email = self.mail,
                  tel=self.tel,
                  adresse=self.adresse,
                  justificatif=self.justificatif,
                 )
        User.populate(user)
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
