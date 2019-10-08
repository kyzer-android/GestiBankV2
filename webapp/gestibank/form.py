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

# class MultiCheckboxField(SelectMultipleField):
#     widget = widgets.ListWidget(prefix_label=False)
#     option_widget = widgets.CheckboxInput()
#
#
# class SimpleForm(Form):
#     string_of_files = ['one\r\ntwo\r\nthree\r\n']
#     list_of_files = string_of_files[0].split()
#     # create a list of value/description tuples
#     files = [(x, x) for x in list_of_files]
#     example = MultiCheckboxField('Label', choices=files)
#
# class AffectForm(FlaskForm):
#     list=['a','b','c']
#     for n in list:
#

