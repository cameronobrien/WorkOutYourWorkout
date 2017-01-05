import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.login_view = ''
login_manager.refresh_view = ''


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
login_manager.init_app(app)


csrf = CsrfProtect()
csrf.init_app(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

from app import views
from app.models.user import User


