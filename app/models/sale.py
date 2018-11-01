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
        self._product_name = kwargs.get("product_name", None)
        self._products_sold = kwargs.get("products_sold", None)
        self._seller_id = kwargs.get("seller_id", None)
        self.total_amount = kwargs.get("total_amount", 0)
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
    def product_name(self):
        "gets product name"
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        "sets product name"
        self._product_name = product_name

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
        valid, errors = self.validate_sale(**data)
        product_name = data['product_name']
        products_sold = data['products_sold']
        seller_id = data['seller_id']
        sale_date = str(datetime.now().date())
        product_quantity = 0

        if valid:
            product_dict = self.db_helper.get_product_by_name(product_name)
            products = self.db_helper.get_products_from_db()

            if product_dict:
                product_id = product_dict['product_id']
                product = self.db_helper.get_a_product_from_db(product_id)
                product_quantity = product['product_quantity']
            # else:
            #     return {
            #         'message': 'Product with Product name {} does not exist'.format(product_name)
            #     }
            # if product:
            #     product_quantity = product['product_quantity']
            else:
                return {
                    'message': 'Product with Product name {} does not exist'.format(product_name)
                }
            
            if product_quantity < products_sold:
                return {
                    'message': 'Sale not possible Product {} has {} product(s) left'.format(
                        product_name, product_quantity
                    )
                }
        
            if products:
                for product in products:
                    if product['product_name'] == product_name:
                        total_amount = products_sold * product['product_price']
                        sale = Sale(
                            product_name=product_name,
                            products_sold=products_sold, 
                            seller_id=seller_id,
                            total_amount=total_amount,
                            sale_date=sale_date
                        )
                        current_stock = product_quantity - products_sold
                        updated_product = Product(
                            product_name = product['product_name'],
                            product_quantity = current_stock,
                            product_price = product['product_price']
                        )
                        updated_product.product_id = product_id
                        self.db_helper.add_sale_to_db(sale)
                        self.db_helper.modify_a_product_in_db(updated_product)

                        return {
                            'message': '{} {}(s) successfully sold'.format(
                                    products_sold, 
                                    product['product_name']
                                )
                        }, 201
            return {
                'message': 'No Products added yet'
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
                        product_name=sale['product_name'],
                        products_sold=sale['products_sold'],
                        total_amount=sale['total_amount'],
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
                    product_name = sale['product_name'],
                    products_sold = sale['products_sold'],
                    total_amount=sale['total_amount'],
                    sale_date = sale['sale_date']
                )
                response_data.append(data)
            return response_data
        return {'message': 'No Sales made yet'}

    def validate_sale(self, **data):
        "validates product"
        is_product_name_valid = False
        is_products_sold_valid = False
        is_seller_id_valid = False

        product_name = data['product_name']
        products_sold = data['products_sold']
        seller_id = data['seller_id']

        errors = {}

        if not str(product_name).strip() == "":
            if isinstance(product_name, str):
                is_product_name_valid = True
            else:
                errors['product_name'] = "Product name is not a valid string"
        else:
            errors['product_name'] = "Product name can not be empty"

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

        return is_product_name_valid and is_products_sold_valid \
            and is_seller_id_valid, errors
