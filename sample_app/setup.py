import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-Bootstrap',
    version='3.3.7.2.dev1',
    url='http://github.com/mbr/flask-bootstrap',
    license='BSD',
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    description='An extension that includes Bootstrap in your '
    'project, without any boilerplate code.',
    long_description=read('README.rst'),
    packages=['flask_bootstrap'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8',
        'dominate',
        'visitor',
    ],
    classifiers=[
        'Environment :: Web Environment', 'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ])
