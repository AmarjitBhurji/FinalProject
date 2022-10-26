# Links the database with your routes, by creating input forms.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField

from application.models import Customer, Products

class CustomerForm(FlaskForm):
    customer_id = IntegerField("Customer ID")
    customer_name = StringField("First Name")
    email = StringField("Email")
    submit = SubmitField("Submit")

class ProductsForm(FlaskForm):
    product_id = IntegerField("Product ID")
    product_name = StringField("Product Name")
    price = IntegerField("Price")
    fk_customer_id = IntegerField("Customer ID")
    submit = SubmitField("Submit")
