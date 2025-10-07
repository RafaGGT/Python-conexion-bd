import mysql.connector
import time

conexion = mysql.connector.connect(
                                    host = "localhost",
                                    database= "product",
                                    user= "root",
                                    password = "root",
                                    port = 3306
                                    )

print("Cargando")
# Y podrias hacer una animacion de carga en una sola linea
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print("\nConexion exitosa.")
cursor = conexion.cursor()



