# How your databases are going to look.
from application import db

class Customer(db.Model):
    customer_id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(30))
    second_name = db.Column(db.String(30))
    email = db.Column(db.String(50))

class Products(db.Model):
    product_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float(3,2))
    amount = db.Column(db.Integer())
    total = db.Column(db.Integer())
    fk_customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
