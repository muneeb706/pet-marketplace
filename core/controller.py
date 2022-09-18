"""
Contains static controller classes to interact with the respective models
"""
from typing import List

from .db import Database
from .models import Owner, Pet
from .utils import get_uuid_str


class OwnerController:
    """
    Controller to interact with the Owner model
    """

    @staticmethod
    def __generate_username(fullname: str) -> str:
        """
        Generates username by appending first five characters
        of uuid.
        :param fullname:
        :return: username
        """

        username = fullname.lower().replace(' ', '')
        username += get_uuid_str()[:5]
        return username

    @staticmethod
    def get_owner(identifier: str) -> Owner:
        """
        Fetches owner by fullname or username as passed in identifier
        :param identifier: username or fullname
        :return: Owner model object
        """

        owner_o = Owner.query.filter((Owner.fullname == identifier) | (Owner.username == identifier)).first()
        return owner_o

    @staticmethod
    def get_pets(username: str) -> List[Pet]:
        """
        Fetches pets of owner identifier by given username
        :param username: username of the owner
        :return: List of Owner Pets
        """

        owner_q = Owner.query.filter(Owner.username == username).first()
        return owner_q.pets

    @staticmethod
    def insert_owner(fullname: str) -> Owner:
        """
        Creates owner object and saves it in the database
        :param fullname: fullname of the owner
        :return: newly inserted owner model instance
        """

        username = OwnerController.__generate_username(fullname)
        owner_o = Owner(username=username, fullname=fullname)
        Database.insert(owner_o)
        return OwnerController.get_owner(username)


class PetController:
    """
    Controller to interact with the Pet model
    """

    @staticmethod
    def get_pet(serial_number: str) -> Pet:
        return Pet.query.filter_by(serial_number=serial_number).first()

    @staticmethod
    def insert_pet(pet_type: str, owner_name: str) -> Pet:
        """
        Creates Pet model object with given params and inserts it in the database
        :param pet_type: Type of per (cat or dog)
        :param owner_name: Name of the owner of the pet
        :return: newly inserted Pet model object
        """
        pet_o = Pet(serial_number=get_uuid_str(), owner_name=owner_name, type=pet_type)
        Database.insert(pet_o)
        return PetController.get_pet(pet_o.serial_number)

    @staticmethod
    def get_all() -> List[Pet]:
        """
        Returns list of all the pets in the database
        """
        return Pet.query.all()
