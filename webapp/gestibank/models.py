from time import time
from flask_babel import gettext as _
import jwt
from flask import flash, current_app, url_for
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect
from webapp.extension import db



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



    @classmethod
    def password(self, pwd):
        return generate_password_hash(pwd)

    def __repr__(self):
        return '<Utilisateur {}>'.format(self.username)

    @classmethod
    def populate(cls,*args):
        for user in args:
            db.session.add(user)
        db.session.commit()
        db.session.close()
        #TODO raise exeption

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

    def update(self):
        db.session.commit()
        db.session.close()


    def lister(self):
        liste = [self.type,self.id, self.username,self.nom,self.prenom, self.email]
        print(liste)
        return liste

    def set_pwd(self, pwd):
        if not self.check_pwd(pwd):
            self.password_hash = generate_password_hash(pwd)
            return True
        else:
            flash(_('This password has allredy been used'))
            return False

    def check_pwd(self, pwd):
        return check_password_hash(self.password_hash, pwd)


    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'password': self.password_hash, 'exp': time() + expires_in},
                          current_app.config['SECRET_KEY'],
                          algorithm='HS256').decode('utf-8')



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

    def affectation(self, agent):  # l'admin affect un client a un agent
        self.affect = agent
        db.session.commit(self)
        db.session.close()

    def validation(self, valide):  # L'agent valide le client
        self.valide = valide
        db.session.commit(self)
        db.session.close()

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
