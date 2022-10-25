# Links the database with your routes, by creating input forms.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField

class CustomerForm(FlaskForm):
    first_name = StringField("Task")
    second_name = IntegerField("Lists ID")
    email = StringField("Email")
    submit = SubmitField("Submit")

class ProductsForm(FlaskForm):
    name = StringField("Product Name")
    price = IntegerField("Price")
    amount = IntegerField("Amount")
    total = IntegerField("Total")
    submit = SubmitField("Submit")