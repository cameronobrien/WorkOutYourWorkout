from app import db


class Workout(db.Model):
    __tablename__ = "workout"


    def __repr__(self):
        return '<Workout %r>' % self.name

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), index=True, unique=True, nullable=False)
    muscle_group = db.Column(db.String(16), index=True,unique=True, nullable=False)
    compound = db.Column(db.Boolean(), nullable=False, default=False)

    def __init__(self, exercise, group, compoundmovement):
        self.name = exercise
        self.muscle_group = group
        self.compound = compoundmovement

    def get_name(self):
        return self.name

    def get_muscle_group(self):
        return self.muscle_group

    def get_compound(self):
        return self.compound
