import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


class Config:
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = "2c084ae6f1b340a7af8880400b83cb49"
    FLASK_SECRET = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{ROOT_DIR}/tmp/pet-marketplace.db"

