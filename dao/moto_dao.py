from dao.vehiculo_dao import VehiculoDao


class MotoDao(VehiculoDao):
    """
    Data Access Object para la entidad Moto.
    Hereda de VehiculoDao aplicando herencia de tablas (Joined Table Inheritance).
    """

    def crear_tabla(self):
        """
        Crea la tabla 'motos' en la base de datos si no existe.
        Invoca primero a super().crear_tabla() para asegurar que la tabla 'vehiculos' exista.
        La tabla contiene:
        - patente: TEXT PRIMARY KEY (y Foreign Key hacia vehiculos.patente)
        """
        super().crear_tabla()

        sql = """
        CREATE TABLE IF NOT EXISTS motos (
            patente TEXT PRIMARY KEY,
            FOREIGN KEY (patente) REFERENCES vehiculos (patente)
        )
        """
        self.cursor.execute(sql)
        self.conexion.commit()
