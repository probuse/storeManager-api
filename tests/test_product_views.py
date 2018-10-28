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

    def test_user_can_send_a_put_request_to_products_endpoint_successfully(self):
        "Tests user can successfully send put request"
        with self.client:
            response = self.modify_product(1, "omo", 2300)
            self.assertEqual(response.status_code, 200)

    def test_user_can_successfully_modify_product(self):
        "Tests user can modify product successfully"
        with self.client:
            self.add_product("honey", 5000)
            response = self.modify_product(1, "magic", 3200)
            resp = self.get_a_product(1)
            self.assertIn(
                b'{"result": "Product successfully updated"}', 
                response.data
            )
            self.assertIn(
                b'{"result": {"product_id": 1, "product_name": "magic", "product_price": 3200, "product_quantity": 1}}',
                resp.data
            )
    
    def test_user_can_not_modify_product_that_doesnot_exist(self):
        "Tests user can not modify a non existing product"
        with self.client:
            self.add_product("egg", 500)
            response = self.modify_product(2, "omo", 2300)
            self.assertIn(
                b'{"message": "Product with id 2 does not exist"}', 
                response.data
            )
            
    def test_user_can_send_a_delete_request_to_products_endpoint_successfully(self):
        "Tests user can successfully send delete request"
        with self.client:
            response = self.delete_product(1)
            self.assertEqual(response.status_code, 200)

    def test_user_cannot_delete_product_if_no_products_are_added_yet(self):
        "Tests user can only delete product if products have been added"
        with self.client:
            response = self.delete_product(1)
            self.assertIn(b'{"message": "No Products added yet"}', response.data)

    def test_user_can_delete_product_if_it_exists(self):
        "Tests user can only delete product if it exists"
        with self.client:
            self.add_product("soda", 3000)
            response = self.delete_product(1)
            self.assertIn(
                b'{"result": "Product successfully deleted"}', response.data)

    def test_user_cannot_delete_product_which_does_not_exist(self):
        "Tests user can only delete product if it exists"
        with self.client:
            self.add_product("soda", 3000)
            response = self.delete_product(2)
            self.assertIn(
                b'{"message": "Product with id 2 does not exist"}', response.data)
