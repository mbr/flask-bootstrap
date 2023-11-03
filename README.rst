===============
Flask-Bootstrap
===============

.. image:: https://travis-ci.org/mbr/flask-bootstrap.png?branch=master
   :target: https://travis-ci.org/mbr/flask-bootstrap

Flask-Bootstrap packages `Bootstrap
<http://getbootstrap.com>`_ into an extension that mostly consists
of a blueprint named 'bootstrap'. It can also create links to serve Bootstrap
from a CDN and works with no boilerplate code in your application.

this was a old project i dont know what is instore for it but i need to make my way to a fast devlopment envoirment
and i trust python to have all the cool new toys.
so all off the work in currently injected using a 3rd partk plugin
 todo:
  * tables spawn info in a sizeable table
   
  * row add i would like each row to be clonable
  * jquary card search. the header with the data type should have a list of data entiys and
     store colums that are not in use. this idea is that form data processing can be reviewed and linked
  * datatype index rework cards should have the data type stored on them
  * page needs more contrast shadows?
  * page storeage needs work
  * image storeage needs work

Usage
-----
.. image:: https://github.com/fenderrex/flask-bootstrap-SBadmin2-jquary/blob/master/dashboard3new.gif
Here is an example::

  from flask_bootstrap import Bootstrap

  [...]

  Bootstrap(app)

This makes some new templates available, containing blank pages that include all
bootstrap resources, and have predefined blocks where you can put your content.

As of version 3, Flask-Bootstrap has a `proper documentation
<http://pythonhosted.org /Flask-Bootstrap>`_, which you can check for more
details.
