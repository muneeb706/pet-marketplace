from .models import Owner, Pet
from .db import Database
from .utils import get_uuid_str


class OwnerController:

    @classmethod
    def __generate_username(cls, fullname):
        username = fullname.lower().replace(' ', '')
        username += get_uuid_str()[:5]
        return username

    def get_owner(self, identifier):
        owner_q = Owner.query.filter((Owner.fullname == identifier) | (Owner.username == identifier)).first()
        return owner_q

    def get_pets(self, username):
        owner_q = Owner.query.filter(Owner.username == username).first()
        return owner_q.pets

    def insert_owner(self, fullname):
        username = self.__generate_username(fullname)
        owner_o = Owner(username=username, fullname=fullname)
        Database.insert(owner_o)
        return self.get_owner(username)


class PetController:

    def insert(self, pet_type, owner_name):
        pet_o = Pet(serial_number=get_uuid_str(), owner_name=owner_name, type=pet_type)
        Database.insert(pet_o)

    @staticmethod
    def get_all():
        return Pet.query.all()


