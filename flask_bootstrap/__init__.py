#!/usr/bin/env python
# coding=utf8

from flask import Blueprint


class Bootstrap(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('BOOTSTRAP_USE_MINIFIED', True)
        app.config.setdefault('BOOTSTRAP_JQUERY_VERSION', '1.7.2')
        app.config.setdefault('BOOTSTRAP_HTML5_SHIM', True)

        self.app = app
        self.blueprint = Blueprint(
            'bootstrap',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=self.app.static_url_path + '/bootstrap')

        app.register_blueprint(self.blueprint)
