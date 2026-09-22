from conectar import crear_conexion  # Importa la función para crear la conexión a la BD
from dao.marca_dao import MarcaDao  # Importa el DAO de marcas
from dao.modelo_dao import ModeloDao  # Importa el DAO de modelos
from dao.auto_dao import AutoDao  # Importa el DAO de autos (que también gestiona vehículos)
from dao.moto_dao import MotoDao  # Importa el DAO de motos
from dao.camion_dao import CamionDao  # Importa el DAO de camiones


def main():  # Función principal de ejecución
    print("--- Inicializando Base de Datos ---")  # Mensaje de inicio

    # 1. Crear la conexión
    conexion = crear_conexion()  # Llama a crear_conexion para obtener el objeto de conexión

    # 2. Instanciar los DAOs pasándoles la conexión
    marca_dao = MarcaDao(conexion)  # Instancia MarcaDao entregando la conexión
    modelo_dao = ModeloDao(conexion)  # Instancia ModeloDao entregando la conexión
    auto_dao = AutoDao(conexion)  # Instancia AutoDao entregando la conexión
    moto_dao = MotoDao(conexion)  # Instancia MotoDao entregando la conexión
    camion_dao = CamionDao(conexion)  # Instancia CamionDao entregando la conexión

    # 3. Crear las tablas en orden de dependencias
    print("Creando tablas...")  # Mensaje informativo
    marca_dao.crear_tabla()      # Crea tabla 'marcas'
    modelo_dao.crear_tabla()     # Crea tabla 'modelos' (FK a marcas)
    auto_dao.crear_tabla()       # Crea tablas 'vehiculos' (FK a modelos) y 'autos' (FK a vehiculos)
    moto_dao.crear_tabla()       # Crea tabla 'motos' (FK a vehiculos)
    camion_dao.crear_tabla()     # Crea tabla 'camiones' (FK a vehiculos)

    # 4. Validar que las tablas existan en la BD
    cursor = conexion.cursor()  # Obtiene un cursor para una consulta general
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")  # Consulta los nombres de las tablas
    tablas_creadas = [fila[0] for fila in cursor.fetchall()]  # Extrae los nombres en una lista

    print("\n--- Tablas encontradas en la Base de Datos ---")  # Mensaje informativo
    for tabla in tablas_creadas:  # Itera sobre la lista de tablas encontradas
        if tabla != "sqlite_sequence":  # Ignora 'sqlite_sequence' que es una tabla del sistema
            print(f"- {tabla}")  # Imprime el nombre de cada tabla

    print("\nProceso finalizado exitosamente.")  # Mensaje final de éxito

    # 5. Cerrar la conexión
    conexion.close()  # Cierra la conexión a la base de datos


if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    main()  # Llama a la función principal
