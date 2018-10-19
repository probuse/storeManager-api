"""
    This module contains sales for the product object
"""
from tests.base_tests import BaseTestCase

class ProductTestCase(BaseTestCase):
    "TestCase to test ProductEndPoint"

    def test_add_product_returns_201_status_code(self):
        "Test adding product returns 201 status code"
        with self.client:
            response = self.add_product()
            self.assertEqual(response.status_code, 201)

    def test_add_product_returns_message_to_user_with_created_product(self):
        "Test adding product returns information of added product"
        with self.client:
            response = self.add_product()
            self.assertIn(b'Product egg with id 1 successfully added', response.data)

    def test_get_products_returns_200_status_code(self):
        "Test product endpoint responds with a 200 status code"
        with self.client:
            response = self.get_products()
            self.assertEqual(response.status_code, 200)

    def test_get_a_product_returns_200_status_code(self):
        "Test /product/<product_id> endpoint responds with a 200 status code"
        with self.client:
            response = self.get_a_product(1)
            self.assertEqual(response.status_code, 200)