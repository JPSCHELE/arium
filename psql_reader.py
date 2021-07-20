import mysql.connector as mysql
import os
import psycopg2
from dotenv import load_dotenv




def fetch_quantity(ean, branch_code, chain):
    load_dotenv()
    host = os.getenv('PSQL-HOST')
    user = os.getenv('PSQL-USER')
    password = os.getenv('PSQL-PASS')
    database = os.getenv('PSQL-DB')
    result =[]
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cur = conexion.cursor()

    cur.execute("SELECT * from stock where ean = CAST({} as text) and branch_code = CAST({} as text) and stock.chain = '{}' and created_at = (SELECT MAX(created_at) FROM stock) order by date_1 desc limit 1".format(ean, branch_code, chain))
    
    for data in cur.fetchall():
        result = [data[5], str(data[11])]
        print(result)
    
    return result





