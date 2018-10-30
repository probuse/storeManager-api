"""
    Contains implementation of the Sale class
"""
from app import app
from db_helper import DBHelper
from datetime import datetime
from app.models.product import Product
class Sale:

    sales = []
    products = Product.products

    def __init__(self, **kwargs):
        self._sale_id = None
        self._product_id = kwargs.get("product_id", None)
        self._products_sold = kwargs.get("products_sold", None)
        self._seller_id = kwargs.get("seller_id", None)
        self.sale_date = str(datetime.now().date())

        self.db_helper = DBHelper(app.config['DATABASE_URL'])

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

    def add_sale(self, **data):
        "Adds a sale"
        products = self.db_helper.get_products_from_db()

        valid, errors = self.validate_sale(**data)
        product_id = data['product_id']
        products_sold = data['products_sold']
        seller_id = data['seller_id']
        sale_date = str(datetime.now().date())

        if valid:
            if products:
                for product in products:
                    if product['product_id'] == int(product_id):
                        sale = Sale(
                            product_id=product_id,
                            products_sold=products_sold, 
                            seller_id=seller_id,
                            sale_date=sale_date
                        )
                        self.db_helper.add_sale_to_db(sale)

                        return {
                            'message': '{} {}(s) successfully sold'.format(
                                    products_sold, 
                                    product['product_name']
                                )
                        }
            return {
                'message': 'Product with Product id {} does not exist'.format(product_id)
                }
        return errors

    def get_sale(self, sale_id):
        "returns a sale with sale id"
        sales = self.db_helper.get_sales_from_db()
        sale = self.db_helper.get_a_sale_from_db(sale_id)

        if sales:
            if sale:
                response_data = dict(
                        sale_id=sale['sale_id'],
                        product_id=sale['product_id'],
                        products_sold=sale['products_sold'],
                        sale_date=sale['sale_date']
                    )
                return response_data
            return {'message': 'Sale with id {} does not exist'.format(sale_id)}
        return {'message': 'No Sales made yet'}
    
    def get_sales(self):
        "returns all sales"
        sales = self.db_helper.get_sales_from_db()

        response_data = []
        if sales:
            for sale in sales:
                data = dict(
                    sale_id = sale['sale_id'],
                    product_id = sale['product_id'],
                    products_sold = sale['products_sold'],
                    sale_date = sale['sale_date']
                )
                response_data.append(data)
            return response_data
        return {'message': 'No Sales made yet'}

    def validate_sale(self, **data):
        "validates product"
        is_product_id_valid = False
        is_products_sold_valid = False
        is_seller_id_valid = False

        product_id = data['product_id']
        products_sold = data['products_sold']
        seller_id = data['seller_id']

        errors = {}
        try:
            product_id = int(product_id)
            if product_id < 1:
                errors['product_id'] = "Product id can not be less than one"
            else:
                is_product_id_valid = True
        except ValueError:
            errors['product_id'] = "Product id is not a number"

        try:
            products_sold = int(products_sold)
            if products_sold < 1:
                errors['products_sold'] = "Products sold can not be less than one"
            else:
                is_products_sold_valid = True
        except ValueError:
            errors['products_sold'] = "Products sold is not a number"

        try:
            seller_id = int(seller_id)
            if seller_id < 1:
                errors['seller_id'] = "Seller id can not be less than one"
            else: 
                is_seller_id_valid = True
        except ValueError:
            errors['seller_id'] = "Seller id is not a number"

        return is_product_id_valid and is_products_sold_valid \
            and is_seller_id_valid, errors
