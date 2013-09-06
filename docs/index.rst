===============
Flask-Bootstrap
===============

Flask-Bootstrap packages `Bootstrap <http://getbootstrap.com>`_ into an
extension that mostly consists of a blueprint named 'bootstrap'. It can also
create links to serve Bootstrap from a CDN.

.. toctree::
   basic-usage
   configuration
   changelog
   bootstrap2
   :maxdepth: 2


Installation
------------

Either install from github using ``pip`` or from `PyPI
<http://pypi.python.org/pypi/Flask-Bootstrap>`_.


Getting started
---------------

To get started, go ahead by reading :doc:`basic-usage`. A list of Frequently
Asked Questions for advanced users or those of older versions can be found
below.


A note on versioning
--------------------

Flask-Bootstrap tries to keep some track of Bootstrap releases. Versioning is
usually in the form of ``Bootstrap version``.``Flask-Bootstrap iteration``.
For example, a version of ``2.0.3.2`` bundles Bootstrap version ``2.0.3`` and is
the second release of Flask-Bootstrap containing that version.

If you need to rely on your templates not changing, simply pin the version in
your setup.py.


Bootstrap 2 vs Bootstrap 3
--------------------------

The latest major version of Bootstrap as of this writing is Bootstrap 3. A
branch of Flask-Bootstrap supporting version 2 is still supported, see the page
on :doc:`bootstrap2` for details.


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

4. How do I use Bootstrap 2/3?

   The current major stable version of Bootstrap is 3, which unfortunately is
   backwards incompatible with Bootstrap 2. Flask-Bootstrap is maintained for
   the latest version of Bootstrap 2 (although you should not expect new
   features, only bug fixes) and, of course, Bootstrap 3.

   By installing Flask-Bootstrap, you will always get the latest version, which
   is Bootstrap 3. To install (or keep) Flask-Bootstrap 2, you will have to
   specify the version in your ``setup.py`` or ``requirements.txt`` like this:

      # other stuff in setup.py
      # ...
      install_requires=['flask-bootstrap<3', 'another_package']
      # ...

   It's not a bad idea to pin to a specific Flask-Bootstrap (e.g.
   ``'flask-bootstrap==2.3.2.2'`` to avoid surprises in production).
