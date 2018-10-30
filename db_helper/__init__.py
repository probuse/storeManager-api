"""
    handles creation and deletion of database
"""
import psycopg2
import psycopg2.extras
from urllib.parse import urlparse

class DBHelper:
    def __init__(self, db_url):
        parsed_url = urlparse(db_url)
        db_name = parsed_url.path[1:]
        username = parsed_url.username
        host = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port

        self.conn = psycopg2.connect(
            database = db_name,
            user = username,
            password = password,
            host = host,
            port = port
        )  
        self.conn.autocommit = True
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

    # create tables
    def create_users_table(self):
        "creates users table"
        sql = """CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY,
                    usernames VARCHAR,
                    email VARCHAR NOT NULL UNIQUE,
                    phone_number VARCHAR,
                    is_admin BOOl NOT NULL,
                    password VARCHAR NOT NULL   
                )
                """
        self.cur.execute(sql)

    def create_products_table(self):
        "creates products table"
        sql = """CREATE TABLE IF NOT EXISTS products (
                    product_id SERIAL PRIMARY KEY,
                    product_name VARCHAR NOT NULL UNIQUE,
                    product_price INTEGER NOT NULL,
                    product_quantity INTEGER NOT NULL
                )
                """
        self.cur.execute(sql)

    def create_sales_table(self):
        "creates sales table"
        sql = """CREATE TABLE IF NOT EXISTS sales (
                    sale_id SERIAL PRIMARY KEY,
                    products_sold INTEGER NOT NULL,
                    seller_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    sale_date VARCHAR NOT NULL
                )
                """
        self.cur.execute(sql)

    def add_user_to_db(self, user):
        "adds user to database"
        sql = """INSERT INTO users 
                (usernames, email, phone_number, is_admin, password)
                VALUES (%s, %s, %s, %s, %s)
            """
        self.cur.execute(
            sql, 
            (
                user.usernames, 
                user.email, 
                user.phone_number, 
                user.is_admin, 
                user.password
            )
        )

    def get_store_attendants_from_db(self):
        "gets all store attendants"
        sql = "SELECT * FROM users"
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def add_product_to_db(self, product):
        "adds product to database"
        sql = """INSERT INTO products
                (product_name, product_price, product_quantity)
                VALUES (%s, %s, %s)
                """
        self.cur.execute(
            sql,
            (
                product.product_name,
                product.product_price,
                product.product_quantity
            )
        )
    
    def get_products_from_db(self):
        "gets all products"
        sql = "SELECT * FROM products"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_a_product_from_db(self, product_id):
        "gets a product with product_id"
        sql = "SELECT * FROM products WHERE product_id = %s"
        self.cur.execute(sql, product_id)
        return self.cur.fetchone()

    def modify_a_product_in_db(self, product):
        "modifies a product with product_id"
        sql = """UPDATE products 
                SET product_price=%s, product_quantity=%s
                WHERE product_name=%s
                """
        self.cur.execute(
            sql,
            (
                product.product_price,
                product.product_quantity,
                product.product_name,
            )
        )
    
    def delete_a_product_from_db(self, product_id):
        "deletes a product with product_id"
        sql = "DELETE FROM products WHERE product_id = %s"
        self.cur.execute(sql, product_id)

    def add_sale_to_db(self, sale):
        "adds sale to database"
        sql = """INSERT INTO sales
                (product_id, products_sold, seller_id, sale_date)
                VALUES (%s, %s, %s, %s)
                """
        self.cur.execute(
            sql,
            (
                sale.product_id,
                sale.products_sold,
                sale.seller_id,
                sale.sale_date
            )
        )

    def get_sales_from_db(self):
        "gets all sales"
        sql = "SELECT * FROM sales"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_a_sale_from_db(self, sale_id):
        "gets a sale with sale_id"
        sql = "SELECT * FROM sales WHERE sale_id = %s"
        self.cur.execute(sql, sale_id)
        return self.cur.fetchone()

    def drop_table(self):
        "drop database tables"
        self.cur.execute("DROP TABLE users")
        self.cur.execute("DROP TABLE products")
        self.cur.execute("DROP TABLE sales")


    