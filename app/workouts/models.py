"""
workouts/models
~~~~~~~~~~~

:author: Cameron O'Brien
:e-mail: cameron.o.j@gmail.com
:github: @cameronobrien

"""

from app import db


class Exercise(db.Model):
    __tablename__ = "Exercise"

    def __repr__(self):
        return '<Movement %r>' % self.exercise_name

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exercise_name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    muscle_group_primary = db.Column(db.String(16), index=True, unique=True, nullable=False)
    muscle_group_secondary = db.Column(db.String(16), index=True, unique=True, nullable=False)
    is_compound = db.Column(db.Boolean, index=True, unique=True, nullable=False)