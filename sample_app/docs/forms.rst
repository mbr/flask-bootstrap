WTForms support
================

The ``bootstrap/wtf.html`` template contains macros to help you output forms
quickly. Flask-WTF_ is not a dependency of Flask-Bootstrap, however, and must be
installed explicitly. The API of Flask-WTF_ has changed quite a bit over the
last few versions, Flask-Bootstrap is currently developed for Flask-WTF_ version
0.9.2.

The most basic way is using them as an aid to create a form by hand:

.. code-block:: jinja

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
--------------------

.. py:function:: quick_form(form,\
                    action=".",\
                    method="post",\
                    extra_classes=None,\
                    role="form",\
                    form_type="basic",\
                    horizontal_columns=('lg', 2, 10),\
                    enctype=None,\
                    button_map={},\
                    id="",\
                    render_kw={})

   Outputs Bootstrap-markup for a complete Flask-WTF_ form.

   :param form: The form to output.
   :param method: ``<form>`` method attribute.
   :param extra_classes: The classes to add to the ``<form>``.
   :param role: ``<form>`` role attribute.
   :param form_type: One of ``basic``, ``inline`` or ``horizontal``. See the
                     Bootstrap_ docs for details on different form layouts.
   :param horizontal_columns: When using the horizontal layout, layout forms
                              like this. Must be a 3-tuple of ``(column-type,
                              left-column-size, right-column-size)``.
   :param enctype: ``<form>`` enctype attribute. If ``None``, will
                    automatically be set to ``multipart/form-data`` if a
                    :class:`~wtforms.fields.FileField` is present in the form.
   :param button_map: A dictionary, mapping button field names to names such as
                      ``primary``, ``danger`` or ``success``. Buttons not found
                      in the ``button_map`` will use the ``default`` type of
                      button.
   :param id: The ``<form>`` id attribute.
   :param render_kw: A dictionary, specifying custom attributes for the
                     ``<form>`` tag.

.. py:function:: form_errors(form, hiddens=True)

   Renders paragraphs containing form error messages. This is usually only used
   to output hidden field form errors, as others are attached to the form
   fields.

   :param form: Form whose errors should be rendered.
   :param hiddens: If ``True``, render errors of hidden fields as well. If
                   ``'only'``, render *only* these.


.. py:function:: form_field(field,\
                            form_type="basic",\
                            horizontal_columns=('lg', 2, 10),\
                            button_map={})

    Renders a single form-field with surrounding elements. Used mainly by
    ``quick_form``.

.. _Flask-WTF: https://flask-wtf.readthedocs.org/en/latest/
.. _Bootstrap: http://getbootstrap.com/

