from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email


class RegistrationForm(FlaskForm):
    username = StringField('user_name', [validators.Length(min=4, max=25)],)
    email = EmailField('email', validators=[Email()])
    password = PasswordField('password', [
        validators.Length(min=8, max=36),
        validators.data_required(),
    ])
    confirm = PasswordField('confirm'), [
        validators.DataRequired(),
        validators.equal_to('password', message="Passwords must match.")
    ]

