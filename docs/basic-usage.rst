Basic usage
===========

To get started, the first step is to import and load the extension::

    from flask import Flask
    from flask_bootstrap import Bootstrap

    def create_app():
      app = Flask(__name__)
      Bootstrap(app)

      return app

    # do something with app...

After loading, new templates are available to derive from in your templates.

Sample Application
------------------

If you want to have a look at a small sample application, try `browsing it on
github
<https://github.com/mbr/flask-bootstrap/tree/master/sample_application>`_.


Templates
---------
.. highlight:: jinja

Creating a new Bootstrap-based template is simple::

    {% extends "bootstrap/base.html" %}
    {% block title %}This is an example page{% endblock %}

    {% block navbar %}
    <div class="navbar navbar-fixed-top">
      <!-- ... -->
    </div>
    {% endblock %}

    {% block content %}
      <h1>Hello, Bootstrap</h1>
    {% endblock %}

Everything you do in child templates is based on blocks. Some blocks (like
``title``, ``navbar`` or ``content``) are "convenience blocks". Strictly
speaking they would not be necessary, but are added to save typing effort.

A very powerful feature is `Jinja2's super()
<http://jinja.pocoo.org/docs/templates/#super-blocks>`_ function. This gives
you the option of amending blocks instead of replacing them.

Available blocks
~~~~~~~~~~~~~~~~

============ =========== =======
Block name   Outer Block Purpose
============ =========== =======
doc                      Outermost block.
html         doc         Contains the complete content of the ``<html>`` tag.
html_attribs doc         Attributes for the HTML tag.
head         doc         Contains the complete content of the ``<head>`` tag.
body         doc         Contains the complete content of the ``<body>`` tag.
body_attribs body        Attributes for the Body Tag.
**title**    head        Contains the complete content of the ``<title>`` tag.
**styles**   head        Contains all CSS style ``<link>`` tags inside head.
metas        head        Contains all ``<meta>`` tags inside head.
**navbar**   body        An empty block directly above *content*.
**content**  body        Convenience block inside the body. Put stuff here.
**scripts**  body        Contains all ``<script>`` tags at the end of the body.
============ =========== =======

Examples
~~~~~~~~

* Adding a custom CSS file::

    {% block styles %}
    {{super()}}
    <link rel="stylesheet"
          href="{{url_for('.static', filename='mystyle.css')}}">
    {% endblock %}

* Custom Javascript loaded *before* Bootstrap's javascript code::

    {% block scripts %}
    <script src="{{url_for('.static', filename='myscripts.js')}}"></script>
    {{super()}}
    {% endblock %}

* Adding a ``lang="en"`` attribute to the ``<html>``-tag::

    {% block html_attribs} lang="en"{% endblock %}

Static resources
----------------

The url-endpoint ``bootstrap.static`` is available for refering to Bootstrap
resources, but usually, this isn't needed. A bit better is using the
``bootstrap_find_resource`` template filter, which will take CDN settings into
account.

The current resource-system is described in detail on :doc:`cdn`.


Macros
------

Flask-Bootstrap comes with macros to make your life easier. These need to be
imported like in this example::

  {% extends "bootstrap/base.html" %}
  {% import "bootstrap/wtf.html" as wtf %}

This would import the ``wtf.html`` macros with the name-prefix of ``wtf``
(these are discussed below at :ref:`forms`).


Fixes
~~~~~

Cross-browser fixes (specifically for Internet Explorer < 9) are usually
included, but not shipped with Flask-Bootstrap. You can download `html5shiv
<https://raw.github.com/aFarkas/html5shiv/master/dist/html5shiv.js>`_ and
`Respond.js <https://raw.github.com/scottjehl/Respond/master/respond.min.js>`_,
put them in your applications static folder and include them like in this
example::

  {% import "bootstrap/fixes.html" as fixes %}
  {% block head %}
    {{super()}}
    {{fixes.ie8()}}
  {% endblock %}

While the scripts are not included, links to them on CDNs are, so if you do not
use ``BOOTSTRAP_SERVE_LOCAL``, they will work out of the box. See :doc:`cdn`
for more details on how CDN-delivery works with Flask-Bootstrap.

Google Analytics
~~~~~~~~~~~~~~~~

`Google Analytics <http://www.google.com/analytics/>`_ support is also
available as an extension macro::

  {% import "bootstrap/google.html" as google %}

  {% block scripts %}
  {{super()}}
  {{google.analytics(account="YOUR ACCOUNT CODE")}}
  {% endblock %}

If you want the analytics account to be configurable from the outside, you can
use something like this instead::

  {{google.analytics(account=config['GOOGLE_ANALYTICS_ACCOUNT'])}}

This allows specifying the account as a Flask configuration value.

Since Flask-Bootstrap version ``3.1.1.2`` there is also support for never
"Universal Analytics" tracking code, e.g.::

  {{google.uanalytics(id=config['GOOGLE_ANALYTICS_ID'],
                      domain=config['GOOGLE_ANALYTICS_DOMAIN'])}}

.. _forms:

Forms
~~~~~

The ``bootstrap/wtf.html`` template contains macros to help you output forms
quickly. Flask-WTF_ is not a dependency of Flask-Bootstrap, however, and must be
installed explicitly. The API of Flask-WTF_ has changed quite a bit over the
last few versions, Flask-Bootstrap is currently developed for Flask-WTF_ version
0.9.2.

The most basic way is using them as an aid to create a form by hand::

  <form class="form form-horizontal" method="post" role="form">
    {{ form.hidden_tag() }}
    {{ wtf.form_errors(form, hiddens="only") }}

    {{ wtf.form_field(form.field1) }}
    {{ wtf.form_field(form.field2) }}
  </form>

However, often you just want to get a form done quickly and have no need for
intense fine-tuning::

  {{ wtf.quick_form(form) }}

Form macro reference
********************

.. py:function:: quick_form(form,\
                    action="",\
                    method="post",\
                    extra_classes=None,\
                    role="form",\
                    form_type="basic",\
                    horizontal_columns=('lg', 2, 10),\
                    enctype=None,\
                    button_map={})

   Outputs Bootstrap-markup for a complete Flask-WTF_ form.

   :param form: The form to output.
   :param method: ``<form>`` method attribute.
   :param extra_classes: The classes to add to the ``<form>``.
   :param role: ``<form>`` role attribute.
   :param form_type: One of ``basic``, ``inline`` or ``horizontal``. See the
                     Bootstrap_ docs for details on different form layouts.
   :param horizontal_columns: When using the horizontal layout, layout forms
                              like this. Must be a 3-tuple of ``(column-type,
                              left-column-size, right-colum-size)``.
   :param enctype: ``<form>`` enctype attribute.
   :param button_map: A dictionary, mapping button field names to names such as ``primary``, ``danger`` or ``success``. 
                      Buttons not found in the ``button_map`` will use the ``default`` type of button.


.. py:function:: form_errors(form, hiddens=True)

   Renders paragraphs containing form error messages. This is usually only used
   to output hidden field form errors, as others are attached to the form
   fields.

   :param form: Form, who's errors should be rendered.
   :param hiddens: If ``True``, render errors of hidden fields as well. If
                   ``'only'``, render *only* these.


.. py:function:: form_field(field,\
                            form_type="basic",\
                            horizontal_columns=('lg', 2, 10),\
                            button_map={})

    Renders a single form-field with surrounding elements. Used mainly by
    ``quick_form``.

.. _Flask-WTF: https://flask-wtf.readthedocs.org/en/latest/

