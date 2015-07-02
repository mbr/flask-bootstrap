# -*- coding: utf-8 -*-

project = u'Flask-Bootstrap'
copyright = u'2013, Marc Brinkmann'
version = '3.3.5.2'
release = '3.3.5.2.dev1'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'alabaster'

intersphinx_mapping = {'http://docs.python.org/': None,
                       'http://pythonhosted.org/Flask-SQLAlchemy/': None,
                       'http://flask.pocoo.org/docs/': None,
                       'https://wtforms.readthedocs.org/en/latest/': None,
                       }
