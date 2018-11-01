"""
    Contains tests for the Sale class
"""
import json
from unittest import TestCase
from app import app
from db_helper import DBHelper
from app.models.product import Product
from app.models.sale import Sale

class SaleTestCase(TestCase):
    "TestCase for the Sale class"

    def setUp(self):
        "initialize variables"
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        self.db_helper.create_users_table()
        self.db_helper.create_products_table()
        self.db_helper.create_sales_table()
        self.sale_obj = Sale(
            product_name = "omo", 
            products_sold = 2, 
            seller_id = 3
        )
        self.product_obj = Product()
        self.product_data = dict(
            product_name="pk", product_price=300, product_quantity=10
        )
    
    def tearDown(self):
        "drop database"
        self.db_helper.drop_database()


    def test_sale_object_created_successfully(self):
        "Test sale project creation was successful"
        self.assertListEqual(
            ["omo", 2, 3],
            [self.sale_obj.product_name, self.sale_obj.products_sold, self.sale_obj.seller_id]
        )

    def test_get_product_name(self):
        "Tests if product_name is returned"
        self.assertEqual(self.sale_obj.product_name, "omo")
    
    def test_get_products_sold(self):
        "Tests if product_sold is returned"
        self.assertEqual(self.sale_obj.products_sold, 2)

    def test_get_seller_id(self):
        "Tests if seller_id is returned"
        self.assertEqual(self.sale_obj.seller_id, 3)

    def test_set_product_name(self):
        "Tests if sale sets product name"
        self.sale_obj.product_id = "omo"
        self.assertEqual(self.sale_obj.product_id, "omo")

    def test_set_products_sold(self):
        "Tests if sale sets products sold"
        self.sale_obj.products_sold = 23
        self.assertEqual(self.sale_obj.products_sold, 23)

    def test_set_seller_id(self):
        "Tests if sale sets seller_id"
        self.sale_obj.products_sold = 23
        self.assertEqual(self.sale_obj.products_sold, 23)

    def test_get_sale_returns_no_products(self):
        "Tests return from get_sale with no product added"
        response = self.sale_obj.get_sale(1)
        self.assertIn("No Sales made yet", response['message'])

    def test_get_sale_returns_no_sales(self):
        "Tests return from get_sale with no product added"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.get_sale(1)
        self.assertIn('No Sales made yet', response['message'])

    def test_empty_product_name(self):
        "Tests if empty product_name is entered"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_name=" ", products_sold=3, seller_id=4)
        self.assertEqual(
            {'product_name': 'Product name can not be empty'}, response)

    def test_empty_products_sold(self):
        "Tests if empty products_sold is entered"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_name="posho", products_sold="", seller_id=4)
        self.assertEqual(
            {'products_sold': 'Products sold is not a number'}, response)

    def test_empty_seller_id(self):
        "Tests if empty seller_id is entered"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_name="pk", products_sold=2, seller_id="")
        self.assertEqual(
            {'seller_id': 'Seller id is not a number'}, response)

    def test_product_name_cannot_be_integer(self):
        "Tests if product_name can not Integer"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_name=23, products_sold=1, seller_id=4)
        self.assertEqual(
            {'product_name': 'Product name is not a valid string'}, response)

    def test_products_sold_cannot_be_zero(self):
        "Tests if products_sold is zero"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_name="pk", products_sold=0, seller_id=4)
        self.assertEqual(
            {'products_sold': 'Products sold can not be less than one'}, response)
    
    def test_seller_id_cannot_be_zero(self):
        "Tests if seller_id is zero"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_name="pk", products_sold=1, seller_id=0)
        self.assertEqual(
            {'seller_id': 'Seller id can not be less than one'}, response)

    def test_input_not_empty_for_all_values_to_add_sale(self):
        "Tests if product_name, products_sold, seller_id are not empty"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_name=" ", products_sold=" ", seller_id=" ")
        self.assertEqual(
            {
                'product_name': 'Product name can not be empty', 
                'products_sold': 'Products sold is not a number',
                'seller_id': 'Seller id is not a number' 
            }
            , response
        )
    
    def test_input_not_zero_for_all_values_to_add_sale(self):
        "Tests if product_name, products_sold, seller_id are not zero"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_name=0, products_sold=0, seller_id=0)
        self.assertEqual(
            {
                'product_name': "Product name is not a valid string",
                'products_sold': "Products sold can not be less than one",
                'seller_id': "Seller id can not be less than one"
            }
            , response
        )

    def test_product_quantity_is_modified_once_sale_is_made(self):
        "Tests is product quantity changes after sale is made"
        self.product_obj.add_product(**self.product_data)
        self.sale_obj.add_sale(product_name='pk', products_sold=5, seller_id=2)
        result = self.db_helper.get_a_product_from_db(1)
        self.assertEqual(
            5
            ,result['product_quantity']
        )

    def test_total_amount_after_sale(self):
        "Tests total amount after sale is made"
        self.product_obj.add_product(**self.product_data)
        self.sale_obj.add_sale(product_name='pk', products_sold=5, seller_id=2)
        result = self.db_helper.get_sales_from_db()
        self.assertEqual(
            1500
            ,result[0]['total_amount']
        )
        
