from .models import Owner
from .db import Database
import uuid


class OwnerController:

    @classmethod
    def __generate_username(cls, fullname):
        username = fullname.lower().replace(' ', '')
        username += str(uuid.uuid4())[:5]
        return username

    def get_owner(self, identifier):
        owner_q = Owner.query.filter((Owner.fullname == identifier) | (Owner.username == identifier)).first()
        return owner_q

    def insert_owner(self, fullname):
        username = self.__generate_username(fullname)
        owner_o = Owner(username=username, fullname=fullname)
        Database.insert(owner_o)
        return self.get_owner(username)
