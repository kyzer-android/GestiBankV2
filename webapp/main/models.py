from datetime import datetime
from time import time
from flask import flash, url_for, current_app
from flask_login import UserMixin
from werkzeug.utils import redirect
from webapp.extension import db, login
from werkzeug.security import generate_password_hash, check_password_hash
import jwt


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):

        resources = query.paginate(page, per_page, False)

        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page, **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data


class User(PaginatedAPIMixin,UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), index=True, unique=True)
    email = db.Column(db.String(40), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

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

    def lister(self):
        liste = [self.id, self.username, self.email, self.password_hash]
        print(liste)
        return liste

    def set_pwd(self, pwd):
        if not self.check_pwd(pwd):
            self.password_hash = generate_password_hash(pwd)
            return True
        else:
            flash('mot de passe déja utiliser veulliez changer merci')
            return False

    def check_pwd(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'password': self.password_hash, 'exp': time() + expires_in},
                          current_app.config['SECRET_KEY'],
                          algorithm='HS256').decode('utf-8')

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

    def to_dict(self, include_email=False):
        data = {
                'id': self.id,
                'username': self.username,
                'post_count': self.posts.count(),
                '_links': {
                'self': url_for('api.get_user', id=self.id),
                'posts': url_for('api.get_posts', id=self.id)
                }
        }
        if include_email:
            data['email'] = self.email
        return data



    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
            if new_user and 'password' in data:
                self.set_password(data['password'])



class Post(PaginatedAPIMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        data = {
                'id': self.id,
                'body': self.body,
                'timestamp': self.timestamp,
                '_links': {
                'self': url_for('api.get_post', id=self.id),
                'user': url_for('api.get_user', id=self.user_id)
                }
        }
        return data



    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader
def user_loader(idt):
    return User.query.get(int(idt))


def select_all():
    users = User.query.all()
    return users



