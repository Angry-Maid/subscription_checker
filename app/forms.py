from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField,
    DecimalField, SelectField,
    IntegerField
)
from wtforms.validators import (
    InputRequired, NumberRange
)

from app import app


class SubscriptionForm(FlaskForm):
    name = StringField('Name', [InputRequired(), ])
    cost = DecimalField('Cost', [InputRequired(), ])
    currency = SelectField('Currency', choices=[
        (symbol.upper(), ) * 2 for symbol in app.config['SYMBOLS'].split(',')
    ])
    billing_date = IntegerField('Billing Day', [InputRequired(), NumberRange(min=1, max=31)])
    submit = SubmitField('Save')
