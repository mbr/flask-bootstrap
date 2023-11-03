CDN support
===========

Flask-Bootstrap supports delivery via CDN or local resources, configurable at
runtime. Upon initialization, Flask-Bootstrap will store a dictionary on your
app named ``yourapp.extensions['bootstrap']['cdns']``, which maps names to
:py:class:`~flask_bootstrap.CDN` instances.

You can use :py:func:`~flask_bootstrap.bootstrap_find_resource` in your
templates as well when using other resources that may be available on CDNs.
CDNs can be added by adding new entries to the dictionary mention above.

.. autoclass:: flask_bootstrap.CDN
   :members:

.. autoclass:: flask_bootstrap.StaticCDN
   :members:

.. autoclass:: flask_bootstrap.WebCDN
   :members:

.. autofunction:: flask_bootstrap.bootstrap_find_resource
