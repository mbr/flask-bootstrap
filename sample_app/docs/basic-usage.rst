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
<https://github.com/mbr/flask-bootstrap/tree/master/sample_app>`_.


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

.. _block-names:

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

    {% block html_attribs %} lang="en"{% endblock %}

Static resources
----------------

The url-endpoint ``bootstrap.static`` is available for refering to Bootstrap
resources, but usually, this isn't needed. A bit better is using the
``bootstrap_find_resource`` template filter, which will take CDN settings into
account.

The current resource-system is described in detail on :doc:`cdn`.
