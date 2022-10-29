from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Customer, Products

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY="Test_Example_key",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app

    def setup(self):
        # Create tables
        db.create_all()

        #Create a test customer
        test_customer = Customer(name="Test_Customer")

        #Create a test products
        test_products = Products(name="Test_Products", fk_customer_id=1)

        db.session.add(test_customer)
        db.session.add(test_products)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# test for READ
class TestViews(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test_Customer", response.data)
        self.assertIn(b"Test_Products", 1, 1, response.data)

# test for CREATE
class TestViews(TestBase):
    def test_addproduct_get(self):
        response = self.client.get(url_for('addproduct'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test_Products", 1, 1, response.data)

class TestViews(TestBase):
    def test_addcustomer_get(self):
        response = self.client.get(url_for('addcustomer'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test_Customer", response.data)

# test for UPDATE
class TestViews(TestBase):
    def test_updateproduct_get(self):
        response = self.client.get(url_for('updateproduct'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test_Products", 1, 1, response.data)

class TestViews(TestBase):
    def test_updatecustomer_get(self):
        response = self.client.get(url_for('updatecustomer'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test_Customer", response.data)

# test for DELETE
class TestViews(TestBase):
    def test_deleteproduct_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test_Products", 1, 1, response.data)

class TestViews(TestBase):
    def test_deletecustomer_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test_Customer", response.data)
