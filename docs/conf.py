# -*- coding: utf-8 -*-

project = u'Flask-Bootstrap'
copyright = u'2013, Marc Brinkmann'
version = '3.3.7.2'
release = '3.3.7.2.dev1'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'alabaster']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'monokai'

html_theme = 'alabaster'
html_theme_options = {
    'github_user': 'mbr',
    'github_repo': 'flask-bootstrap',
    'description': 'All Bootstrap, no boilerplate.',
    'github_banner': True,
    'gratipay_user': 'mbr',
    'github_button': False,
    'show_powered_by': False,

    # required for monokai:
    'pre_bg': '#292429',
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

intersphinx_mapping = {'http://docs.python.org/': None,
                       'http://flask-sqlalchemy.pocoo.org/': None,
                       'http://pythonhosted.org/flask-nav/': None,
                       'http://flask.pocoo.org/docs/': None,
                       'https://wtforms.readthedocs.org/en/latest/': None, }
