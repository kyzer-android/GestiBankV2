from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, Length, Optional


class InscriptionForm(FlaskForm):
    username = StringField("Identifiant de connexion",[validators.Length(min=8, max=25)])
    password = PasswordField("mot de passe de connexion", [validators.Length(min=8, max=25)])
    nom = StringField("Nom", validators=[DataRequired()])
    prenom = StringField("Prenom", validators=[DataRequired()])
    mail = StringField("mail", validators=[DataRequired(), Email()])
    tel = StringField("Téléphone", validators=[DataRequired(), Length(10)])
    adresse = StringField("Adresse", validators=[DataRequired()])
    justificatif = StringField("Justificatif", validators=[Optional()])
    submit = SubmitField('Envoyer')

