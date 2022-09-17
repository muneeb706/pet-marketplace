from unittest import TestCase
from core.controller import OwnerController
from core import create_app
from core.db import Database


class TestOwnerController(TestCase):

    def setUp(self):
        self.controller = OwnerController()
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        # This creates an in-memory sqlite db
        # See https://martin-thoma.com/sql-connection-strings/
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

        with self.app.app_context():
            Database.init_db()

    def tearDown(self):
        pass

    def test_insert_owner(self):
        with self.app.app_context():
            owner_o = self.controller.insert_owner("Muneeb Shahid")
            self.assertIsNotNone(owner_o)
            self.assertIsNotNone(owner_o.username)
