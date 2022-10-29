# How your databases are going to look.
from application import db

class Customer(db.Model):
    customer_id = db.Column(db.Integer(), primary_key=True)
    customer_name = db.Column(db.String(50))
    email = db.Column(db.String(50))

class Products(db.Model):
    product_id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String(30))
    price = db.Column(db.Float(3,2))
    fk_customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
