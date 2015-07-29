from flask_wtf import Form
from wtforms.fields import TextField, SubmitField


class SignupForm(Form):
    name = TextField(u'Your name')
    submit = SubmitField(u'Signup')
