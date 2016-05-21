Flask-SQLAlchemy support
========================

`Flask-SQLAlchemy <https://pythonhosted.org/Flask-SQLAlchemy/>`_ supports
pagination through its :meth:`~flask_sqlalchemy.BaseQuery.paginate`, which
will return a :class:`~flask_sqlalchemy.Pagination` object. These can
automatically rendered through the ``render_pagination`` macro:

.. code-block:: jinja

  {% from "bootstrap/pagination.html" import render_pagination %}

  {# ... #}

  {{render_pagination(query_results)}}

.. py:function:: render_pagination(pagination,\
                     endpoint=None,\
                     prev='«',\
                     next='»',\
                     ellipses='…',\
                     size=None,\
                     args={},\
                     **kwargs)

   Renders a pager for query pagination.

   :param pagination: :class:`~flask_sqlalchemy.Pagination` instance.
   :param endpoint: Which endpoint to call when a page number is clicked.
                    :func:`~flask.url_for` will be called with the given
                    endpoint and a single parameter, ``page``. If ``None``,
                    uses the requests current endpoint.
   :param prev: Symbol/text to use for the "previous page" button. If
                ``None``, the button will be hidden.
   :param next: Symbol/text to use for the "previous next" button. If
                ``None``, the button will be hidden.
   :param ellipses: Symbol/text to use to indicate that pages have been
                    skipped. If ``None``, no indicator will be printed.
   :param size: Can be 'sm' or 'lg' for smaller/larger pagination.
   :param args: Additional arguments passed to :func:`~flask.url_for`. If
                ``endpoint`` is ``None``, uses :attr:`~flask.Request.args` and
                :attr:`~flask.Request.view_args`
   :param kwargs: Extra attributes for the ``<ul>``-element.
