"""
    Contains implementation of the Sale class
"""
from datetime import datetime
class Sale:
    def __init__(self, product_id, products_sold, seller_id=None):
        self.sale_id = None
        self.product_id = product_id
        self.products_sold = products_sold
        self.seller_id = seller_id
        self.sale_date = str(datetime.now().date())
