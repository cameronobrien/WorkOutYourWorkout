import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


lm = LoginManager()
lm.login_view = ''
lm.refresh_view = ''


@lm.user_loader
def load_user(id):
    return auth.models.User.query.get(id)
lm.init_app(app)


csrf = CsrfProtect()
csrf.init_app(app)

from app.admin import models, forms, views
from app.index import models, forms, views
from app.auth import models, forms, views

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')



