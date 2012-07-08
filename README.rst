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

Macros
------

A few macros are available to make your life easier. These need to be imported
(I recommend create your own "base.html" template that extends one of the
bootstrap base templates first and including the the macros there).

An example "base.html"::

  {% extends "bootstrap_response.html" %}
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

:BOOTSTRAP_USE_MINIFIED: (default: ``True``) - whether or not to use the minified versions of the css/js files
:BOOTSTRAP_JQUERY_VERSION: (default: ``'1.7.2'``) - this version of jQuery is included in the template via Google CDN. Also honors ``BOOTSTRAP_USE_MINIFIED``. Set this to ``None`` to not include jQuery at all.
:BOOTSTRAP_HTML5_SHIM: (default: ``True``) Include the default IE-fixes that are usually included when using bootstrap.
:BOOTSTRAP_GOOGLE_ANALYTICS_ACCOUNT: (default: ``None``). If set, include `Google Analytics <http://www.google.com/analytics>`_ boilerplate using this account.

Installation
------------

Either install from github using ``pip`` or from `PyPI
<http://pypi.python.org>`_. Note that the package is known on PyPI as
``flask-bootstrap2``.

A note on versioning
--------------------

Flask-Bootstrap tries to keep sometrack track of Twitter's Bootstrap releases.
Versioning is usually in the form of ``Bootstrap version`` - ``Flask-Bootstrap
iteration``. For example, a version of ``2.0.3-2`` bundles Bootstrap version
``2.0.3`` and is the second release of Flask-Bootstrap containing that version.

If you need to rely on your templates not changing, simply pin the version in
your setup.py.
