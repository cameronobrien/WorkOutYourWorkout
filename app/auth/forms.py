"""
auth/forms
~~~~~~~~~~

:author: Cameron O'Brien
:e-mail: cameron.o.j@gmail.com
:github: @cameronobrien

"""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email


class LoginForm(FlaskForm):
    login = StringField('user_name', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
    submit = SubmitField("Log In")


class RegisterForm(FlaskForm):
    username = StringField('user_name', [validators.Length(min=4, max=25)])
    email = EmailField('email', validators=[Email()],)
    password = PasswordField('password', [
        validators.Length(min=6, max=36),
        validators.data_required(),
    ])
    confirm = PasswordField('confirm', validators=[
        validators.data_required(),
        validators.equal_to('password', message="Passwords must match.")
    ])

    submit = SubmitField("Register!")
