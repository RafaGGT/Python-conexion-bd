import dbconect as db
class Menu:
 def mostrar_menu(self):
       print("-"*10, " Menu ","-"*10)
       print("Seleccione una opcion:")
       print("1) Ingresar producto")
       print("2) Listar productos")
       print("3) Eliminar producto")
       print("0) Salir")
       opcion = input("Opcion: ")
       if opcion == "1":
              self.ingresar_producto()
              self.mostrar_menu()
       elif opcion == "2":
              self.listar_productos()
              self.mostrar_menu()
       elif opcion == "3":
              self.listar_productos()
              idProducto = int(input("ID del producto a eliminar: "))
              self.eliminar_producto(idProducto)
              self.mostrar_menu()
       elif opcion == "0":
              self.cerrar_conexion()
       else:
              print("Opcion incorrecta.")
              self.mostrar_menu()

 def ingresar_producto(self):
       nombre = input("Nombre del producto: ")
       nombre = nombre.capitalize().strip()
       tipo = input("Tipo: ")
       tipo = tipo.capitalize().strip()
       precio = float(input("Precio: "))
       precio = float(precio)
       peso = float(input("Peso: "))
       peso = float(peso)
       stock = int(input("Stock: "))
       stock = int(stock)

       consulta = ("INSERT INTO productos (nombre, tipo, precio, peso, stock) VALUES(%s, %s, %s, %s, %s)")
       # Verificamos si ya existe uno con ese nombre
       consulta_verificar = "SELECT COUNT(*) FROM productos WHERE nombre = %s"
       db.cursor.execute(consulta_verificar, [nombre])
       # Devuelve una dupla que en este caso si es 1 significa que ya existe, el []
       existe = db.cursor.fetchone()[0]
       if existe != 0:
              print("El nombre ya existe en la base de datos. Ingresa otro nombre.")
       else:
              db.cursor.execute(consulta, [nombre, tipo, precio, peso, stock])
              db.conexion.commit()
       
 def listar_productos(self):
       consulta = ("SELECT * FROM productos")
       db.cursor.execute(consulta)
       datos = db.cursor.fetchall()
       if datos == []:
              print("No hay productos en la base de datos.")
       else:
              print("-"*5, " Productos ","-"*5)
              for (idProducto, nombre, tipo, precio, peso, stock) in datos:
                     print(f" {idProducto}) {nombre.capitalize()}: ${precio}")
              print("-"*25)

 def eliminar_producto(self, idProducto):
       consulta = ("DELETE FROM productos WHERE idProducto = %s")
       db.cursor.execute(consulta, [idProducto])
       db.conexion.commit()
       print("Producto eliminado.")

 def cerrar_conexion(self):
       db.cursor.close()
       db.conexion.close()
       print("Cerrando conexion...")