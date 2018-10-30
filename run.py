"""
    This is the main entry into the app, it runs the application
"""
from app import app
from db_helper import DBHelper


if __name__ == '__main__':
    db_helper = DBHelper(app.config['DATABASE_URL'])
    db_helper.create_users_table()
    db_helper.create_products_table()
    db_helper.create_sales_table()
    app.run(debug=True)