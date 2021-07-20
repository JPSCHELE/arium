import psycopg2
import os
import time

if __name__ == "__main__":

    host = 'database-1.col4iwqqbjnd.us-east-2.rds.amazonaws.com'
    database = 'arium'
    user = 'postgres'
    password = 'TCG2021$rs'

    try:
        conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    except:
        print('Error')

    cur = conexion.cursor()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('____________________________________________________')
        print('\t\t\tTCG LATAM')
        print('\t\tArium Quantity In Stcok')
        print('----------------------------------------------------')
        print("\t\t¿Qué desea realizar?")
        print('----------------------------------------------------')
        print(">[1].Buscar cantidad de articulos en stock")
        print(">[0].Salir")

        try:
            mainSelect = input('>>')
        except:
            print('Error: Invalid argument.')
        
        if mainSelect == '1':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('____________________________________________________')
                print("\tBuscar Cantidad De Articulos En Stock")
                print('----------------------------------------------------')
                print("\tIngresa los siguientes datos:")
                print('----------------------------------------------------')
                ean = input("1.EAN: ")
                branch_code = input("2.Codigo de Sucursal: ")
                chain = input("3.Cadena: ")
                print("\nBuscar: EAN: {} | Cod Sucursal: {} | Cadena: {} ?".format(ean,branch_code,chain))
                try:
                    print('')
                    confirm = input('Ejecutar busqueda [si/no]> ')
                except:
                    print('Error: Invalid argument.')
                
                if confirm == 'si':
                    start_time = time.time()
                    cur.execute("SELECT * from stock where ean = CAST({} as text) and branch_code = CAST({} as text) and stock.chain = '{}' and created_at = (SELECT MAX(created_at) FROM stock) order by id desc limit 1".format(ean, branch_code, chain))
                    
                    for data in cur.fetchall():
                        print("Last Quantity: (", data[5], ") date:", data[1])
                        print("Elapsed time:",time.time()-start_time,"seconds")
                    enter = input('\n[Enter] para continuar >> ')
                    break
                else: 
                    print('error')

        elif mainSelect == '0':
            conexion.close()
            break

            
        

