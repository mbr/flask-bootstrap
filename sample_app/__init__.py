# Welcome to the Flask-Bootstrap sample application. This will give you a
# guided tour around creating an application using Flask-Bootstrap.
#
# To run this application yourself, please install its requirements first:
#
#   $ pip install -r sample_app/requirements.txt
#
# This will, among other things, install Flask-Appconfig, which contains a
# program to run the application.
#
#   $ flaskdev sample_app
#
# Afterwards, point your browser to http://localhost:5000, then check out the
# source.

from flask import Flask
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap


def create_app(configfile=None):
    # We are using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__)

    # we use Flask-Appconfig here, but this is not a requirement
    AppConfig(app)

    # install our Bootstrap extension
    Bootstrap(app)

    return app
