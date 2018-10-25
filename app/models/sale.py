"""
    Contains implementation of the Sale class
"""
from datetime import datetime
from app.utils import (
    validate_product_id, validate_products_sold, validate_seller_id
    )
from app.models.product import Product
class Sale:

    sales = []
    products = Product.products

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

    def get_sale(self, sale_id):
        "returns a sale with sale id"
        if Sale.products:
            if Sale.sales:
                for sale in Sale.sales:
                    if sale.sale_id == int(sale_id):
                        response_data = dict(
                                sale_id=sale.sale_id,
                                product_id=sale.product_id,
                                products_sold=sale.products_sold,
                                sale_date=sale.sale_date
                            )
                        return response_data
                return {'message': 'Sale with id {} does not exist'.format(sale_id)}
            return {'message': 'No Sales made yet'}
        return {'message': 'No products added yet'}
    
    def get_sales(self):
        "returns all sales"
        response_data = []
        if Sale.sales:
            for sale in Sale.sales:
                data = dict(
                    sale_id = sale.sale_id,
                    product_id = sale.product_id,
                    products_sold = sale.products_sold,
                    sale_date = sale.sale_date
                )
                response_data.append(data)
            return response_data
        return {'message': 'No Sales made yet'}

    def add_sale(self, **data):
        "Adds a sale"
        product_id = data['product_id']
        products_sold = data['products_sold']

        if Sale.products:
            for product in Sale.products:
                if product.product_id == int(product_id):
                    sale = Sale(
                        product_id = product.product_id,
                        products_sold = products_sold 
                    )
                    sale.sale_id = len(Sale.sales) + 1
                    Sale.sales.append(sale)
                    return {
                        'message': '{} {}(s) successfully sold'.format(
                            products_sold, 
                            product.product_name
                            )
                    }
        return {
            'message': 'Product with Product id {} does not exist'.format(product_id)
            }
