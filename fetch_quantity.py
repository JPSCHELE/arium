import psycopg2

def fetch_quantity(ean, branch_code, chain):
    host = 'database-1.col4iwqqbjnd.us-east-2.rds.amazonaws.com'
    database = 'arium'
    user = 'postgres'
    password = 'TCG2021$rs'

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cur = conexion.cursor()

    cur.execute("SELECT * from stock where ean = CAST({} as text) and branch_code = CAST({} as text) and stock.chain = '{}' and created_at = (SELECT MAX(created_at) FROM stock) order by date_1 desc limit 1".format(ean, branch_code, chain))
    
    for data in cur.fetchall():
        result = [data[5], data[11]]
    print(result)
    return result

