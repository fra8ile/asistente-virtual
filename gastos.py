gastos = []

def agregar_gasto():
    nombre = input("Nombre del gasto: ")
    categoria = input("Categoría (comida/transporte/ocio/otro): ")
    cantidad = float(input("Cantidad: $"))
    gastos.append(("Nombre: " + nombre, "Categoría: " + categoria, "Cantidad: " + str(cantidad)))
    print("Gasto agregado exitosamente.")

def total_por_categoria():
    categorias = {}
    for gasto in gastos:
        nombre, categoria, cantidad = gasto
        if categoria in categorias:
            categorias[categoria] += float(cantidad)
        else:
            categorias[categoria] = float(cantidad)
    return categorias

def total_mes():
    total = 0
    for gasto in gastos:
        nombre, categoria, cantidad = gasto
        total += float(cantidad)
    return total

def gasto_mas_alto():
    if not gastos:
        print("No hay gastos registrados.")
        return None
    gasto_mas_alto = max(gastos, key=lambda x: float(x[2]))
    return gasto_mas_alto

def modulo_gastos():
	while True:
		print("\n=== MÓDULO GASTOS ===")
        print("1. Agregar gasto")
        print("2. Total por categoría")
        print("3. Total del mes")
        print("4. Gasto más alto")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_gasto()
        elif opcion == "2":
            total_por_categoria()
        elif opcion == "3":
            total_mes()
        elif opcion == "4":
            gasto_mas_alto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")