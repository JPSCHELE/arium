import mysql.connector as mysql
import os
from dotenv import load_dotenv
from branch_product import ProductBranch


def get_products():
    load_dotenv()

    host = os.getenv('MYSQL-HOST')
    user = os.getenv('MYSQL-USER')
    password = os.getenv('MYSQL-PASS')
    database = os.getenv('MYSQL-DB')
    products = []

    db = mysql.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    cursor = db.cursor()

    query = "select bp.id ,p.ean , b.store_id, UCASE(b.chain_name) from branch_product as bp join products p on p.id = bp.product_id join branches b on bp.branch_id = b.id where b.store_id IS NOT NULL"

    cursor.execute(query)


    data = cursor.fetchall()

    for i in data:
        products.append(ProductBranch(i[0], i[2], i[1], i[3]))
    
    return  products





