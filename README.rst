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

  {{ wtf.quick_form(form) }}

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
``BOOTSTRAP_CDN_BASEURL``              A dictionary set up with URLs to ``cdnjs.com``.          The URLs to which Bootstrap and other filenames are appended when using a CDN.
``BOOTSTRAP_CDN_PREFER_SSL``           ``True``                                                 If the ``BOOTSTRAP_CDN_BASEURL`` starts with ``//``, prepend ``'https:'`` to it.
``BOOTSTRAP_FONTAWESOME``              ``False``                                                If ``True``, `FontAwesome`_ will be enabled.
``BOOTSTRAP_CUSTOM_CSS``               ``False``                                                If ``True``, no Bootstrap CSS files will be loaded. Use this if you compile a custom css file that already includes bootstrap.
``BOOTSTRAP_QUERYSTRING_REVVING``      ``True``                                                If ``True``, will apppend a querystring with the current version to all static resources served locally. This ensures that upon upgrading Flask-Bootstrap, these resources are refreshed.
====================================== ======================================================== ===

.. _FontAwesome: http://fortawesome.github.com/Font-Awesome/

Installation
------------

Either install from github using ``pip`` or from `PyPI
<http://pypi.python.org/pypi/Flask-Bootstrap>`_.

A note on versioning
--------------------

Flask-Bootstrap tries to keep some track of Twitter's Bootstrap releases.
Versioning is usually in the form of ``Bootstrap version`` - ``Flask-Bootstrap
iteration``. For example, a version of ``2.0.3-2`` bundles Bootstrap version
``2.0.3`` and is the second release of Flask-Bootstrap containing that version.

If you need to rely on your templates not changing, simply pin the version in
your setup.py.

FAQ
---

1. Why do I have undesired auto-escapes in my template output?

   Make sure your templates end in ``.htm``, ``.html``, ``.xml`` or ``.xhtml``.
   Flask sets the Jinja2-autoescape mode depending on the template file
   extension (see `this StackOverflow question
   <http://stackoverflow.com/questions/13222925/how-do-i-enable-autoescaping-in-templates-with-a-jhtml-extension-in-flask>`_
   for more information).

   General convention in Flask applications is to name your HTML-templates
   ``.html`` though.

2. How can I add custom javascript to the template?

   Use Jinja2's ``super()`` in conjunction with the ``bootstrap_js_bottom``
   block. The super-function adds the contents of a block from the parent
   template, that way you can even decide if you want to include it before or
   after jQuery/bootstrap. Example::

     {% block bootstrap_js_bottom %}
       {{super()}}
       <script src="my_app_code.js">
     {% endblock %}

3. How do I serve the static files in deployment?

   Flask-Bootstrap is not special in the sense that it simply adds a blueprint
   named ``bootstrap``. The static files map to a specific URL-prefix (per
   default ``static/bootstrap`` and are served from a specific directory
   found in your virtualenv installation (e.g.
   ``lib/python2.7/site-packages/flask_bootstrap/static``), so a traditional
   setup would be setting up your webserver to serve this address from the
   mentioned directory.

   A more elegant approach is having a cache in front of the WSGI server that
   respects ``Cache-Control`` headers. Per default, Flask will serve static
   files with an expiration time of 12 hours (you can change this value using
   the ``SEND_FILE_MAX_AGE_DEFAULT``), which should be sufficient.

   For this approach `nginx <http://nginx.org>`_ (or, if you prefer,
   `Varnish <http://varnish-cache.org>`_) or their cloud-service based
   equivalents should suffice. Flask-Bootstrap 2.3.2.2 supports this by
   offering querystring revving (see ``BOOTSTRAP_QUERYSTRING_REVVING``) to
   ensure newer Bootstrap versions are served when you upgrade Flask-Bootstrap.

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
* `FontAwesome`_ now version 3.0 instead of 2.0.
* The ``navbar()``-macro is gone. It was accidentally committed and never did
  anything useful, so this hopefully won't concern anyone.

2.3.0-2
"""""""
* Switched the CDN to `cdnjs <http://cdnjs.com>`_ because `netdna
  <http://bootstrapcdn.com>`_ keeps changing files around too much.
* Introduced ``BOOTSTRAP_CUSTOM_CSS`` option.

2.3.2.1
"""""""
* Slight change in versioning (dot instead of hyphen for the Flask-Bootstrap
  release).

2.3.2.2
"""""""
* html5-shim is loaded using a protocol-relative URL
* Rendering of RadioField changed (see sample app).