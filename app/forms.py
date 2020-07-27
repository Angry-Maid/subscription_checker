from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField,
    BooleanField, SubmitField,
    DecimalField, SelectField,
    IntegerField
)
from wtforms.validators import (
    InputRequired, NumberRange
)


class AddSubscription(FlaskForm):
    name = StringField('Name', [InputRequired(), ])
    cost = DecimalField('Cost', [InputRequired(), ])
    currency = SelectField('Currency', choices=[
        ('USD', 'USD'),
        ('EUR', 'EUR')
    ])
    billing_day = IntegerField('Billing Day', [InputRequired(), NumberRange(min=1, max=31)])
