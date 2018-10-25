"""
    Contains tests for the Sale class
"""
from unittest import TestCase
from app.models.sale import Sale
from app.models.product import Product

class SaleTestCase(TestCase):
    "TestCase for the Sale class"

    def setUp(self):
        "initialize variables"
        self.sale_obj = Sale(
            product_id = 1, 
            products_sold = 2, 
            seller_id = 3
        )
        self.product_obj = Product()
        self.product_data = dict(product_name="pk", product_price=300)

    def tearDown(self):
        "release resources"
        Sale.sales[:] = []
        Sale.products[:] = []

    def test_sale_object_created_successfully(self):
        "Test sale project creation was successful"
        self.assertListEqual(
            [1, 2, 3],
            [self.sale_obj.product_id, self.sale_obj.products_sold, self.sale_obj.seller_id]
        )

    def test_get_product_id(self):
        "Tests if product_id is returned"
        self.assertEqual(self.sale_obj.product_id, 1)
    
    def test_get_products_sold(self):
        "Tests if product_sold is returned"
        self.assertEqual(self.sale_obj.products_sold, 2)

    def test_get_seller_id(self):
        "Tests if seller_id is returned"
        self.assertEqual(self.sale_obj.seller_id, 3)

    def test_set_product_id(self):
        "Tests if sale sets product id"
        self.sale_obj.product_id = 1
        self.assertEqual(self.sale_obj.product_id, 1)

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
        self.assertIn("No products added yet", response['message'])

    def test_get_sale_returns_no_sales(self):
        "Tests return from get_sale with no product added"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.get_sale(1)
        self.assertIn('No Sales made yet', response['message'])

    def test_empty_product_id(self):
        "Tests if empty product_id is entered"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_id="", products_sold=3, seller_id=4)
        self.assertEqual(
            {'product_id': 'Product id is not a number'}, response)

    def test_empty_products_sold(self):
        "Tests if empty products_sold is entered"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_id=1, products_sold="", seller_id=4)
        self.assertEqual(
            {'products_sold': 'Products sold is not a number'}, response)

    def test_empty_seller_id(self):
        "Tests if empty seller_id is entered"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_id=1, products_sold=2, seller_id="")
        self.assertEqual(
            {'seller_id': 'Seller id is not a number'}, response)

    def test_product_id_cannot_be_zero(self):
        "Tests if product_id is zero"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_id=0, products_sold=1, seller_id=4)
        self.assertEqual(
            {'product_id': 'Product id can not be less than one'}, response)

    def test_products_sold_cannot_be_zero(self):
        "Tests if products_sold is zero"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_id=1, products_sold=0, seller_id=4)
        self.assertEqual(
            {'products_sold': 'Products sold can not be less than one'}, response)
    
    def test_seller_id_cannot_be_zero(self):
        "Tests if seller_id is zero"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_id=1, products_sold=1, seller_id=0)
        self.assertEqual(
            {'seller_id': 'Seller id can not be less than one'}, response)

    def test_input_not_empty_for_all_values_to_add_sale(self):
        "Tests if product_id, products_sold, seller_id are not empty"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_id="", products_sold="", seller_id="")
        self.assertEqual(
            {
                'product_id': 'Product id is not a number', 
                'products_sold': 'Products sold is not a number',
                'seller_id': 'Seller id is not a number' 
            }
            , response
        )
    
    def test_input_not_zero_for_all_values_to_add_sale(self):
        "Tests if product_id, products_sold, seller_id are not zero"
        self.product_obj.add_product(**self.product_data)
        response = self.sale_obj.add_sale(
            product_id=0, products_sold=0, seller_id=0)
        self.assertEqual(
            {
                'product_id': "Product id can not be less than one",
                'products_sold': "Products sold can not be less than one",
                'seller_id': "Seller id can not be less than one"
            }
            , response
        )
