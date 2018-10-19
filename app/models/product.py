"""
    This contains implementation of the Product class
"""
class Product:

    def __init__(self, product_name, product_price, product_count = 1):
        "Product takes in product_name and product_price"
        self.product_id = None
        self.product_name = product_name
        self.product_price = product_price
        self.product_count = product_count