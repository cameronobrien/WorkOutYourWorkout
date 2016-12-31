from flask_wtf import Form
from wtforms import SubmitField, PasswordField, StringField, BooleanField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email


class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email Address', validators=[Email()])
    password = PasswordField('Password', [
        validators.data_required(),
    ])
    remember_me = BooleanField('Remember Me', default=False)
    submit = SubmitField("Register")
