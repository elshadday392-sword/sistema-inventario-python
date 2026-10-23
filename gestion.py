class SistemaInventario:
    def __init__(self):
        self.inventario = {}
    def agregar_producto(self, nombre, precio, stock):
        self.inventario[nombre] = [precio, stock]
    def guardar_datos(self):
        with open("inventario.txt", "w") as archivo:
            for nombre, datos in self.inventario.items():
                linea = f"{nombre},{datos[0]},{datos[1]}\n"
                archivo.write(linea)
    def cargar_datos(self):
        try:
            with open("inventario.txt", "r") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        partes = linea.split(",")
                        nombre = partes[0]
                        precio = int(partes[1])
                        stock = int(partes[2])
                        self.inventario[nombre] = [precio, stock]
        except FileNotFoundError:
            print("No se encontró archivo previo, iniciando inventario vacío.")
    def vender_producto(self, nombre, cantidad):  # ← PARÁMETROS AGREGADOS
        try:
            cantidad = int(cantidad)
            if nombre not in self.inventario:
                print("Producto no encontrado.")
                return
            precio, stock_actual = self.inventario[nombre]
            if cantidad > stock_actual:
                print(f"Stock insuficiente. Disponible: {stock_actual}")
            else:
                self.inventario[nombre][1] -= cantidad
                total = precio * cantidad
                nuevo_stock = self.inventario[nombre][1]
                print(f"Venta exitosa. Total: ${total}. Stock restante: {nuevo_stock}")
        except ValueError:
            print("Error: la cantidad debe ser un número válido.")
    def eliminar_producto(self, nombre):
        if nombre not in self.inventario:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")
            return False
        datos_eliminados = self.inventario.pop(nombre)
        print(f"Producto '{nombre}' eliminado exitosamente. (Precio: ${datos_eliminados[0]}, Stock restante: {datos_eliminados[1]})")
        return True

# FLUJO PRINCIPAL CORREGIDO
tienda = SistemaInventario()
tienda.cargar_datos()

while True:
    print("\n=== SISTEMA DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver inventario")
    print("4. Eliminar producto")
    print("5. Guardar y Salir")
    print("=============================")
    
    try:
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            # Pedir datos y agregar
            nombre = input("Producto: ")
            precio = int(input("Precio: $"))
            stock = int(input("Cantidad: "))
            tienda.agregar_producto(nombre, precio, stock)
            tienda.guardar_datos()
        elif opcion == "2":
            # Pedir datos y vender
            print("\n--- Venta ---")
            nombre_venta = input("Producto a vender: ")
            cantidad_venta = input("Cantidad: ")
            tienda.vender_producto(nombre_venta, cantidad_venta)
            tienda.guardar_datos()
        elif opcion == "3":
            print("\n--- Inventario Actual ---")
            if not tienda.inventario:
                print("El inventario está vacío.")
            else:
                for nombre, datos in tienda.inventario.items():
                    print(f"Producto: {nombre} | Precio: ${datos[0]} | Stock: {datos[1]}")          
        elif opcion == "4":  # ← NUEVA OPCIÓN: Eliminar producto
            print("\n--- Eliminar Producto ---")
            nombre_eliminar = input("Nombre del producto a eliminar: ")
            tienda.eliminar_producto(nombre_eliminar)
            tienda.guardar_datos()  # Guardar automáticamente tras eliminar            
        elif opcion == "5":
            tienda.guardar_datos()
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
            
    except ValueError:
        print("Error: Ingresa un número válido.")

