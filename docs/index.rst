===============
Flask-Bootstrap
===============

Flask-Bootstrap packages `Bootstrap <http://getbootstrap.com>`_ into an
extension that mostly consists of a blueprint named 'bootstrap'. It can also
create links to serve Bootstrap from a CDN.

.. toctree::
   basic-usage
   configuration
   cdn
   changelog
   faq
   bootstrap2
   :maxdepth: 2


Installation
------------

Either install from github using ``pip`` or from `PyPI
<http://pypi.python.org/pypi/Flask-Bootstrap>`_.


Getting started
---------------

To get started, go ahead by reading :doc:`basic-usage`. A list of Frequently
Asked Questions for advanced users or those of older versions can be found
below.


A note on versioning
--------------------

Flask-Bootstrap tries to keep some track of Bootstrap releases. Versioning is
usually in the form of ``Bootstrap version``.``Flask-Bootstrap iteration``.
For example, a version of ``2.0.3.2`` bundles Bootstrap version ``2.0.3`` and is
the second release of Flask-Bootstrap containing that version.

If you need to rely on your templates not changing, simply pin the version in
your setup.py.


Bootstrap 2 vs Bootstrap 3
--------------------------

The latest major version of Bootstrap as of this writing is Bootstrap 3. A
branch of Flask-Bootstrap supporting version 2 is still supported, see the page
on :doc:`bootstrap2` for details.


