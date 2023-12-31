from pydoc import cli
from clientes.crud import Clientes
from connection import connect_db, close_connection


if __name__ == '__main__':

    conn = connect_db()
    cursor = conn.cursor()

    _request = input("Escoge una opcion:\r\n 1: Clientes \r\n 2: Activos \r\n 3: Equipos \r\n")

    if _request == '1':
        _request = input("Escoge una opcion:\r\n 1: Crear \r\n 2: Listar \r\n 3: Detalle \r\n 4: Actualizar \r\n 5: Eliminar\r\n1")

        if _request == '1':
            cliente = Clientes(nombre='Brinks', nit='34235245') # Obligatorio __init__
            cliente.nombre_contacto = 'John Fawer'
            cliente.telefono = '24523 EXT 405'
            cliente.correo = 'negocios@ospinn.com'
            cliente.direccion = 'Calle 2'

            _id = cliente.create(cursor, conn)
            print(f'El id del cliente {cliente} es {_id}')

        elif _request == '2':
            clientes = Clientes.list(cursor)
            for cliente in clientes:
                print(f"""
                    Nombre: {cliente.nombre} \r\n
                    NIT: {cliente.nit} \r\n
                    Contacto: {cliente.nombre_contacto} \r\n
                    Teléfono: {cliente.telefono} \r\n
                    Dirección: {cliente.direccion} \r\n
                    Correo: {cliente.correo} \r\n
                    """
                    )

        elif _request == '3':
            pk = 5
            cliente = Clientes()
            cliente.retrieve(cursor, pk)
            print(cliente)
            print(f"""
                    Nombre: {cliente.nombre} \r\n
                    NIT: {cliente.nit} \r\n
                    Contacto: {cliente.nombre_contacto} \r\n
                    Teléfono: {cliente.telefono} \r\n
                    Dirección: {cliente.direccion} \r\n
                    Correo: {cliente.correo} \r\n
                    """
                    )
        
        elif _request == '4':
            pk = 5
            cliente = Clientes()
            cliente.retrieve(cursor, pk)
            valores = {
                "nombre": "Fase Pi",
                "nit": '098765',
                "contacto": "Ricardo Trujillo",
                "correo": "ricardotrujillo@transer.com"
            }

            cliente.update(conn, cursor, valores)

        elif _request == '5':
            pk = 9
            cliente = Clientes()
            cliente.retrieve(cursor, pk)
            cliente.delete(conn, cursor)

        
        
    close_connection(cursor, conn)