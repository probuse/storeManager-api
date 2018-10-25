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

    def test_sale_object_created_successfully(self):
        "Test sale project creation was successful"
        self.assertListEqual(
            [1, 2, 3],
            [self.sale_obj.product_id, self.sale_obj.products_sold, self.sale_obj.seller_id]
        )

    def test_product_id_cannot_be_zero(self):
        "Test product id is not Zero"
        sale = Sale(
            product_id = 0,
            products_sold = 2,
            seller_id = 1
        )
        self.assertEqual("Product id can not be 0", sale.product_id)

    
    def test_product_id_must_be_greater_than_zero(self):
        "Test product id must be greater than zero"
        sale = Sale(
            product_id = -3,
            products_sold = 2,
            seller_id = 1
        )
        self.assertEqual("Product id must be greater than zero", sale.product_id)

    def test_product_id_cannot_be_a_string(self):
        "Test product id is not string"
        sale = Sale(
            product_id = 'etwin',
            products_sold = 2,
            seller_id = 1
        )
        self.assertEqual("Product id can not be a string", sale.product_id)

    def test_product_id_cannot_be_empty(self):
        "Test product id is not empty"
        sale = Sale(
            product_id = '',
            products_sold = 2,
            seller_id = 1
            )
        self.assertEqual("Product id can not be empty", sale.product_id)

    def test_products_sold_cannot_be_zero(self):
        "Test products sold can not be zero"
        sale = Sale(
            product_id = 2,
            products_sold = 0,
            seller_id = 1
        )
        self.assertEqual("Products sold can not be 0", sale.products_sold)

    def test_products_sold_cannot_be_an_empty_string(self):
        "Test products sold can not be empty string"
        sale = Sale(
            product_id = 4,
            products_sold = '',
            seller_id = 1
        )
        self.assertEqual(
            "Products sold can not be empty", sale.products_sold)

    def test_products_sold_cannot_be_a_string(self):
        "Test products sold can not be a string"
        sale = Sale(
            product_id = 4,
            products_sold = 'ten',
            seller_id = 1
        )
        self.assertEqual(
            "Products sold can not be a string", sale.products_sold)

    def test_products_sold_must_be_greater_than_zero(self):
        "Test products sold must be greater than zero"
        sale = Sale(
            product_id = 4,
            products_sold = -2,
            seller_id = 1
        )
        self.assertEqual(
            "Products sold must be greater than 0", sale.products_sold)

    def test_seller_id_cannot_be_zero(self):
        "Test seller_id is not zero"
        sale = Sale(
            product_id = 4,
            products_sold = 3,
            seller_id = 0
        ) 
        self.assertEqual(
            "Seller id can not be 0", sale.seller_id)

    def test_seller_id_must_be_greater_than_zero(self):
        "Test seller_id is greater than zero"
        sale = Sale(
            product_id = 4,
            products_sold = 3,
            seller_id = -3
        ) 
        self.assertEqual(
            "Seller id must be greater than 0", sale.seller_id)

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


