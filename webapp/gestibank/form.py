from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, SelectField, FloatField
from wtforms.validators import DataRequired, Email, Length, Optional, EqualTo
from webapp.gestibank.models.admin import Admin


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
    delete = BooleanField(_l("Delete account"))
    username = StringField(_l("Connexion identifier"))
    nom = StringField(_l("FirstName"))
    prenom = StringField(_l("Surname"))
    mail = StringField(_l("Email"))
    tel = StringField(_l("Phone number"))
    submit = SubmitField(_l('Send'))

class ValidedemandFrom(FlaskForm):
    valide = RadioField("Valide", choices=[('True', 'Validation'),('False', 'En attente'),('None', 'Ne rien faire')])
    submit = SubmitField(_l('Send'))



class AffectdemandFrom(FlaskForm):
    affect = SelectField(u'Programming Language')
    submit = SubmitField(_l('Send'))

class VirementForm(FlaskForm):
    username = StringField(_l("Nom destinataire"), validators=[Length(min=8, max=25)])
    rib = StringField(_l("Rib_Destinataire"), validators=[Length(min=8, max=30)])
    montant = FloatField(_l('Montant'))
    motif = StringField(_l("Motif virement"))

    submit = SubmitField(_l('Valider'))


class OperationForm(FlaskForm):
    submit1 = SubmitField(_l('Virement'))
    submit2 = SubmitField(_l('Demande Chequier'))
    submit3 = SubmitField(_l('Contacter votre Conseiller'))
