from flask_babel import Babel
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import lazy_gettext as _l

#creation des differents objet nécessaire à l'application

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()
babel = Babel()

login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
