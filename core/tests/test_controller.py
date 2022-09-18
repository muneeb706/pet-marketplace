from unittest import TestCase

from core import create_app
from core.controller import OwnerController, PetController
from core.db import Database


class TestBase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        # This creates an in-memory sqlite db
        # See https://martin-thoma.com/sql-connection-strings/
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

        # adding flask application context
        # so, that we don't have to open context
        # every time we interact with the application
        self._ctx = self.app.app_context()
        self._ctx.push()
        Database.init_db()

    def tearDown(self):
        Database.close_db()
        if getattr(self, '_ctx') and self._ctx is not None:
            self._ctx.pop()
        del self._ctx


class TestOwnerController(TestBase):

    def test_insert_owner(self):
        owner_o = OwnerController.insert_owner("Muneeb Shahid")
        self.assertIsNotNone(owner_o)
        self.assertIsNotNone(owner_o.username)

    def test_get_pets(self):
        # inserting pet with owner
        owner_o = OwnerController.insert_owner("Muneeb Shahid")
        pet_o = PetController.insert_pet(pet_type="dog", owner_name=owner_o.fullname)
        pets = OwnerController.get_pets(owner_o.username)
        self.assertEqual(1, len(pets))
        self.assertEqual(pet_o.serial_number, pets[0].serial_number)


class TestPetController(TestBase):

    def test_insert_pet(self):
        owner_o = OwnerController.insert_owner("Muneeb Shahid")
        pet_o = PetController.insert_pet(pet_type="dog", owner_name=owner_o.fullname)
        self.assertIsNotNone(pet_o)
        self.assertEqual("dog", pet_o.type)

    def test_get_all(self):
        owner_o = OwnerController.insert_owner("Muneeb Shahid")
        PetController.insert_pet(pet_type="dog", owner_name=owner_o.fullname)
        PetController.insert_pet(pet_type="dog", owner_name=owner_o.fullname)

        pets = PetController.get_all()
        self.assertEqual(2, len(pets))
