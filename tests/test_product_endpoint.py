"""
    This module will contain sales for the product object
"""
from tests.base_tests import BaseTestCase

class ProductTestCase(BaseTestCase):

    def test_product_endpoint_responds_correctly(self):
        "Test product endpoint returns a 200 status code"
        with self.client:
            response = self.get_products()
            self.assertEqual(response.status_code, 200)