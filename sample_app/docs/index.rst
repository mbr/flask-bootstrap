===============
Flask-Bootstrap
===============

Flask-Bootstrap packages `Bootstrap <http://getbootstrap.com>`_ into an
extension that mostly consists of a blueprint named 'bootstrap'. It can also
create links to serve Bootstrap from a CDN.

.. toctree::
   :maxdepth: 3

   basic-usage
   configuration
   macros
   forms
   sqlalchemy
   nav
   cdn
   faq
   bootstrap2
   changelog
   chinese_version


Installation
------------

Flask-Bootstrap can be installed using ``pip`` from `PyPI
<http://pypi.python.org/pypi/Flask-Bootstrap>`_. Using `virtualenv <http://www.virtualenv.org/en/latest/>`_ is recommended -- for no specific reason other than it being good practice. Installing is simple::

   pip install flask-bootstrap

For development, clone the `official github repository <https://github.com/mbr/flask-bootstrap>`_ instead and use::

   python setup.py develop


Getting started
---------------

To get started, go ahead by reading :doc:`basic-usage`. A list of :doc:`faq` is also available.

The latest major version of Bootstrap as of this writing is Bootstrap 3. A
branch of Flask-Bootstrap supporting version 2 is still supported, see the page
on :doc:`bootstrap2` for details.


A note on versioning
--------------------

Flask-Bootstrap tries to keep some track of Bootstrap releases. Versioning is
usually in the form of ``Bootstrap version``.``Flask-Bootstrap iteration``.
For example, a version of ``2.0.3.2`` bundles Bootstrap version ``2.0.3`` and is
the second release of Flask-Bootstrap containing that version.

If you need to rely on your templates not changing, simply pin the version in
your setup.py.
