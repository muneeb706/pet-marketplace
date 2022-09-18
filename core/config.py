import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
TMP_DIR = f"{ROOT_DIR}/tmp"
DB_FILE = f"{TMP_DIR}/pet-marketplace.db"
ADMIN_NAME = "administrator"


class AppConfig:
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = "2c084ae6f1b340a7af8880400b83cb49"
    FLASK_SECRET = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE}"
