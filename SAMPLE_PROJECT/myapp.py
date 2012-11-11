#!/usr/bin/env python
# coding=utf8

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form, TextField, HiddenField, ValidationError,\
                          Required, RecaptchaField

app = Flask(__name__)
Bootstrap(app)

app.config['BOOTSTRAP_USE_MINIFIED'] = True
app.config['BOOTSTRAP_USE_CDN'] = True
app.config['BOOTSTRAP_FONTAWESOME'] = True
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'


class ExampleForm(Form):
    field1 = TextField('First Field', description='This is field one.')
    field2 = TextField('Second Field', description='This is field two.',
                       validators=[Required()])
    hidden_field = HiddenField('You cannot see this', description='Nope')
    recaptcha = RecaptchaField('A sample recaptcha field')

    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')


@app.route('/', methods=('GET', 'POST',))
def index():
    form = ExampleForm()
    if form.validate_on_submit():
        return "PASSED"
    return render_template('example.html', form=form)


if '__main__' == __name__:
    app.run(debug=True)
