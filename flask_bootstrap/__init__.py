#!/usr/bin/env python
# coding=utf8

from flask import Blueprint

try:
    from wtforms.fields import HiddenField
except ImportError:
    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:
    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)


class Bootstrap(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('BOOTSTRAP_USE_MINIFIED', True)
        app.config.setdefault('BOOTSTRAP_JQUERY_VERSION', '1.7.2')
        app.config.setdefault('BOOTSTRAP_HTML5_SHIM', True)
        app.config.setdefault('BOOTSTRAP_GOOGLE_ANALYTICS_ACCOUNT', None)

        self.app = app
        self.blueprint = Blueprint(
            'bootstrap',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=self.app.static_url_path + '/bootstrap')

        app.register_blueprint(self.blueprint)

        app.jinja_env.filters['bootstrap_is_hidden_field'] =\
            is_hidden_field_filter
