Macros
======

.. highlight:: jinja

Flask-Bootstrap comes with macros to make your life easier. These need to be
imported like in this example::

  {% extends "bootstrap/base.html" %}
  {% import "bootstrap/wtf.html" as wtf %}

This would import the ``wtf.html`` macros with the name-prefix of ``wtf``
(these are discussed below at :doc:`forms`).

In addition to the small macros on this page, broad support for other libraries
is also available; see :doc:`forms` and :doc:`sqlalchemy` for details.


Browser support
---------------

Bootstrap v4 dropped IE8, IE9, and iOS 6 support.
v4 is now only IE10+ and iOS 7+. For sites needing either of those, use v3.


Google Analytics
----------------

The `Google Analytics <http://www.google.com/analytics/>`_ API has changed
fairly quickly recently, currently `analytics.js
<https://developers.google.com/analytics/devguides/collection/analyticsjs/>`_
is best supported, using the ``uanalytics(id, options='auto')`` macro::

  {% import "bootstrap/google.html" as google %}

  {% block scripts %}
    {{super()}}
    {{google.uanalytics('U-XXXX-YY')}}
  {% endblock %}

It is possible to pass through options to the ``ga()`` js function call, for
example to utilize the `User ID <https://developers.google.com/analytics/
devguides/collection/analyticsjs/user-id>`_ feature::

  {{google.uanalytics('U-XXXX-YY', {'userId': 'myUser'})}}

If you want the analytics account to be configurable from the outside, you can
use something like this instead::

  {{google.uanalytics(config['GOOGLE_ANALYTICS_ID'])}}


.. note:: Please make sure you at least pseudomize user ids properly.

The officially deprecated `ga.js
<https://developers.google.com/analytics/devguides/collection/gajs/>`_ API
support is also available supported through a similarly named macro
``analytics(account)``::

  {{google.analytics(account=config['GOOGLE_ANALYTICS_ID'])}}


Utilities
---------

A few extra template macros are available in the ``bootstrap/utils.html``
file. Like the form macros, these are intended to aid rapid application
development, until they are replaced with custom solutions in more mature
applications.

.. py:function:: flashed_messages(messages=None, container=True, transform=..., default_category=None, dismissible=False)

   Renders Flask's :func:`~flask.flash` messages. Maps commonly used categories
   to the slightly uncommon bootstrap css classes (i.e. ``error -> danger``).

   :param messages: A list of messages. If not given, will use
                    :func:`~flask.get_flashed_messages` to retrieve them.
   :param container: If true, will output a complete
                     ``<div class="container">`` element, otherwise just the
                     messages each wrapped in a ``<div>``.
   :param transform: A dictionary of mappings for categories. Will be looked up
                     case-insensitively. Default maps all Python loglevel
                     *names* to bootstrap CSS classes.
   :param default_category: If a category does not has a mapping in transform,
                            it is passed through unchanged. If
                            ``default_category`` is set, it is replaced with
                            this instead.
   :param dismissible: If true, will output a button to close an alert.
                       For fully functioning, dismissible alerts,
                       you must use the alerts JavaScript plugin.

Note that for this functionality to work properly, flashing messages must be
categorized with a valid bootstrap alert category (one of ``success``,
``info``, ``warning``, ``danger``).

Example:

.. code-block:: python

    flash('Operation failed', 'danger')

Versions of Flask-Bootstrap pre-3.3.5.7 did not escape the content of
``flashed_messages`` to allow HTML to be used. This behaviour has changed, the
preferred way to utilize HTML inside messages now is by using the
``Markup``-wrapper:


.. code-block:: python

    from flask import flash
    from markupsafe import Markup

    # ...

    flash(Markup('Flashed message with <b>bold</b> statements'), 'success')

    user_name = '<b>ad username'
    flash(Markup('<u>You</u> are our favorite user, <i>'
                 + user_name
                 + Markup('</i>!'),
         'danger')


.. py:function:: form_button(url, content, method='post', class='btn-link',\
                 **kwargs)

   Renders a button/link wrapped in a form.

   :param url: The endpoint to submit to.
   :param content: The inner contents of the button element.
   :param method: ``method``-attribute of the surrounding form.
   :param class: ``class``-attribute of the button element.
   :param kwargs: Extra html attributes for the button element.


A handy little method to create things like delete-buttons without using
``GET`` requests. An example::

  {{form_button(url_for('remove_entry', id=entry_id),
                icon('remove') + ' Remove entry')}}
