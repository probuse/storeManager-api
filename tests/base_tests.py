"""
    This module will contain base tests for the api endpoints.
"""
import json
from unittest import TestCase
from app import app
from app.routes import products

class BaseTestCase(TestCase):
    def setUp(self):
        "initialize up a client to for testing"
        self.client = app.test_client(self)

    def tearDown(self):
        "Drop all data structures used for storage"
        products[:] = []

    def add_product(self):
        "allows user to post a product"
        return self.client.post(
            '/api/v1/products',
            data = json.dumps(dict(
                product_name="egg",
                product_price=500,
            )
        ),
            content_type='application/json'
        )


    def get_products(self):
        "return all available products"
        return self.client.get('/api/v1/products')