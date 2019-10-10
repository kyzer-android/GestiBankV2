from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm, widgets
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, Optional, EqualTo

#Formulaire de demande de creation de compte utilisateur
class InscriptionForm(FlaskForm):
    username = StringField(_l("Connexion identifier"),validators=[Length(min=8, max=25)])
    password = PasswordField(_l("password"), validators=[Length(min=8, max=25)])
    test = PasswordField(_l('Password Confirmation'),validators=[DataRequired(), EqualTo('password')])
    nom = StringField(_l("FirstName"), validators=[DataRequired()])
    prenom = StringField(_l("Surname"), validators=[DataRequired()])
    mail = StringField(_l("Email"), validators=[DataRequired(), Email()])
    tel = StringField(_l("Phone number"), validators=[DataRequired(), Length(10)])
    adresse = StringField(_l("Adresse"), validators=[DataRequired()])
    justificatif = StringField(_l("Justificatif"), validators=[Optional()])
    submit = SubmitField(_l('Send'))


class AgentForm(FlaskForm):
    username = StringField(_l("Connexion identifier"),validators=[Length(min=8, max=25)])
    nom = StringField(_l("FirstName"), validators=[DataRequired()])
    prenom = StringField(_l("Surname"), validators=[DataRequired()])
    mail = StringField(_l("Email"), validators=[DataRequired(), Email()])
    tel = StringField(_l("Phone number"), validators=[DataRequired(), Length(10)])
    submit = SubmitField(_l('Send'))

class ModifagentForm(FlaskForm):

    username = StringField(_l("Connexion identifier"))
    nom = StringField(_l("FirstName"))
    prenom = StringField(_l("Surname"))
    mail = StringField(_l("Email"))
    tel = StringField(_l("Phone number"))
    submit = SubmitField(_l('Send'))


