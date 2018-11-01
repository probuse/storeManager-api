"""
    This contains implementation of the Product class
"""
from app import app
from db_helper import DBHelper
class Product:
    "Class for creating all objects in store"

    def __init__(self, **kwargs):
        "Product takes in product_name and product_price"
        self._product_id = None
        self._product_name = kwargs.get('product_name', None)
        self._product_price = kwargs.get('product_price', None)
        self._product_quantity = kwargs.get('product_quantity', 1)

        self.db_helper = DBHelper(app.config['DATABASE_URL'])

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

    def add_product(self, **data):
        "Adds a product to products list"
        valid, errors = self.validate_product(**data)
        product_name = data['product_name']
        product_price = data['product_price']
        product_quantity = data['product_quantity']
        
        product = Product(
            product_name=product_name,
            product_price=product_price,
            product_quantity=product_quantity
        )

        if valid:
            result = self.db_helper.add_product_to_db(product)
            if result:
                return {'message': result}
            return {'message': 'Product successfully added',}, 201
        else:
            return errors


    def get_all_products(self):
        "returns a list of all products"
        products = self.db_helper.get_products_from_db()
        if products:
            return {'result': products} 
        return {'message': 'No Products added yet'}

    def get_product(self, product_id):
        "returns product whose id is product_id"
        products = self.db_helper.get_products_from_db()
        product = self.db_helper.get_a_product_from_db(product_id)

        if products:
            if product:
                return {'result': product}
            return {
                'message': 'Product with id {} does not exist'.format(product_id)
            }, 404
        return {'message': 'No Products added yet'}, 404

    def modify_product(self, product_id, **data):
        "updates product"
        product_price = data.get('product_price')
        product_quantity = data.get('product_quantity')

        products = self.db_helper.get_products_from_db()
        product = self.db_helper.get_a_product_from_db(product_id)

        if products:
            if product:
                product_obj = Product(
                    product_price=product_price,
                    product_quantity=product_quantity
                ) 
                product_obj.product_id = product_id
                self.db_helper.modify_a_product_in_db(product_obj)

                return {'result': 'Product successfully updated'}
            return {
                'message': 'Product with id {} does not exist'.format(product_id)
            }
        return {'message': 'No Products added yet'}

    def delete_product(self, product_id):
        "deletes a product"
        products = self.db_helper.get_products_from_db()
        product = self.db_helper.get_a_product_from_db(product_id)
        if products:
            if product:
                self.db_helper.delete_a_product_from_db(product_id)
                return {'result': 'Product successfully deleted'}
            return {
                'message': 'Product with id {} does not exist'.format(product_id)
            }
        return {'message': 'No Products added yet'}

    def validate_product(self, **data):
        "validates product"
        is_price_valid = False
        is_name_valid = False

        product_name = data['product_name']
        product_price = data['product_price']

        errors = {} 
        try:
            product_price = int(product_price)
            if product_price < 1:
                errors['product_price'] = "Product Price can not be less than one"
            else:
                is_price_valid = True
        except ValueError:
            errors['product_price'] = "Price is not a number" 

        if isinstance(product_name, str) and str(product_name).isalpha():
            is_name_valid = True
        else:
            errors['product_name'] = "Product Name must be a string"

        return is_name_valid and is_price_valid, errors
