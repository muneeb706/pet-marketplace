from typing import Optional

from flask import Flask
from core import config
import click
from .db import Database
import os

db = Database.get_instance()


@click.command('init-db')
def init_db_command():
    try:
        os.makedirs(f"{config.TMP_DIR}")
    except OSError:
        pass
    """Clear the existing data and create new tables."""
    open(f"{config.DB_FILE}", "w")
    Database.init_db()
    click.echo('Initialized the database.')


def create_app(cfg: Optional[config.AppConfig] = None):
    if cfg is None:
        cfg = config.AppConfig()

    # create and configure the app
    # instance_relative_config=True tells the app that
    # configuration files are relative to the instance folder.
    # The instance folder is located outside the core package
    # and can hold local data that shouldn’t be committed to
    # version control, such as configuration secrets and the database file.
    # ensure the instance folder exists

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(cfg)

    db.init_app(app)

    from . import views
    app.register_blueprint(views.bp)

    app.teardown_appcontext(Database.close_db)
    app.cli.add_command(init_db_command)

    return app
