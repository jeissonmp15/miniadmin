class Clientes:
    pk: int = None
    nombre: str = None
    nit: str = None
    nombre_contacto: str = None
    telefono: str = None
    direccion: str = 'null'
    correo: str = None

    def __str__(self):
        return self.nombre

    def __init__(self, nombre_param=None, nit_param=None) -> None:
        self.nombre = nombre_param
        self.nit = nit_param

        if self.nombre == 'OSP':
            self.nombre_contacto = 'Jeisson Manrique'

    def create(self, cursor, conn):
        query = f"""
            INSERT INTO Clientes (nombre, nit, contacto, telefono, direccion, correo)
            VALUES {self.nombre, self.nit, self.nombre_contacto, self.telefono, self.direccion, self.correo}
        """

        cursor.execute(query)
        _id = cursor.lastrowid
        conn.commit()

        return _id

    @staticmethod
    def list(cursor):
        query = "SELECT * FROM Clientes"
        cursor.execute(query)
        clientes_data = cursor.fetchall()
        print(clientes_data)
        clientes = []
        for cliente in clientes_data:
            kwargs = {
                "nombre_param": cliente[1],
                "nit_param": cliente[2],
            }
            instancia_cliente = Clientes(**kwargs)
            instancia_cliente.nombre_contacto = cliente[3]
            instancia_cliente.telefono = cliente[4]
            instancia_cliente.direccion = cliente[5]
            instancia_cliente.correo = cliente[6]

            clientes.append(instancia_cliente)

        return clientes

    def retrieve(self, cursor, pk):
        query = f"""SELECT * FROM Clientes WHERE pk = {pk} LIMIT 1"""
        cursor.execute(query)
        cliente_data = cursor.fetchone()
        self.pk = cliente_data[0]
        self.nombre = cliente_data[1]
        self.nit = cliente_data[2]
        self.nombre_contacto = cliente_data[3]
        self.telefono = cliente_data[4]
        self.direccion = cliente_data[5]
        self.correo = cliente_data[6]

    def update(self, conn, cursor, valores):
        query = f"""
            UPDATE Clientes SET nombre = '{valores['nombre']}', nit = '{valores['nit']}', contacto = '{valores['contacto']}', 
            correo = '{valores['correo']}'
            WHERE pk = {self.pk}
        """
        cursor.execute(query)
        conn.commit()

        self.retrieve(cursor, self.pk)

    def delete(self, conn, cursor, pk):
        query = f"DELETE FROM Clientes WHERE pk = {pk}"
        cursor.execute(query)
        conn.commit()
