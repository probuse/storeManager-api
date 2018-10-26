"""
    This contains implementation of the Product class
"""
class Product:
    "Class for creating all objects in store"
    products = []

    def __init__(self, **kwargs):
        "Product takes in product_name and product_price"
        self._product_id = None
        self._product_name = kwargs.get('product_name', None)
        self._product_price = kwargs.get('product_price', None)
        self._product_quantity = kwargs.get('product_quantity', 1)


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

        if valid:
            if Product.products:
                for product in Product.products:
                    if product.product_name == product_name:
                        return {
                            'message' : 'Product {} already exists'.format(product_name)
                        }

            product_id = len(Product.products) + 1
            new_product = Product(
                product_name = product_name,
                product_price = product_price,
            )
            new_product.product_id = product_id
            Product.products.append(new_product)
            return {
                'message': 'Product {} with id {} successfully added'.format(
                    product_name, product_id),
                }, 201
        else:
            return errors


    def get_all_products(self):
        "returns a list of all products"
        response_data = []
        if Product.products:
            for product in Product.products:
                data = dict(
                    product_id = product.product_id,
                    product_name = product.product_name,
                    product_price = product.product_price,
                    product_quantity = product.product_quantity
                )
                response_data.append(data)
            return {'result': response_data}
                
        return {'message': 'No Products added yet'}

    def get_product(self, product_id):
        "returns product whose id is product_id"
        if Product.products:
            for product in Product.products:
                if product.product_id == int(product_id):
                    response_data = dict(
                            product_id=product.product_id,
                            product_name=product.product_name,
                            product_price=product.product_price,
                            product_quantity=product.product_quantity
                        )
                    return {'result': response_data}
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
