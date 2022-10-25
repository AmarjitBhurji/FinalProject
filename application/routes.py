# This is where your CREATE, READ, UPDATE AND DELETE functionality is going to go.
from asyncio import Task
from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Products, Customer
from application.forms import ProductsForm, CustomerForm

#READ BOTH DATABASES
#Location of this functionality: ip_address:4000/
@app.route('/', methods=['POST', 'GET'])
def index():
    customers = Customers.query.all()
    products = Productss.query.all()
    return render_template('index.html', title="Customer Order", customers=customers, products=products)

# CREATE customers
@app.route('/addcustomer', methods=['POST', 'GET'])
def customeradd():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(
            name = form.name.data
        )
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addcustomer.html', title="Enter Customer Details", form=form)

#CREATE products
#Location of this functionality: ip_address:5000/add
@app.route('/addproduct', methods=['POST','GET'])
def add():
    # This points to TodoForm
    form = ProductsForm()
    # Checks that we have clicked the submit button
    if form.validate_on_submit():
        # the variable tasks becomes what is put on the form
        # todos becomes what we are going to be adding to the database
        products = Products(
            products = form.products.data,
            # Foreign key as a option to add to the create process.
            fk_customer_id = form.fk_customer_id.data
        )
        # This performs the add to database
        db.session.add(products)
        # This commits those changes
        db.session.commit()
        # This one redirects to the index functions url
        return redirect(url_for('index'))
    # Otherwise return the template of addcustomer.html
    return render_template('addproduct.html', title="Add Product", form=form)

#UPDATE customer
@app.route('/updatecustomer/<int:customer_id>', methods=['GET', 'POST'])
def updatecustomer(customer_id):
    form = CustomerForm()

    Customer = Customer.query.get(customer_id)

    if form.validate_on_submit():
        customer.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = customer.name
    return render_template('updatecustomer.html', title='Update Customer Details', form=form)


#UPDATE products
@app.route('/updateproduct/<int:product_id>', methods=['GET', 'POST'])
def updateproduct(product_id):
    form = ProductsForm()
    # Get one tasks from the specified ID
    customer = Products.query.get(product_id)
    # POST method
    # If the user clicks submit
    if form.validate_on_submit():
        # What is put in the form gets ammended to the database
        product_id.products = form.products.data
        customer.fk_customer_id = form.fk_customer_id.data
        # Commit the changes
        db.session.commit()
        # Redirect to the url for index function
        return redirect(url_for('index'))
    # Else if the request method is a GET
    elif request.method == 'GET':
        # Update the form with whats in the database
        form.products.data = products.products
        form.fk_customer_id.data = products.fk_customer_id
    # If we go to the url return the template updatecustomer.html
    return render_template('updateproduct.html', title='Update Product', form=form)


#DELETE customer
@app.route('/deletecustomer/<int:customer_id>')
def deletecustomer(customer_id):
    customer = Customer.query.get(customer_id)
    db.session.delete(Customer)
    db.session.commit()
    return redirect(url_for('index'))

#DELETE products
#Location of this functionality: ip_address:4000/delete/1
@app.route('/delete/<int:product_id>')
def deleteproduct(product_id):
    # Collecting the task we want to delete based on its id
    products = Products.query.get(tid)
    # deleting this item from the database
    db.session.delete(products)
    # committing this change
    db.session.commit()
    # returning the url in the index function.
    return redirect(url_for('index'))
