from auto import Auto
from moto import Moto
from camion import Camion

vehiculo1 = Auto("AB1234", 2018, 100) # Instancia el primer objeto Auto pasándole su patente y año
vehiculo2 = Moto("CD5678", 2020) # Instancia el segundo objeto Moto pasándole su patente y año
vehiculo3 = Camion("EF9012", 2023, 5000) # Instancia el tercer objeto Camion pasándole su patente y año

print(vehiculo1.ingresar()) # Ejecuta ingresar() del primer vehículo y muestra el texto retornado en consola
print(vehiculo2.ingresar()) # Ejecuta ingresar() del segundo vehículo y muestra el texto retornado en consola
print(vehiculo3.ingresar()) # Ejecuta ingresar() del tercer vehículo y muestra el texto retornado en consola

print(f"Tarifa por hora del primer vehículo: ") # Concatena e imprime la tarifa retornada por el primer vehículo
print(f"Tarifa por hora del segundo vehículo: ") # Concatena e imprime la tarifa retornada por el segundo vehículo
print(f"Tarifa por hora del tercer vehículo: ") # Concatena e imprime la tarifa retornada por el tercer vehículo
