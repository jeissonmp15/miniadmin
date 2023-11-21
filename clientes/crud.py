from re import S


class Clientes:
    nombre: str = None
    nit: str = None
    nombre_contacto: str = None
    telefono: str = None
    direccion:str = 'null'
    correo: str = None


    def __str__(self):
        return self.nombre


    def __init__(self, nombre, nit) -> None:
        self.nombre = nombre
        self.nit = nit


    def create(self, cursor, conn):
        query = f"""
            INSERT INTO Clientes (nombre, nit, contacto, telefono, direccion, correo)
            VALUES {self.nombre, self.nit, self.nombre_contacto, self.telefono, self.direccion, self.correo}
        """

        print(query)

        cursor.execute(query)
        _id = cursor.lastrowid
        conn.commit()

        return _id
        

    def list(self):
        pass

    def retrieve(self, pk):
        pass

    def delete(self, pk):
        pass