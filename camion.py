from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Camion(Vehiculo): # Define la subclase Camion que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_carga: int): # Constructor que recibe patente, anio y capacidad de carga
        super().__init__(patente, anio) # Llama al constructor de la clase base (Vehiculo) para inicializar patente y anio
        self.capacidad_carga: int = capacidad_carga # Asigna mediante el setter para ejecutar la validación

    @property
    def capacidad_carga(self) -> int: # Getter para acceder a la capacidad de carga
        return self.__capacidad_carga # Retorna el atributo privado __capacidad_carga

    @capacidad_carga.setter
    def capacidad_carga(self, valor: int) -> None: # Setter para validar y asignar la capacidad de carga
        if not isinstance(valor, int) or valor <= 0: # Valida que sea un entero positivo mayor a 0
            raise ValueError("La capacidad de carga debe ser un número entero positivo mayor a 0.")
        self.__capacidad_carga: int = valor # Asigna el valor validado al atributo privado

    def tarifa_hora(self) -> int: # Método que retorna la tarifa por hora específica para Camion
        return 40000 # Retorna 40000 como número entero
