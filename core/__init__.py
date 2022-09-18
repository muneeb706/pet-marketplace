"""
It contains flask application factory and commands to initialize database
"""

import os
from typing import Optional

import click
from flask import Flask

from core import config
from .db import Database

# Singleton SQLAlchemy db instance
db = Database.get_instance()


@click.command('init-db')
def init_db_command():
    """
    This method runs against the init-db command.
    It initializes the database.
    """

    # create tmp directory if it does not exist
    try:
        os.makedirs(f"{config.TMP_DIR}")
    except OSError:
        pass

    # create db file if not exists
    open(f"{config.DB_FILE}", "w")

    Database.init_db()

    click.echo('Database setup complete.')


def create_app(cfg: Optional[config.AppConfig] = None) -> Flask:
    """
    Creates and returns flask application after configuring it
    :param cfg: config object
    :return: flask application
    """

    if cfg is None:
        cfg = config.AppConfig()

    app = Flask(__name__, instance_relative_config=True)
    # update the config values from given object
    app.config.from_object(cfg)

    # Linking SQLAlchemy db object with flask application
    db.init_app(app)

    # registering views module with the application
    from . import views
    app.register_blueprint(views.bp)

    # function to be called when application context ends
    app.teardown_appcontext(Database.close_db)
    # adding cli commands to application
    app.cli.add_command(init_db_command)

    return app
