from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Auto(Vehiculo): # Define la subclase Auto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_maletero: int): # Constructor que recibe patente, anio y capacidad del maletero
        super().__init__(patente, anio) # Llama al constructor de la clase base (Vehiculo) para inicializar patente y anio
        self.__capacidad_maletero: int = capacidad_maletero # Asigna la capacidad del maletero en litros a un atributo privado
