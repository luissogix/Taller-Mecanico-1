from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py
from auto import Auto # Importa la clase Auto desde auto.py
from moto import Moto # Importa la clase Moto desde moto.py
from camion import Camion # Importa la clase Camion desde camion.py

# Instanciación de objetos de las subclases (Vehiculo es abstracta)
vehiculo1 = Auto("AB1234", 2018, 100) # Instancia un objeto Auto con patente, año y capacidad de maletero
vehiculo2 = Moto("CD5678", 2020) # Instancia un objeto Moto con patente y año
vehiculo3 = Camion("EF9012", 2023, 5000) # Instancia un objeto Camion con patente, año y capacidad de carga

# Registro de ingreso al taller para cada vehículo
print(vehiculo1.ingresar()) # Ejecuta ingresar() del primer vehículo y muestra el mensaje en consola
print(vehiculo2.ingresar()) # Ejecuta ingresar() del segundo vehículo y muestra el mensaje en consola
print(vehiculo3.ingresar()) # Ejecuta ingresar() del tercer vehículo y muestra el mensaje en consola

# Demostración de encapsulamiento con la propiedad patente
pruebaEnc = vehiculo3.patente # Obtiene la patente a través del getter de la propiedad
print(f"Patente obtenida de vehiculo3: {pruebaEnc}") # Muestra la patente en consola

# Invocación y visualización de la tarifa por hora de cada vehículo
print(f"Tarifa por hora del primer vehículo (Auto): {vehiculo1.tarifa_hora()}") # Muestra la tarifa específica de Auto (25000)
print(f"Tarifa por hora del segundo vehículo (Moto): {vehiculo2.tarifa_hora()}") # Muestra la tarifa específica de Moto (15000)
print(f"Tarifa por hora del tercer vehículo (Camión): {vehiculo3.tarifa_hora()}") # Muestra la tarifa específica de Camion (40000)

