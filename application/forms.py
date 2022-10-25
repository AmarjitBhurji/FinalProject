# Links the database with your routes, by creating input forms.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField

class CustomerForm(FlaskForm):
    first_name = StringField("First Name")
    second_name = StringField("Last Name")
    email = StringField("Email")
    submit = SubmitField("Submit")

class ProductsForm(FlaskForm):
    name = StringField("Product Name")
    price = IntegerField("Price")
    amount = IntegerField("Amount")
    total = IntegerField("Total")
    submit = SubmitField("Submit")
