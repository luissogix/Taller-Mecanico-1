# ==========================================
# CÓDIGO DEL REPOSITORIO TALLER MECÁNICO
# ==========================================

# --- Definición de la Clase Vehiculo (vehiculo.py) ---
class Vehiculo: # Define la clase Vehiculo
    def __init__(self, patente: str, anio: int): # Constructor que recibe patente y año al crear el objeto
        self.__patente: str = patente # Asigna la patente recibida a un atributo privado
        self.__anio: int = anio # Asigna el año recibido a un atributo privado
        self.__en_taller: bool = False # Inicializa el estado en False (no está en el taller por defecto) como privado

    def ingresar(self) -> str: # Método para registrar el ingreso del vehículo al taller
        if self.__en_taller: # Verifica si el vehículo ya está marcado como dentro del taller
            return "El vehículo ya se encuentra en el taller." # Devuelve mensaje si ya estaba ingresado
        self.__en_taller = True # Cambia el estado a True (ingresado)
        return "El vehículo ha ingresado al taller." # Devuelve mensaje de éxito

    def entregar(self) -> str: # Método para registrar la salida o entrega del vehículo
        if not self.__en_taller: # Verifica si el vehículo no está en el taller
            return "El vehículo no se encuentra en el taller." # Devuelve mensaje indicando que no se puede entregar
        self.__en_taller = False # Cambia el estado a False (fuera del taller)
        return "El vehículo ha sido entregado." # Devuelve mensaje de éxito

    def tarifa_hora(self) -> int: # Método que retorna el costo de la tarifa por hora
        return 5000 # Retorna un valor fijo de 5000


# --- Ejecución Principal (main.py) ---
if __name__ == "__main__":
    vehiculo1 = Vehiculo("AB1234", 2018) # Instancia el primer objeto Vehiculo pasándole su patente y año
    vehiculo2 = Vehiculo("CD5678", 2020) # Instancia el segundo objeto Vehiculo pasándole su patente y año
    vehiculo3 = Vehiculo("EF9012", 2023) # Instancia el tercer objeto Vehiculo pasándole su patente y año

    print(vehiculo1.ingresar()) # Ejecuta ingresar() del primer vehículo y muestra el texto retornado en consola
    print(vehiculo2.ingresar()) # Ejecuta ingresar() del segundo vehículo y muestra el texto retornado en consola
    print(vehiculo3.ingresar()) # Ejecuta ingresar() del tercer vehículo y muestra el texto retornado en consola

    print(f"Tarifa por hora del primer vehículo: ") # Concatena e imprime la tarifa retornada por el primer vehículo
    print(f"Tarifa por hora del segundo vehículo: ") # Concatena e imprime la tarifa retornada por el segundo vehículo
    print(f"Tarifa por hora del tercer vehículo: ") # Concatena e imprime la tarifa retornada por el tercer vehículo
