from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Camion(Vehiculo): # Define la subclase Camion que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_carga: int): # Constructor que recibe patente, anio y capacidad de carga
        super().__init__(patente, anio) # Llama al constructor de la clase base (Vehiculo) para inicializar patente y anio
        self.__capacidad_carga: int = capacidad_carga  # Asigna la capacidad de carga en kilos a un atributo privado
