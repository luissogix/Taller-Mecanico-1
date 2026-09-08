from abc import ABC, abstractmethod


class Vehiculo(ABC): # Define la clase Vehiculo como una clase abstracta
    def __init__(self, patente: str, anio: int): # Constructor que recibe patente y año al crear el objeto
        self.patente: str = patente # Asigna mediante el setter de la propiedad para ejecutar la validación
        self.__anio: int = anio # Asigna el año recibido a un atributo privado
        self.__en_taller: bool = False # Inicializa el estado en False (no está en el taller por defecto) como privado

    @property
    def patente(self) -> str: # Getter para acceder al valor de la patente
        return self.__patente # Retorna el valor del atributo privado __patente

    @patente.setter
    def patente(self, valor: str) -> None: # Setter para validar y asignar la patente
        if not isinstance(valor, str) or len(valor) < 6 or " " in valor: # Valida que tenga al menos 6 caracteres y sin espacios
            raise ValueError("La patente debe tener al menos 6 caracteres y no contener espacios.") # Lanza error si no cumple
        self.__patente: str = valor # Asigna el valor validado al atributo privado __patente

    def get_patente(self) -> str: # Método getter tradicional
        return self.patente # Retorna la patente

    def set_patente(self, valor: str) -> None: # Método setter tradicional
        self.patente = valor # Asigna y valida la patente

    def ingresar(self) -> str: # Método para registrar el ingreso del vehículo al taller sin usar if
        mensajes = { # Diccionario de mapeo de estados para evitar condicionales if
            True: "El vehículo ya se encuentra en el taller.",
            False: "El vehículo ha ingresado al taller."
        }
        mensaje = mensajes[self.__en_taller] # Obtiene el mensaje según el estado actual
        self.__en_taller = True # Actualiza el estado a True (ingresado)
        return mensaje # Retorna el mensaje correspondiente

    def entregar(self) -> str: # Método para registrar la salida o entrega del vehículo sin usar if
        mensajes = { # Diccionario de mapeo de estados para evitar condicionales if
            False: "El vehículo no se encuentra en el taller.",
            True: "El vehículo ha sido entregado."
        }
        mensaje = mensajes[self.__en_taller] # Obtiene el mensaje según el estado actual
        self.__en_taller = False # Actualiza el estado a False (fuera del taller)
        return mensaje # Retorna el mensaje correspondiente

    @abstractmethod
    def tarifa_hora(self) -> int: # Método abstracto para que cada subclase defina su tarifa por hora
        pass