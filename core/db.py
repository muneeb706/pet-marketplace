from flask_sqlalchemy import SQLAlchemy


class Database:

    __instance = None

    @staticmethod
    def get_instance():
        """Static Access Method"""
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
        cls.get_instance().create_all()

    @classmethod
    def insert(cls, model_instance):
        cls.get_instance().session.add(model_instance)
        cls.get_instance().session.commit()

    @classmethod
    def insert_all(cls, model_instances):
        cls.get_instance().session.add_all(model_instances)
        cls.get_instance().session.commit()

    @classmethod
    def close_db(cls, e=None):
        cls.get_instance().session.close()



