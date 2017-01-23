import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
TEMPLATES_AUTO_RELOAD = True
SECRET_KEY = "IMGAY"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}
