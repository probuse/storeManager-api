"""
    This module contains sales for the product object
"""
from tests.base_tests import BaseTestCase

class ProductTestCase(BaseTestCase):
    "TestCase to test ProductEndPoint"

    def test_add_product_returns_201_status_code(self):
        "Test adding product returns 201 status code"
        with self.client:
            response = self.add_product("egg", 500)
            self.assertEqual(response.status_code, 201)

    def test_add_product_returns_message_to_user_with_created_product(self):
        "Test adding product returns information of added product"
        with self.client:
            response = self.add_product("egg", 500)
            self.assertIn(b'Product egg with id 1 successfully added', response.data)

    def test_get_products_returns_200_status_code(self):
        "Test product endpoint responds with a 200 status code"
        with self.client:
            response = self.get_products()
            self.assertEqual(response.status_code, 200)

    def test_get_products_returns_no_products_added_yet_if_no_products_are_added(self):
        "Test product endpoint returns No Products added yet when no products are added"
        with self.client:
            response = self.get_products()
            self.assertIn(b'No Products added yet', response.data)

    def test_get_a_product_returns_200_status_code(self):
        "Test /product/<product_id> endpoint responds with a 200 status code"
        with self.client:
            response = self.get_a_product(1)
            self.assertEqual(response.status_code, 200)

    def test_get_products_returns_no_product_if_product_id_doesnot_exist(self):
        "Test product endpoint returns Product does not exists with invalid id"
        with self.client:
            self.add_product("egg", 500)
            response = self.get_a_product(2)
            self.assertIn(b'Product with id 2 does not exist', response.data)
