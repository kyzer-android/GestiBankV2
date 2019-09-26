from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_babel import lazy_gettext as _l

class LoginForm(FlaskForm):
    username = StringField(_l('User'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember me'))
    submit = SubmitField(_l('Connect'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l(' Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l('Password Confirmation'),validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Reset Password'))
