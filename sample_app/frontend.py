# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Label, Separator

frontend = Blueprint('frontend', __name__)

# we're adding a navbar as well through flask-navbar
nav = Nav()

nav.register_element('top', Navbar(
    View('Flask-Bootstrap', '.index'),
    Subgroup(
        'Docs',
        Link('Flask-Bootstrap',
             href='http://pythonhosted.org/Flask-Bootstrap'),
        Link('Flask-AppConfig',
             href='https://github.com/mbr/flask-appconfig'),
        Link('Flask-Debug',
             href='https://github.com/mbr/flask-debug'),
        Separator(),
        Label('Bootstrap'),
        Link('Getting started',
             href='http://getbootstrap.com/getting-started/'),
        Link('CSS',
             href='http://getbootstrap.com/css/'),
        Link('Components',
             href='http://getbootstrap.com/components/'),
        Link('Javascript',
             href='http://getbootstrap.com/javascript/'),
        Link('Customize',
             href='http://getbootstrap.com/customize/'),
    )
))


# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    return render_template('index.html')
