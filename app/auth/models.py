import hashlib
from flask_login import UserMixin
from app.helpers import get_current_time
from app import db
m = hashlib.sha512()


class User(db.Model, UserMixin):
    __tablename__ = "user"

    def __repr__(self):
        return '<User %r>' % self.user_name

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), index=True, unique=True, nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=get_current_time())
    _password = db.Column('password', db.String(64), nullable=False)

    def get_password(self):
        return self._password

    def set_password(self, password):
        m = hashlib.sha512()
        m.update(password.encode('utf-8'))

    password = db.synonym('_password',
                          descriptor=property(get_password,
                                              set_password))

    @classmethod
    def authenticate(cls, user_name, password):
        user = User.query.filter(db.or_(User.user_name == user_name)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    @classmethod
    def is_user_name_taken(cls, user_name):
        return db.session.query(db.exists().where(User.user_name == user_name)).scalar()

    @classmethod
    def is_email_taken(cls, email_address):
        return db.session.query(db.exists().where(User.email == email_address)).scalar()





