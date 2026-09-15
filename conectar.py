import sqlite3
from marca import Marca
from modelo import Modelo   
from auto import Auto




conexion=sqlite3.connect("basededatos.db")

cursor=conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculos (
                patente TEXT PRIMARY KEY,
                modelo TEXT,
                en_taller INTEGER)""")
marca_toyota = Marca("Toyota")
modelo = Modelo("Yaris", marca_toyota)





auto=Auto("ABC123", 2020, modelo)

##cursor.execute("INSERT OR REPLACE INTO vehiculos (patente, modelo, en_taller) VALUES (?,?,?)",
####                (auto.patente, auto.modelo.nombre,int(auto._en_taller)))


cursor.execute("SELECT * FROM vehiculos WHERE patente=?", ("ABC123",))
fila=cursor.fetchone()
print(fila)

conexion.commit()




