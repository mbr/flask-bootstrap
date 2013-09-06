Configuration
=============

There are a few configuration options used by the templates:

====================================== ======================================================== ===
Option                                 Default
====================================== ======================================================== ===
``BOOTSTRAP_USE_MINIFIED``             ``True``                                                 Whether or not to use the minified versions of the css/js files.
``BOOTSTRAP_JQUERY_VERSION``           ``'1'``                                                  This version of jQuery is included in the template via CDN. Also honors ``BOOTSTRAP_USE_MINIFIED``. Set this to ``None`` to not include jQuery at all.
``BOOTSTRAP_USE_CDN``                  ``False``                                                If ``True``, Bootstrap resources will no be served from the local app instance, but will use a Content Delivery Network instead (configured by ``BOOTSTRAP_CDN_BASEURL``).
``BOOTSTRAP_CDN_BASEURL``              A dictionary set up with URLs to ``cdnjs.com``.          The URLs to which Bootstrap and other filenames are appended when using a CDN.
``BOOTSTRAP_CDN_PREFER_SSL``           ``True``                                                 If the ``BOOTSTRAP_CDN_BASEURL`` starts with ``//``, prepend ``'https:'`` to it.
``BOOTSTRAP_QUERYSTRING_REVVING``      ``True``                                                 If ``True``, will apppend a querystring with the current version to all static resources served locally. This ensures that upon upgrading Flask-Bootstrap, these resources are refreshed.
====================================== ======================================================== ===
