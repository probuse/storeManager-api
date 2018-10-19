"""
    Contains tests for the Sale class
"""
from unittest import TestCase
from app.models.sale import Sale

class SaleTestCase(TestCase):
    "TestCase for the Sale class"

    def test_sale_object_created_successfully(self):
        "Test sale project creation was successful"
        sale = Sale(1, 2, 3)
        self.assertListEqual(
            [1, 2, 3],
            [sale.product_id, sale.products_sold, sale.seller_id]
        )

    def test_sale_object_created_successfully_without_seller_id(self):
        "Test sale project creation was successful"
        sale = Sale(1, 2)
        self.assertListEqual(
            [1, 2, None],
            [sale.product_id, sale.products_sold, sale.seller_id]
        )