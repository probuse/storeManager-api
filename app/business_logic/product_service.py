
from app import app
from db_helper import DBHelper

class ProductService:
    def __init__(self):
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        
    def get_product(self, product_id):
        "returns product whose id is product_id"
        products = self.db_helper.get_products_from_db()
        product = self.db_helper.get_a_product_from_db(product_id)

        if products:
            if product:
                return {'result': product}
            return {
                'message': 'Product with id {} does not exist'.format(product_id)
            }
        return {'message': 'No Products added yet'}
