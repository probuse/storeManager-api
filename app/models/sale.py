"""
    Contains implementation of the Sale class
"""
from datetime import datetime
from app.utils import (
    validate_product_id, validate_products_sold, validate_seller_id
    )
class Sale:
    def __init__(self, **kwargs):
        self._sale_id = None
        self._product_id = validate_product_id(kwargs.get("product_id", None))
        self._products_sold = validate_products_sold(
            kwargs.get("products_sold", None)
        )
        self._seller_id = validate_seller_id(
            kwargs.get("seller_id", None)
        )
        self.sale_date = str(datetime.now().date())

    @property
    def sale_id(self):
        "gets sale id"
        return self._sale_id

    @sale_id.setter
    def sale_id(self, sale_id):
        "sets sale id"
        self._sale_id = sale_id

    @property
    def product_id(self):
        "gets product id"
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        "sets product id"
        self._product_id = product_id

    @property
    def products_sold(self):
        "gets products sold"
        return self._products_sold

    @products_sold.setter
    def products_sold(self, products_sold):
        "sets products sold"
        self._products_sold = products_sold 

    @property
    def seller_id(self):
        "gets seller id"
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        "sets seller_id"
        self._seller_id = seller_id