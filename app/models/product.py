"""
    This contains implementation of the Product class
"""
from app.utils import validate_product_name
class Product:

    def __init__(self, product_name, product_price, product_quantity = 1):
        "Product takes in product_name and product_price"
        self._product_id = None
        self._product_name = product_name
        self._product_price = product_price
        self._product_quantity = product_quantity

    @property
    def product_id(self):
        "Returns product id"
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        "Sets product_id"
        self._product_id = product_id

    @property
    def product_name(self):
        "Returns product name"
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        "Sets product_name"
        validate_product_name(product_name)
        self._product_name = product_name

    @property
    def product_price(self):
        "Returns product price"
        return self._product_price

    @product_price.setter
    def product_price(self, product_price):
        "Sets product_price"
        self._product_price = product_price

    @property
    def product_quantity(self):
        "Returns product quantity"
        return self._product_quantity

    @product_quantity.setter
    def product_quantity(self, product_quantity):
        "Sets product_quantity"
        self._product_quantity = product_quantity