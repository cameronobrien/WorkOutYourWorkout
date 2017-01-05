from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, validators


class LoginForm(FlaskForm):
    login = StringField('user_name', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
