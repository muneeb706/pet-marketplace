"""
Contains singleton class for Database instance.
"""

from flask_sqlalchemy import SQLAlchemy


class Database:
    """
    Singleton class to interact with the database
    """

    __instance = None

    @staticmethod
    def get_instance() -> SQLAlchemy:
        """
        Returns SQLAlchemy database instance.
        Creates if not already initialized
        """
        if not Database.__instance:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance:
            raise Exception("Only one instance of Database is allowed")
        else:
            Database.__instance = SQLAlchemy()

    @classmethod
    def init_db(cls):
        """
        Initializes database by creating all the tables
        defined in the models
        """
        cls.get_instance().create_all()

    @classmethod
    def insert(cls, model_instance):
        """
        Inserts record in the database table as
        represented by model instance
        :param model_instance: Instance of any model that needs to be inserted
        """

        cls.get_instance().session.add(model_instance)
        cls.get_instance().session.commit()

    @classmethod
    def insert_all(cls, model_instances):
        """
        Inserts multiple records in the database as
        represented by list of model instances
        :param model_instances: List of model instances
        """

        cls.get_instance().session.add_all(model_instances)
        cls.get_instance().session.commit()

    @classmethod
    def close_db(cls, e=None):
        """
        Terminates database connection
        """
        cls.get_instance().session.close()
