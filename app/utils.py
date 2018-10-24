"""
    Contains helper functions
"""

def validate_product_name(product_name):
    "validates product name"
    if str(product_name).strip() == "":
        raise NameError("Product Name can not be empty")
        
