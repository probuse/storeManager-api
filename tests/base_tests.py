"""
    This module will contain base tests for the api endpoints.
"""
import json
from app import app
from db_helper import DBHelper
from unittest import TestCase
from app import app

class BaseTestCase(TestCase):
    def setUp(self):
        "initialize up a client to for testing"
        self.client = app.test_client(self)
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        
        self.db_helper.create_users_table()
        self.db_helper.create_products_table()
        self.db_helper.create_sales_table()

    def get_home_view(self):
        "get request to home view"
        return self.client.get('/')

    def add_product(self, product_name, product_price, product_quantity):
        "allows user to add a product"
        return self.client.post(
            '/api/v1/products',
            data = json.dumps(dict(
                product_name=product_name,
                product_price=product_price,
                product_quantity=product_quantity
            )
        ),
            content_type='application/json'
        )


    def get_products(self):
        "return all available products"
        return self.client.get('/api/v1/products')

    def get_a_product(self, product_id):
        "returns a single product"
        return self.client.get('/api/v1/products/{}'.format(product_id))

    def add_sale(self, product_name, products_sold, seller_id):
        "allows user to add a sale"
        return self.client.post(
            '/api/v1/sales',
            data = json.dumps(
                dict(
                    product_name=product_name,
                    products_sold=products_sold,
                    seller_id = seller_id
                )
            ),
            content_type='application/json'
        )

    def get_sales(self):
        "return all sales made"
        return self.client.get('/api/v1/sales')

    def get_a_sale(self, sale_id):
        "returns a single sale"
        return self.client.get('/api/v1/sales/{}'.format(sale_id))

    def modify_product(self, product_id, product_price, product_quantity):
        "allows user to modiy a product"
        return self.client.put(
            '/api/v1/products/{}'.format(product_id),
            data=json.dumps(dict(
                product_name=product_id,
                product_price=product_price,
                product_quantity=product_quantity
            )
            ),
            content_type='application/json'
        )

    def delete_product(self, product_name):
        "allows user to delete a product"
        return self.client.delete(
            '/api/v1/products/{}'.format(product_name),
        )

    def register_store_attendant(self, **data):
        "allows admin to add a store attendant"
        usernames = data.get('usernames')
        email = data.get('email')
        phone_number = data.get('phone_number')
        password = data.get('password')
        return self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(dict(
                usernames=usernames,
                email=email,
                is_admin=False,
                phone_number=phone_number,
                password=password
            )
            ),
            content_type='application/json'
        )

    def get_store_attendants(self):
        "return all available store attendants"
        return self.client.get('/api/v1/store-attendants')

    def login_store_attendant_user(self, email, password, is_admin):
        "allows store attendant to login"
        return self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(
                dict(
                    email=email,
                    password=password, 
                    is_admin=is_admin
                                   )
            ),
            content_type='application/json'
        )

    def login_admin_user(self, email, password, is_admin):
        "allows admin to login"
        return self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(
                dict(
                    email=email,
                    password=password, 
                    is_admin=is_admin
                                   )
            ),
            content_type='application/json'
        )
