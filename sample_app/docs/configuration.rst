Configuration
=============

There are a few configuration options used by Flask-Bootstrap, these are
regular Flask Configuration variables (there's a manual on these `here <http://flask.pocoo.org/docs/config/>`_).

.. note:: There's a Flask extension available to aid the creation of
          `Twelve-Factor <http://12factor.net/>`_-patterned apps in the form of
          `Flask-Appconfig <https://github.com/mbr/flask-appconfig>`_. It also
          handles other kinds of configuration setups and goes along well with
          Flask-Bootstrap.

====================================== ======================================================== ===
Option                                 Default
====================================== ======================================================== ===
``BOOTSTRAP_USE_MINIFIED``             ``True``                                                 Whether or not to use the minified versions of the css/js files.
``BOOTSTRAP_SERVE_LOCAL``              ``False``                                                If ``True``, Bootstrap resources will be served from the local app instance every time. See :doc:`cdn` for details.
``BOOTSTRAP_LOCAL_SUBDOMAIN``          ``None``                                                 Passes a ``subdomain`` parameter to the generated :class:`~flask.Blueprint`. Useful when serving assets locally from a different subdomain.
``BOOTSTRAP_CDN_FORCE_SSL``            ``True``                                                 If a CDN resource url starts with ``//``, prepend ``'https:'`` to it.
``BOOTSTRAP_QUERYSTRING_REVVING``      ``True``                                                 If ``True``, will append a querystring with the current version to all static resources served locally. This ensures that upon upgrading Flask-Bootstrap, these resources are refreshed.
====================================== ======================================================== ===
