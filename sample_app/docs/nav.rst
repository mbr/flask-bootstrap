Flask-Nav support
=================

The Flask-Nav_ extension allows easily creating navigational structures and
Flask-Bootstrap ships with a Bootstrap-compatible renderer for these. Upon
initializing an application, Flask-Bootstrap will register the Bootstrap
renderer as the default.

Rendering a navbar "just works", for example

.. code-block:: jinja

    {% block navbar %}
    {{nav.mynavbar.render()}}
    {% endblock %}

will automatically emit Bootstrap-compatible HTML. A minimal example to
generate a working navbar would be:

.. code-block:: python

    from flask_nav import Nav
    from flask_nav.elements import Navbar, View

    nav = Nav()

    @nav.navigation()
    def mynavbar():
        return Navbar(
            'mysite',
            View('Home', 'index'),
        )

    # ...

    nav.init_app(app)

See the sample application for a more detailed example on navigation.


The BootstrapRenderer
---------------------

The renderer for Bootstrap-specific HTML (available as
``flask_bootstrap.nav.BootstrapRenderer``) has a few specific features. Namely,
the ``title`` attribute of any :class:`~flask_nav.elements.Navbar` can also be
a :class:`~flask_nav.elements.Link` or :class:`~flask_nav.elements.View`.

The ``title``, if not ``None``, will be rendered using the ``brand`` classes
(see the `Bootstrap docs
<http://getbootstrap.com/components/#navbar-brand-image>`_ for details) and if
it has a ``get_url`` method, the return value of it will be the link for the
brand text.


Customizing the navbar
~~~~~~~~~~~~~~~~~~~~~~

To modify the output of the ``BootstrapRenderer``, it is possible to subclass
it and register the resulting child class as another renderer. See the
Flask-Nav_ documentation for `more information about that topic <http://pythonhosted.org/flask-nav/advanced-topics.html#implementing-custom-renderers>`_.

.. _Flask-Nav: http://pythonhosted.org/flask-nav
