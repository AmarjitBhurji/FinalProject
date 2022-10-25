# How your databases are going to look.
from application import db

class Customer(db.Model):
    customer_id = db.Column(db.Integer(5), primary_key=True)
    first_name = db.Column(db.varchar(30))
    second_name = db.Column(db.varchar(30))
    email = db.Column(db.varchar(50))

class Products(db.Model):
    product_id = db.Column(db.integer(5), primary_key=True)
    name = db.Column(db.varchar(30))
    price = db.Column(db.decimal(3,2))
    amount = db.Column(db.integer(2))
    total = db.Column(db.integer(3))
    fk_customer_id = db.Column(db.integer, db.foreignkey('customer.customer_id'))
