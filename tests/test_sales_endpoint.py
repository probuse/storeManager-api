"""
    This module will contain tests for the sales endpoint
"""
from tests.base_tests import BaseTestCase

class SaleTestCase(BaseTestCase):
    "TestCase to test SaleEndPoint"

    def test_add_sale_returns_200_status_code(self):
        "Test adding sale returns 201 status code"
        with self.client:
            response = self.add_sale(1, 5, 1)
            self.assertEqual(response.status_code, 200)

    def test_add_sale_returns_message_to_user(self):
        "Test adding sale returns information of added sale"
        with self.client:
            self.add_product("egg", 500)
            sale_response = self.add_sale(1, 2, 1)
            self.assertIn(b'2 egg(s) successfully sold', sale_response.data)

    def test_add_sale_if_product_id_doesnot_exist(self):
        "Test adding sale with invalid product_id"
        with self.client:
            self.add_product("egg", 500)
            sale_response = self.add_sale(3, 2, 1)
            self.assertIn(b'Product with Product id 3 does not exist', sale_response.data)

    def test_get_sales_returns_200_status_code(self):
        "Test a GET request to /sales returns a 200 status code"
        with self.client:
            response = self.get_sales()
            self.assertEqual(response.status_code, 200)

    def test_get_sales_when_no_sales_have_been_made(self):
        "Test request to /sales returns a message to user with no sales"
        with self.client:
            response = self.get_sales()
            self.assertIn(b'No Sales made yet', response.data)

    def test_get_sales_when_sales_have_been_made(self):
        "Test request to /sales returns a message to user with sales"
        with self.client:
            self.add_product("egg", 500)
            self.add_sale(1, 2, 1)
            response = self.get_sales()
            self.assertIn(b'2', response.data)

    def test_get_a_sale_returns_200_status_code(self):
        "Test /sales/<sale_id> endpoint responds with a 200 status code"
        with self.client:
            self.add_product("egg", 500)
            self.add_sale(1, 2, 1)
            response = self.get_a_sale(1)
            self.assertEqual(response.status_code, 200)
