"""
    Contains helper functions
"""

def validate_product_name(product_name):
    "validates product name"
    if str(product_name).strip() == "" or len(str(product_name)) == 0:
        return "Product Name can not be empty"
    elif not str(product_name).strip().isalnum():
        return "Product Name must be contain atleast a letter or a digit"
    return product_name

def validate_product_price(product_price):
    "validates product price"
    if isinstance(product_price, str):
        return "Product Price can not be a string"
    if not isinstance(product_price, int):
        return "Product Price must be an integer"
    elif product_price == 0:
        return "Product Price can not be zero"
    elif product_price < 0:
        return "Product Price can not be a negative"
    return product_price

def validate_product_quantity(product_quantity):
    "validates product quantity"
    if isinstance(product_quantity, str):
        return "Product Quantity can not be a string"
    if not isinstance(product_quantity, int):
        return "Product Quantity must be an integer"
    elif product_quantity == 0:
        return "Product Quantity can not be zero"
    elif product_quantity < 0:
        return "Product Quantity can not be a negative"
    return product_quantity
