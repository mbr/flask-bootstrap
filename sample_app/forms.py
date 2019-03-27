from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, PasswordField, SelectMultipleField
from wtforms import SubmitField, BooleanField, RadioField, FileField
from wtforms import FloatField, DecimalField, IntegerField
from wtforms.fields.html5 import DateField, DateTimeField, EmailField, IntegerRangeField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import Required, Email


class SignupForm(FlaskForm):
    name = TextField(u'Your name', validators=[Required()])
    password = PasswordField(u'Your favorite password', validators=[Required()])
    email = EmailField(u'Your email address', validators=[Email()])
    birthday = DateField(u'Your birthday')

    a_float = FloatField(u'A floating point number')
    a_decimal = DecimalField(u'Another floating point number')
    a_integer = IntegerField(u'An integer')

    now = DateTimeLocalField(u'Current time Local',
                             description='...for no particular reason')
    now2 = DateTimeField(u'Current time',
                         description='...for no particular reason')

    ranger = IntegerRangeField('Ranger', render_kw={'step': 1})
    radio = RadioField('Radio', choices=[('vw', 'Volkswagen'),
                                         ('bmw', 'BMW'),
                                         ('benz', 'Mercedes')])
    select = SelectField('Brand',
                         choices=[('vw', 'Volkswagen'),
                                  ('bmw', 'BMW'),
                                  ('benz', 'Mercedes')],
                         default='bmw',
                         validators=[Required()])
    select_multi = SelectMultipleField('Brands',
                                       choices=[('vw', 'Volkswagen'),
                                                ('bmw', 'BMW'),
                                                ('benz', 'Mercedes')],
                                       default=['vw', 'benz'],
                                       validators=[Required()])

    sample_file = FileField(u'Your favorite file')
    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[Required('You must agree to not agree!')])

    submit = SubmitField(u'Signup')
