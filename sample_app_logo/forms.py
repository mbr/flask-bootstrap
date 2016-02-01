from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import Required, Email


class SignupForm(Form):
    name = TextField(u'Your name', validators=[Required()])
    password = TextField(u'Your favorite password', validators=[Required()])
    email = TextField(u'Your email address', validators=[Email()])
    birthday = DateField(u'Your birthday')

    a_float = FloatField(u'A floating point number')
    a_decimal = DecimalField(u'Another floating point number')
    a_integer = IntegerField(u'An integer')

    now = DateTimeField(u'Current time',
                        description='...for no particular reason')
    sample_file = FileField(u'Your favorite file')
    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[Required('You must agree to not agree!')])

    submit = SubmitField(u'Signup')
