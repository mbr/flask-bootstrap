===============
Flask-Bootstrap
===============

Flask-Bootstrap packages `Twitter's Bootstrap
<http://twitter.github.com/bootstrap/>`_ into an extension that mostly consists
of a blueprint named 'bootstrap'. It can also create links to serve Bootstrap
from a CDN.

Usage
-----

Here is an example::

  from flask.ext.bootstrap import Bootstrap

  [...]

  Bootstrap(app)

This makes some new templates available, mainly ``bootstrap_base.html`` and
``bootstrap_responsive.html``. These are blank pages that include all bootstrap
resources, and have predefined blocks where you can put your content. The core
block to alter is ``body_content``, otherwise see the source of the template
for more possiblities.

The url-endpoint ``bootstrap.static`` is available for refering to Bootstrap
resources, but usually, this isn't needed. A bit better is using the
``bootstrap_find_resource`` template filter, which will CDN settings into
account.

Macros
------

A few macros are available to make your life easier. These need to be imported
(I recommend create your own "base.html" template that extends one of the
bootstrap base templates first and including the the macros there).

An example "base.html"::

  {% extends "bootstrap_responsive.html" %}
  {% import "bootstrap_wtf.html" as wtf %}

Forms
~~~~~

The ``bootstrap_wtf`` template contains macros to help you output forms
quickly. The most basic way is using them as an aid to create a form by hand::

  <form class="form form-horizontal" method="post">
    {{ form.hidden_tag() }}
    {{ wtf.form_errors(form, "only") }}

    {{ wtf.horizontal_field(form.field1) }}
    {{ wtf.horizontal_field(form.field2) }}

    <div class="form-actions">
       <button name="action_save" type="submit" class="btn btn-primary">Save changes</button>
    </div>
  </form>

However, often you just want to get a form done quickly and have no need for
intense fine-tuning:

::

  {{ quick_form(form) }}

Configuration options
---------------------

There are a few configuration options used by the templates:

====================================== ======================================================== ===
Option                                 Default
====================================== ======================================================== ===
``BOOTSTRAP_USE_MINIFIED``             ``True``                                                 Whether or not to use the minified versions of the css/js files.
``BOOTSTRAP_JQUERY_VERSION``           ``'1'``                                                  This version of jQuery is included in the template via Google CDN. Also honors ``BOOTSTRAP_USE_MINIFIED``. Set this to ``None`` to not include jQuery at all. Note that non-minified Bootstrap resources are sometimes missing on bootstrapcdn, so it is best not to use it without turning on ``BOOTSTRAP_USE_MINIFIED``.
``BOOTSTRAP_HTML5_SHIM``               ``True``                                                 Include the default IE-fixes that are usually included when using bootstrap.
``BOOTSTRAP_GOOGLE_ANALYTICS_ACCOUNT`` ``None``                                                 If set, include `Google Analytics <http://www.google.com/analytics>`_ boilerplate using this account.
``BOOTSTRAP_USE_CDN``                  ``False``                                                If ``True``, Bootstrap resources will no be served from the local app instance, but will use a Content Delivery Network instead (configured by ``BOOTSTRAP_CDN_BASEURL``).
``BOOTSTRAP_CDN_BASEURL``              A dictionary set up with URLs to ``bootstrapcdn.com``    The URLs to which Bootstrap and other filenames are appended when using a CDN.
``BOOTSTRAP_CDN_PREFER_SSL``           ``True``                                                 If the ``BOOTSTRAP_CDN_BASEURL`` starts with ``//``, prepend ``'https:'`` to it.
``BOOTSTRAP_FONTAWESOME``              ``False``                                                If ``True``, `FontAwesome`_ will be enabled.
====================================== ======================================================== ===

.. _FontAwesome: http://fortawesome.github.com/Font-Awesome/

Installation
------------

Either install from github using ``pip`` or from `PyPI
<http://pypi.python.org>`_. The package is known on PyPI as
``flask-bootstrap``.

A note on versioning
--------------------

Flask-Bootstrap tries to keep some track of Twitter's Bootstrap releases.
Versioning is usually in the form of ``Bootstrap version`` - ``Flask-Bootstrap
iteration``. For example, a version of ``2.0.3-2`` bundles Bootstrap version
``2.0.3`` and is the second release of Flask-Bootstrap containing that version.

If you need to rely on your templates not changing, simply pin the version in
your setup.py.

CHANGES
~~~~~~~

The following changes could have possibly been not backwards compatible:

2.1.0-1
"""""""
* New upstream release: 2.1.0.
* Changed the default version of jQuery from 1.7.2 to just 1. This means that
  the latest 1.x.x version of jQuery will be pulled.

2.1.1-1
"""""""
* WTForms generated HTML code is now considered safe. This allows Flask-WTF's
  ``RecaptchaField`` to work with ``quick_form``.

2.1.1-2
"""""""
* There is no longer a self.app on Flask-Bootstrap. The extension can be shared
  by any number of applications using ``init_app()`` (though the old
  ``__init__()`` signature is kept for backward compatibiliy).

2.2.1-1
"""""""
* `FontAwesome`_ is now supported
  as well, can also be loaded from bootstrapCDN. Set ``BOOTSTRAP_FONTAWESOME``
  to ``True`` to enable it.
* ``BOOTSTRAP_CDN_BASEURL`` is now a dictionary for multiple CDNs (i.e.
  Bootstrap, FontAwesome can use different base URLs). This will break any code
  that relied on setting ``BOOTSTRAP_CDN_BASEURL``.

2.2.2-1
"""""""
* FontAwesome now version 3.0 instead of 2.0.
