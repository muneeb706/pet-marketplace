import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # instance_relative_config=True tells the app that
    # configuration files are relative to the instance folder.
    # The instance folder is located outside the core package
    # and can hold local data that shouldn’t be committed to
    # version control, such as configuration secrets and the database file.
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs("tmp")
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import views
    app.register_blueprint(views.bp)

    return app
