# Lista donde se guardarán los productos
# VALIDAR NOMBRE
# VALIDAR PRECIO
# VALIDAR CANTIDAD
# CREAR PRODUCTO
# CALCULAR TOTAL
inventario = []


def agregar_producto():
    print("\n--- Agregar producto ---")


    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre == '':
            print("Error: el nombre no puede estar vacío.")
        elif nombre.isnumeric():
            print("Error: el nombre no puede ser solo números.")
        else:
            break


    while True:
        precio_ingresado = input("Precio: ").strip()
        if precio_ingresado == '':
            print("Error: el precio no puede estar vacío.")
        elif ' ' in precio_ingresado:
            print("Error: el precio no puede contener espacios.")
        elif not precio_ingresado.replace('.', '', 1).isnumeric():
            print("Error: ingrese un número válido.")
        else:
            precio = float(precio_ingresado)
            if precio < 0:
                print("Error: el precio no puede ser negativo.")
            else:
                break

    
    while True:
        cantidad_ingresada = input("Cantidad: ").strip()
        if cantidad_ingresada == '':
            print("Error: la cantidad no puede estar vacía.")
        elif not cantidad_ingresada.isnumeric():
            print("Error: debe ser un número entero.")
        elif int(cantidad_ingresada) <= 0:
            print("Error: debe ser mayor a cero.")
        else:
            cantidad = int(cantidad_ingresada)
            break

    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    
    costo_total = precio * cantidad

    print("\n" + "=" * 40)
    print(f"Producto: {nombre} | Precio: {precio:.0f} | Cantidad: {cantidad} | Total: {costo_total:.0f}")
    print("=" * 40)
    print(" Producto registrado correctamente.")


def mostrar_inventario():
    print("\n--- Inventario ---")

    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


def calcular_estadisticas():
    print("\n--- Estadísticas ---")

    if len(inventario) == 0:
        print("No hay productos para calcular.")
        return

    total_valor = 0
    total_productos = 0

    for producto in inventario:
        total_valor += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print(f"Valor total del inventario: {total_valor:.0f}")
    print(f"Cantidad total de productos: {total_productos}")


# ================= MENÚ PRINCIPAL =================

def menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print(" Opción inválida, intenta de nuevo.")


#Inicio del programa
print("Sistema de Registro de Inventario")
menu()