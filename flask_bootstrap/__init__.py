#!/usr/bin/env python
# coding=utf8

__version__ = '3.0.0.1'

import re

from flask import Blueprint, current_app, url_for

try:
    from wtforms.fields import HiddenField
except ImportError:
    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:
    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)


class CDN(object):
    """Base class for CDN objects."""
    def get_resource_url(self, filename):
        """Return resource url for filename."""
        raise NotImplementedError


class StaticCDN(object):
    """A CDN that serves content from the local application.

    :param static_endpoint: Endpoint to use.
    :param rev: If ``True``, honor ``BOOTSTRAP_QUERYSTRING_REVVING``.
    """
    def __init__(self, static_endpoint='static', rev=False):
        self.static_endpoint = static_endpoint
        self.rev = rev

    def get_resource_url(self, filename):
        extra_args = {}

        if self.rev and current_app.config['BOOTSTRAP_QUERYSTRING_REVVING']:
            extra_args['bootstrap'] = __version__

        return url_for(self.static_endpoint, filename=filename, **extra_args)


class WebCDN(object):
    """Serves files from the Web.

    :param baseurl: The baseurl. Filenames are simply appended to this URL.
    """
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def get_resource_url(self, filename):
        return self.baseurl + filename


def bootstrap_find_resource(filename, cdn, use_minified=None, local=True):
    """Resource finding function, also available in templates.

    Tries to find a resource, will force SSL depending on
    ``BOOTSTRAP_CDN_FORCE_SSL`` settings.

    :param filename: File to find a URL for.
    :param cdn: Name of the CDN to use.
    :param use_minified': If set to ``True``/``False``, use/don't use
                          minified. If ``None``, honors
                          ``BOOTSTRAP_USE_MINIFIED``.
    :param local: If ``True``, uses the ``local``-CDN when
                  ``BOOTSTRAP_SERVE_LOCAL`` is enabled. If ``False``, uses
                  the ``static``-CDN instead.
    :return: A URL.
    """
    config = current_app.config

    if None == use_minified:
        use_minified = config['BOOTSTRAP_USE_MINIFIED']

    if use_minified:
        filename = '%s.min.%s' % tuple(filename.rsplit('.', 1))

    if config['BOOTSTRAP_SERVE_LOCAL']:
        cdn = 'local' if local else 'static'

    cdns = current_app.extensions['bootstrap']['cdns']
    resource_url = cdns[cdn].get_resource_url(filename)

    if resource_url.startswith('//') and config['BOOTSTRAP_CDN_FORCE_SSL']:
        resource_url = 'https:%s' % resource_url

    return resource_url


class Bootstrap(object):
    def __init__(self, app=None):
        BOOTSTRAP_VERSION = re.sub(r'^(\d+\.\d+\.\d+).*', r'\1', __version__)
        JQUERY_VERSION = '2.0.3'
        HTML5SHIV_VERSION = '3.6.2'
        RESPONDJS_VERSION = '1.3.0'

        if app is not None:
            self.init_app(app)
            if not hasattr(app, 'extensions'):
                app.extensions = {}

            app.extensions['bootstrap'] = {
                'cdns': {
                    'local': StaticCDN('bootstrap.static', rev=True),
                    'static': StaticCDN(),
                    'bootstrap': WebCDN('//cdnjs.cloudflare.com/ajax/libs'
                                        '/twitter-bootstrap/%s/'
                                        % BOOTSTRAP_VERSION),
                    'jquery': WebCDN('//cdnjs.cloudflare.com/ajax/libs/jquery'
                                     '/%s/' % JQUERY_VERSION),
                    'html5shiv': WebCDN('//cdnjs.cloudflare.com/ajax/libs/'
                                        'html5shiv/%s/' % HTML5SHIV_VERSION),
                    'respond.js': WebCDN('//cdnjs.cloudflare.com/ajax/libs/'
                                         'respond.js/%s/' % RESPONDJS_VERSION),
                },
            }

    def init_app(self, app):
        app.config.setdefault('BOOTSTRAP_USE_MINIFIED', True)
        app.config.setdefault('BOOTSTRAP_CDN_FORCE_SSL', False)

        app.config.setdefault('BOOTSTRAP_QUERYSTRING_REVVING', True)
        app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', False)

        blueprint = Blueprint(
            'bootstrap',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/bootstrap')

        app.register_blueprint(blueprint)

        app.jinja_env.globals['bootstrap_is_hidden_field'] =\
            is_hidden_field_filter
        app.jinja_env.globals['bootstrap_find_resource'] =\
            bootstrap_find_resource
