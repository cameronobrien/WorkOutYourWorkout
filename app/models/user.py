from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from app.helpers import JsonSerializer, get_current_time
import app.constants
from app import db


class UserJsonSerializer(JsonSerializer):
    __json_public__ = ['id', 'email', 'username']
    __json_modifiers__ = {
        'role_code': ['role', (lambda code: app.constants.USER_ROLE[code])]

    }


class User(db.Model, UserMixin, UserJsonSerializer):
    __tablename__ = "user"

    def __repr__(self):
        return '<User %r>' % self.username

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), index=True, unique=True, nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=get_current_time())
    role_code = db.Column(db.SmallInteger, default=app.constants.USER, nullable=False)
    user_password = db.Column('password', db.String(36), nullable=False)

    def get_password(self):
        return self.user_password

    def set_password(self):
        self.user_password = generate_password_hash(user_password)

    password = db.synonym('user_password',
                          descriptor=property(get_password,
                                              set_password))
    def check_password(self,password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter(db.or_(User.username == username)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    @classmethod
    def is_user_taken(cls, username):
        return db.session.query(db.exists().where(User.username == username)).scalar()

    @classmethod
    def is_email_taken(cls, email):
        return db.session.query(db.exists().where(User.email == email)).scalar()





