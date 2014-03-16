========================
Common use cases and FAQ
========================


Why do I have undesired auto-escapes in my template output?
-----------------------------------------------------------

Make sure your templates end in ``.htm``, ``.html``, ``.xml`` or ``.xhtml``.
Flask sets the Jinja2-autoescape mode depending on the template file extension
(see `this StackOverflow question <http://stackoverflow.com/questions/13222925
/how-do-i-enable-autoescaping-in-templates-with-a-jhtml-extension-in-flask>`_
for more information).

General convention in Flask applications is to name your HTML-templates
``.html`` though.


How can I add custom javascript to the template?
------------------------------------------------
.. highlight:: jinja

Use Jinja2's super_ in conjunction with the ``scripts`` block.
The super-function adds the contents of a block from the parent template, that
way you can even decide if you want to include it before or after
jQuery/bootstrap.
Example::


  {% block scripts %}
    {{super()}}
    <script src="my_app_code.js">
  {% endblock %}


How do I serve the static files in deployment?
----------------------------------------------

Flask-Bootstrap is not special in the sense that it simply adds a blueprint
named ``bootstrap``. The static files map to a specific URL-prefix (per default
``static/bootstrap`` and are served from a specific directory found in your
virtualenv installation (e.g. ``lib/python2.7/site-
packages/flask_bootstrap/static``), so a traditional setup would be setting up
your webserver to serve this address from the mentioned directory.

A more elegant approach is having a cache in front of the WSGI server that
respects ``Cache-Control`` headers. Per default, Flask will serve static files
with an expiration time of 12 hours (you can change this value using the
``SEND_FILE_MAX_AGE_DEFAULT``), which should be sufficient.

For this approach `nginx <http://nginx.org>`_ (or, if you prefer, `Varnish <http
://varnish-cache.org>`_) or their cloud-service based equivalents should
suffice. Flask-Bootstrap 2.3.2.2 supports this by offering querystring revving
(see ``BOOTSTRAP_QUERYSTRING_REVVING``) to ensure newer Bootstrap versions are
served when you upgrade Flask-Bootstrap.


How do I use Bootstrap 2/3?
---------------------------
.. highlight:: python

The current major stable version of Bootstrap is 3, which unfortunately is
backwards incompatible with Bootstrap 2. Flask-Bootstrap is maintained for
the latest version of Bootstrap 2 (although you should not expect new
features, only bug fixes) and, of course, Bootstrap 3.

By installing Flask-Bootstrap, you will always get the latest version, which
is Bootstrap 3. To install (or keep) Flask-Bootstrap 2, you will have to
specify the version in your ``setup.py`` or ``requirements.txt`` like this::

  # other stuff in setup.py
  # ...
  install_requires=['flask-bootstrap<3', 'another_package']
  # ...

It's not a bad idea to pin to a specific Flask-Bootstrap (e.g.    ``'flask-
bootstrap==2.3.2.2'`` to avoid surprises in production).

See the :doc:`bootstrap2` documentation for details.


Where is FontAwesome?
---------------------
.. highlight:: jinja

Versions of Flask-Bootstrap using Bootstrap 2 included FontAwesome_, this is no longer the case for Flask-Bootstrap 3 and higher.

Originally, Bootstrap did come only with image-based icons that did not scale
well, FontAwesome fixed this by providing vector-based replacements, as well as
additional icons. However, starting with Bootstrap 3 icons were included as a
font again, for this reason FontAwesome was dropped from the extension to
simplify things.

Today, FontAwesome_ is not the only choice, a comparison of available
alternatives is `available on the web
<http://tagliala.github.io/vectoriconsroundup/>`_.

If you still want to use FontAwesome, it's easy to include it by adding it to
the styles block inside your template derived base template::

  {% block styles -%}
  {{super()}}
  <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
  {% endblock styles %}

..  _FontAwesome: http://fontawesome.io
.. _super: http://jinja.pocoo.org/docs/templates/#super-blocks
