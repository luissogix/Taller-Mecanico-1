from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Auto(Vehiculo): # Define la subclase Auto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_maletero: int): # Constructor que recibe patente, anio y capacidad del maletero
        super().__init__(patente, anio) # Llama al constructor de la clase base (Vehiculo) para inicializar patente y anio
        self.capacidad_maletero: int = capacidad_maletero # Asigna mediante el setter para ejecutar la validación

    @property
    def capacidad_maletero(self) -> int: # Getter para acceder a la capacidad del maletero
        return self.__capacidad_maletero # Retorna el atributo privado __capacidad_maletero

    @capacidad_maletero.setter
    def capacidad_maletero(self, valor: int) -> None: # Setter para validar y asignar la capacidad del maletero
        if not isinstance(valor, int) or valor <= 0: # Valida que sea un entero positivo mayor a 0
            raise ValueError("La capacidad del maletero debe ser un número entero positivo mayor a 0.")
        self.__capacidad_maletero: int = valor # Asigna el valor validado al atributo privado

    def tarifa_hora(self) -> int: # Método que retorna la tarifa por hora específica para Auto
        return 25000 # Retorna 25000 como número entero
