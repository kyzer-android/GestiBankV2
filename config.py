import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ma_cle_secrete'

    # init SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'app.db')) + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    LANGUAGES = ['en', 'fr','de']
# from flask.ext.script import Manager
# init SQLAlchemy and Flask-Script
# manager = Manager(app)
