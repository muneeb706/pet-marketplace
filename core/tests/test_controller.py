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

        with self.app.app_context():
            Database.init_db()

    def tearDown(self):
        with self.app.app_context():
            Database.close_db()


class TestOwnerController(TestBase):

    def test_insert_owner(self):
        with self.app.app_context():
            owner_o = OwnerController.insert_owner("Muneeb Shahid")
            self.assertIsNotNone(owner_o)
            self.assertIsNotNone(owner_o.username)

    def test_get_pets(self):
        with self.app.app_context():
            # inserting pet with owner
            owner_o = OwnerController.insert_owner("Muneeb Shahid")
            pet_o = PetController.insert_pet(pet_type="dog", owner_name=owner_o.fullname)
            pets = OwnerController.get_pets(owner_o.username)
            self.assertEqual(1, len(pets))
            self.assertEqual(pet_o.serial_number, pets[0].serial_number)


class TestPetController(TestBase):

    def test_insert_pet(self):
        with self.app.app_context():
            owner_o = OwnerController.insert_owner("Muneeb Shahid")
            pet_o = PetController.insert_pet(pet_type="dog", owner_name=owner_o.fullname)
            self.assertIsNotNone(pet_o)
            self.assertEqual("dog", pet_o.type)

    def test_get_all(self):
        with self.app.app_context():
            owner_o = OwnerController.insert_owner("Muneeb Shahid")
            PetController.insert_pet(pet_type="dog", owner_name=owner_o.fullname)
            PetController.insert_pet(pet_type="dog", owner_name=owner_o.fullname)

            pets = PetController.get_all()
            self.assertEqual(2, len(pets))
