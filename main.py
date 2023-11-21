from clientes.crud import Clientes
from connection import connect_db, close_connection


if __name__ == '__main__':
    conn = connect_db()
    cursor = conn.cursor()

    _request = input("Escoge una opcion:\r\n 1: Clientes \r\n 2: Activos \r\n 3: Equipos \r\n")

    if _request == '1':
        _request = input("Escoge una opcion:\r\n 1: Crear \r\n 2: Listar \r\n")

        if _request == '1':
            cliente = Clientes(nombre='Brinks', nit='34235245') # Obligatorio __init__
            cliente.nombre_contacto = 'John Fawer'
            cliente.telefono = '24523 EXT 405'
            cliente.correo = 'negocios@ospinn.com'
            cliente.direccion = 'Calle 2'

            _id = cliente.create(cursor, conn)
            print(f'El id del cliente {cliente} es {_id}')

        
    close_connection(cursor, conn)