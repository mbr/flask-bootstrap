Using Bootstrap 2
=================

The current major stable version of Bootstrap is 3, which is backwards
incompatible with Bootstrap 2. Besides version 3, Flask-Bootstrap is maintained
for the latest version of Bootstrap 2 (although you should not expect new
features, only bug fixes).

Installation
------------

By installing Flask-Bootstrap, you will always get the latest version, which is
Bootstrap 3. To install (or keep) Flask-Bootstrap 2, you will have to specify
the version in your ``setup.py`` or ``requirements.txt`` similiar to this::

    # other stuff in setup.py...
    install_requires=['flask-bootstrap<3', 'another_package']

It's not a bad idea to pin to a specific Flask-Bootstrap version (e.g.
``'flask-bootstrap==2.3.2.2'`` to avoid surprises in production).

Documentation
-------------

Before version 3, Flask-Bootstrap only had a README file as documentation. You
can find the full file below.

You can also find previous version tags on `github <https://github.com>`_. To
have a look at the code or sample app for major version 2, take a look at
`2.3.2.2 <https://github.com/mbr/flask-bootstrap/tree/2.3.2.2>`_.

Flask-Bootstrap
^^^^^^^^^^^^^^^

Flask-Bootstrap packages `Bootstrap
<http://getbootstrap.com>`_ into an extension that mostly consists
of a blueprint named 'bootstrap'. It can also create links to serve Bootstrap
from a CDN.

Usage
*****

Here is an example::

  from flask_bootstrap import Bootstrap

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
******

.. highlight:: jinja

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
*********************

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
``BOOTSTRAP_CUSTOM_CSS``               ``False``                                                If ``True``, no Bootstrap CSS files will be loaded. Use this if you compile a custom css file that already includes bootstrap.
``BOOTSTRAP_QUERYSTRING_REVVING``      ``True``                                                 If ``True``, will apppend a querystring with the current version to all static resources served locally. This ensures that upon upgrading Flask-Bootstrap, these resources are refreshed.
====================================== ======================================================== ===

.. _FontAwesome: http://fortawesome.github.com/Font-Awesome/

Installation
************

Either install from github using ``pip`` or from `PyPI
<http://pypi.python.org/pypi/Flask-Bootstrap>`_.

A note on versioning
********************

Flask-Bootstrap tries to keep some track of Bootstrap's releases.
Versioning is usually in the form of ``Bootstrap version`` - ``Flask-Bootstrap
iteration``. For example, a version of ``2.0.3-2`` bundles Bootstrap version
``2.0.3`` and is the second release of Flask-Bootstrap containing that version.

If you need to rely on your templates not changing, simply pin the version in
your setup.py.

FAQ
***

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
   default ``static/bootstrap``) and are served from a specific directory
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

See :doc:`changelog` for changes including version 2.
