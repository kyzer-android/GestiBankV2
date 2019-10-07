from flask import Flask, request, session, current_app
from config import Config

from webapp.extension import db, migrate, login, mail, babel
from webapp.main import bp as main_bp
from webapp.auth import bp as auth_bp
from webapp.api import bp as api_bp
from webapp.gestibank import bp as gesti_bp

#Fonction de création de l'application et d'initialisation des diferents objets de l'application

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    mail.init_app(app)
    babel.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(gesti_bp)
    with app.app_context():
        from webapp.main import filter
    return app


@babel.localeselector
def get_local():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang',request.accept_languages.best_match(current_app.config['LANGUAGES']))



