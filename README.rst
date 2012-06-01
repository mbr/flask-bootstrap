===============
Flask-Bootstrap
===============

Flask-Bootstrap packages `Twitter's Bootstrap
<http://twitter.github.com/bootstrap/>`_ into an extension that mostly consists
of a blueprint named 'bootstrap'.

Usage
-----

Here is an example::

  from flask.ext.bootstrap import Bootstrap

  [...]

  Bootstrap(app)

This makes some new templates available, mainly ``bootstrap_base.html`` and
``bootstrap_responsive.html``. These are blank pages that include all bootstrap
resources, and have predefined blocks where you can put your content. The core
block to alter is ``body_content``, otherwise see the source of the template for
more possiblities.

The url-endpoint ``bootstrap.static`` is available for refering to Bootstrap
resources, but usually, this isn't needed.

Configuration options
---------------------
There are a few configuration options used by the templates:

:BOOTSTRAP_USE_MINIFIED: (default: ``True``) - whether or not to use the minified versions of the css/js files
:BOOTSTRAP_JQUERY_VERSION: (default: ``'1.7.2'``) - this version of jQuery is included in the template via Google CDN. Also honors ``BOOTSTRAP_USE_MINIFIED``. Set this to ``None`` to not include jQuery at all.
:BOOTSTRAP_HTML5_SHIM: (default: ``True``) Include the default IE-fixes that are usually included when using bootstrap.
:BOOTSTRAP_GOOGLE_ANALYTICS_ACCOUNT: (default: ``None``). If set, include ``Google Analytics <http://www.google.com/analytics``_ boilerplate using this account.
