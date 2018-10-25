"""
    Contains helper functions
"""

# def validate_product_name(product_name):
#     "validates product name"
#     if str(product_name).strip() == "" or len(str(product_name)) == 0:
#         return "Product Name can not be empty"
#     elif not str(product_name).strip().isalnum():
#         return "Product Name must be contain atleast a letter or a digit"
#     return product_name

# def validate_product_price(product_price):
#     "validates product price"
#     if isinstance(product_price, str):
#         return "Product Price can not be a string"
#     if not isinstance(product_price, int):
#         return "Product Price must be an integer"
#     elif product_price == 0:
#         return "Product Price can not be zero"
#     elif product_price < 0:
#         return "Product Price can not be a negative"
#     return product_price

# def validate_product_quantity(product_quantity):
#     "validates product quantity"
#     if isinstance(product_quantity, str):
#         return "Product Quantity can not be a string"
#     if not isinstance(product_quantity, int):
#         return "Product Quantity must be an integer"
#     elif product_quantity == 0:
#         return "Product Quantity can not be zero"
#     elif product_quantity < 0:
#         return "Product Quantity can not be a negative"
#     return product_quantity

# def validate_product_id(product_id):
#     "validates product id"
#     if product_id == 0:
#         return "Product id can not be 0"
#     elif str(product_id).strip() == "" or len(str(product_id).strip()) == 0:
#         return "Product id can not be empty"
#     elif isinstance(product_id, str):
#         return "Product id can not be a string"
#     elif product_id is not None and int(product_id) < 0:
#         return "Product id must be greater than zero"
#     return product_id

# def validate_products_sold(products_sold):
#     "validates products sold"
#     if products_sold == 0:
#         return "Products sold can not be 0"
#     elif str(products_sold).strip() == "" and len(str(products_sold)) == 0:
#         return "Products sold can not be empty"
#     elif isinstance(products_sold, str):
#         return "Products sold can not be a string"
#     elif products_sold is not None and int(products_sold) < 0:
#         return "Products sold must be greater than 0"
#     return products_sold

# def validate_seller_id(seller_id):
#     "validates seller id"
#     if seller_id == 0:
#         return "Seller id can not be 0"
#     elif seller_id is not None and int(seller_id) < 0:
#         return "Seller id must be greater than 0"
#     elif str(seller_id).strip() == "" or len(str(seller_id).strip()) == 0:
#         return "Seller id can not be empty"
#     elif isinstance(seller_id, str):
#         return "Seller id can not be a string"
#     return seller_id
    