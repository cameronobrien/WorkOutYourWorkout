from flask.ext.wtf import Form
from wtforms import SubmitField, PasswordField, StringField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email


class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email Address', validators=[Email()])
    password = PasswordField('Password', [
        validators.data_required(),
    ])
    submit = SubmitField("Register")
