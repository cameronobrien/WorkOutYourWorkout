from flask_wtf import Form
from wtforms import PasswordField, StringField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email


class RegistrationForm(Form):
    username = StringField('user_name', [validators.Length(min=4, max=25)], validators.Regexp("^[a-zA-Z0-9]*$",
                            message="Username can only contain letters and numbers"))
    email = EmailField('email', validators=[Email()])
    password = PasswordField('password', [
        validators.Length(min=8, max=36),
        validators.data_required(),
    ])
    confirm = PasswordField('Confirm password.'), [
        validators.DataRequired(),
        validators.equal_to('password', message="Passwords must match.")
    ]

