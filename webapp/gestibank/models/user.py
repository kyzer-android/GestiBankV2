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
    def password(cls, pwd):
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
            if password_check['password']is None or password_check['password'] == user.password_hash:
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
        if self.password_hash is None:
            return False
        else:
            return check_password_hash(self.password_hash, pwd)

    #fonction de creation du token de réinitialisation de mot de passe
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'password': self.password_hash, 'exp': time() + expires_in},
                          current_app.config['SECRET_KEY'],
                          algorithm='HS256').decode('utf-8')
