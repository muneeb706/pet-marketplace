from core import db


class Owner(db.Model):
    __tablename__ = "owner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, unique=True, nullable=False)
    pets = db.relationship("Pet", backref="owner")


class Pet(db.Model):
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String, unique=True, nullable=False)
    owner_name = db.Column(db.String, db.ForeignKey('owner.fullname'), nullable=True)
