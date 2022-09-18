"""
Configuration file, contains configuration variables, that
can be imported anywhere in the application.
It also, contains AppConfig class for flask app configuration
"""

import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
TMP_DIR = f"{ROOT_DIR}/tmp"
DB_FILE = f"{TMP_DIR}/pet-marketplace.db"
ADMIN_NAME = "administrator"


class AppConfig:
    DEBUG = True
    # Flask-SQLAlchemy has its own event notification system
    # that gets layered on top of SQLAlchemy. This takes extra resources.
    # It is better to disable it.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE}"
