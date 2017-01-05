from flask_wtf import Form
from wtforms import SubmitField, PasswordField, StringField, BooleanField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)], validators.Regexp("^[a-zA-Z0-9]*$",
                            message="Username can only contain letters and numbers"))
    email = EmailField('Email Address', validators=[Email()])
    password = PasswordField('Password', [
        validators.Length(min=8, max=36),
        validators.data_required(),
        validators.equal_to('confirm', message="Passwords must match.",
        )
    ])
    confirm = PasswordField('Confirm password.'), [
        validators.DataRequired()
    ]
    accept_tos = BooleanField('I accept the ToS', [validators.data_required()])
    submit = SubmitField("Register")

