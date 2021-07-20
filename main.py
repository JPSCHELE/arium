from psql_reader import fetch_quantity
from mysql_reader import get_products
import time


products = get_products()
start_time = time.time()
contador = 0

for i in range(100):
    print("obteniendo producto",products[i].store_id)
    ean = products[i].ean
    print(ean)
    branch_id = products[i].store_id
    branch = products[i].branch
    response = fetch_quantity(ean,branch_id,branch)
    if len(response) > 0:
        products[i].stock = response[0]
        products[i].last_update = response[1]
    else:
        print("no se encontro stock")
        contador+=1

print(time.time() - start_time)   
print(" no se encontraton ", contador) 
