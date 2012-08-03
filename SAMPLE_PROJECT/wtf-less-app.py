#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_USE_CDN'] = True


@app.route('/')
def index():
    return render_template('noforms.html')


@app.route('/breakme/')
def breakme():
    return render_template('noformserror.html')


if __name__ == '__main__':
    app.run(debug=True)
