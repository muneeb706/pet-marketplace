"""
Contains Models definition for database tables
"""

from core import db
from .animal import animal_factory


class Owner(db.Model):
    __tablename__ = "owner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, unique=True, nullable=False)
    # one-to-many relation
    pets = db.relationship("Pet", backref="owner")


class Pet(db.Model):
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String, unique=True, nullable=False)
    owner_name = db.Column(db.String, db.ForeignKey('owner.fullname'), nullable=True)
    type = db.Column(db.String, nullable=False)

    @property
    def serialize(self) -> dict:
        """
        This property is used to convert model instance into a dictionary object
        """

        return {
            'type': self.type,
            'serial_number': self.serial_number,
            'owner': self.owner_name,
            'sound': animal_factory(self.type).speak()
        }
