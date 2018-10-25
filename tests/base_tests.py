"""
    This module will contain base tests for the api endpoints.
"""
import json
from unittest import TestCase
from app import app
from app.views.products_views import products
from app.views.sales_views import sales

class BaseTestCase(TestCase):
    def setUp(self):
        "initialize up a client to for testing"
        self.client = app.test_client(self)

    def tearDown(self):
        "Drop all data structures used for storage"
        products[:] = []
        sales[:] = []

    def add_product(self, product_name, product_price):
        "allows user to post a product"
        return self.client.post(
            '/api/v1/products',
            data = json.dumps(dict(
                product_name=product_name,
                product_price=product_price,
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

    def add_sale(self, product_id, products_sold):
        "allows user to post a sale"
        return self.client.post(
            '/api/v1/sales',
            data = json.dumps(
                dict(
                    product_id=product_id,
                    products_sold=products_sold
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


