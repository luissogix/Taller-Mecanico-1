# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel
**Institución:** Inacap

---

## Bitácora de Avances

### 31 de Agosto de 2026
- **Creación de Subclases:**
  - Se crearon los archivos uto.py, moto.py y camion.py, implementando herencia desde la clase base Vehiculo.
- **Especialización de Clases:**
  - **Camion (camion.py):** Se implementó constructor propio llamando a super().__init__() y se definió el atributo privado __capacidad_carga (en kilos).
  - **Auto (uto.py):** Se implementó constructor propio llamando a super().__init__() y se definió el atributo privado __capacidad_maletero (en litros).
  - **Moto (moto.py):** Hereda directamente de Vehiculo.
- **Actualización de Script Principal (main.py):**
  - Se actualizaron las importaciones e instanciaciones para utilizar las subclases Auto, Moto y Camion con sus respectivos parámetros requeridos.
- **Documentación:** Se comentaron todas las nuevas líneas de código explicando el uso de herencia y constructores.

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (gh auth).
- **Limpieza:** Se eliminó la versión antigua del archivo ehiculo.py para construir el proyecto desde cero.
- **Clase Vehiculo (ehiculo.py):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados __patente, __anio y __en_taller en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos ingresar() y entregar() con validación de estado.
  - Se creó el método 	arifa_hora() que retorna un valor fijo de 5000.
- **Script de Pruebas (main.py):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase Vehiculo y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (ehiculo.py y main.py) explicando paso a paso su funcionamiento con fines educativos.
