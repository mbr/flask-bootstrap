#!/usr/bin/env python
# coding=utf8

from flask import Blueprint, current_app, url_for

try:
    from wtforms.fields import HiddenField
except ImportError:
    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:
    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)


def bootstrap_find_resource(filename,
                            use_minified=None,
                            cdn='bootstrap'):
    # FIXME: get rid of this function and instead manipulate the flask routing
    #        system
    config = current_app.config

    if None == use_minified:
        use_minified = config['BOOTSTRAP_USE_MINIFIED']

    if use_minified:
        filename = '%s.min.%s' % tuple(filename.rsplit('.', 1))

    if not config['BOOTSTRAP_USE_CDN']:
        return url_for('bootstrap.static', filename=filename)
    else:
        baseurl = config['BOOTSTRAP_CDN_BASEURL'][cdn]

        if baseurl.startswith('//') and config['BOOTSTRAP_CDN_PREFER_SSL']:
            baseurl = 'https:%s' % baseurl
        return baseurl + filename


class Bootstrap(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('BOOTSTRAP_USE_MINIFIED', True)
        app.config.setdefault('BOOTSTRAP_JQUERY_VERSION', '1')
        app.config.setdefault('BOOTSTRAP_HTML5_SHIM', True)
        app.config.setdefault('BOOTSTRAP_GOOGLE_ANALYTICS_ACCOUNT', None)
        app.config.setdefault('BOOTSTRAP_USE_CDN', False)
        app.config.setdefault('BOOTSTRAP_CDN_PREFER_SSL', True)
        app.config.setdefault('BOOTSTRAP_FONTAWESOME', False)
        app.config.setdefault(
            'BOOTSTRAP_CDN_BASEURL', {
                'bootstrap':   '//netdna.bootstrapcdn.com/'\
                               'twitter-bootstrap/2.2.2/',
                'fontawesome': '//netdna.bootstrapcdn.com/'\
                               'font-awesome/3.0/',
            }
        )

        blueprint = Blueprint(
            'bootstrap',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/bootstrap')

        app.register_blueprint(blueprint)

        app.jinja_env.filters['bootstrap_is_hidden_field'] =\
            is_hidden_field_filter
        app.jinja_env.filters['bootstrap_find_resource'] =\
            bootstrap_find_resource
