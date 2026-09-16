from conectar import crear_conexion
from dao.marca_dao import MarcaDao
from dao.modelo_dao import ModeloDao
from dao.auto_dao import AutoDao
from dao.moto_dao import MotoDao
from dao.camion_dao import CamionDao


def main():
    # 1. Crear la conexión
    conexion = crear_conexion()

    # 2. Instanciar los DAOs
    marca_dao = MarcaDao(conexion)
    modelo_dao = ModeloDao(conexion)
    auto_dao = AutoDao(conexion)
    moto_dao = MotoDao(conexion)
    camion_dao = CamionDao(conexion)

    # 3. Crear las tablas en orden de dependencias
    marca_dao.crear_tabla()      # Crea tabla 'marcas'
    modelo_dao.crear_tabla()     # Crea tabla 'modelos' (FK a marcas)
    auto_dao.crear_tabla()       # Crea tablas 'vehiculos' (FK a modelos) y 'autos' (FK a vehiculos)
    moto_dao.crear_tabla()       # Crea tabla 'motos' (FK a vehiculos)
    camion_dao.crear_tabla()     # Crea tabla 'camiones' (FK a vehiculos)

    print("Tablas creadas exitosamente: marcas, modelos, vehiculos, autos, motos, camiones.")

    # 4. Cerrar la conexión
    conexion.close()


if __name__ == "__main__":
    main()
