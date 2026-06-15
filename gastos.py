from interfaz import pedir_input,limpiar_pantalla

gastos = []

def agregar_gasto():
    nombre = input("Nombre del gasto: ")
    categoria = input("Categoría (comida/transporte/ocio/otro): ")
    cantidad = float(input("Cantidad: $"))
    gastos.append((nombre, categoria, cantidad))
    print("Gasto agregado exitosamente.")

def total_por_categoria():
    categorias = []
    nombres_cat = []

    for gasto in gastos:
        nombre, categoria, cantidad = gasto
        encontrado = False
        for i in range(len(nombres_cat)):
            if nombres_cat[i] == categoria:
                categorias[i] += cantidad
                encontrado = True
                break
        if not encontrado:
            nombres_cat.append(categoria)
            categorias.append(cantidad)

    print("\n--- Total por categoría ---")
    for i in range(len(nombres_cat)):
        print(nombres_cat[i] + ": $" + str(categorias[i]))

def total_mes():
    total = 0
    for gasto in gastos:
        nombre, categoria, cantidad = gasto
        total += cantidad
    print("\nTotal del mes: $" + str(total))

def gasto_mas_alto():
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return
    mayor = gastos[0]
    for gasto in gastos:
        nombre, categoria, cantidad = gasto
        nombre_mayor, categoria_mayor, cantidad_mayor = mayor
        if cantidad > cantidad_mayor:
            mayor = gasto
    nombre_mayor, categoria_mayor, cantidad_mayor = mayor
    print("\nGasto más alto:")
    print("Nombre: " + nombre_mayor)
    print("Categoría: " + categoria_mayor)
    print("Cantidad: $" + str(cantidad_mayor))

def modulo_gastos():
    continuar=True
    while continuar:
        print("\n=== MÓDULO GASTOS ===")
        print("1. Agregar gasto")
        print("2. Total por categoría")
        print("3. Total del mes")
        print("4. Gasto más alto")
        print("0. Volver al menú principal")

        opcion = int(pedir_input("Seleccione una opción: "))

        if opcion == 1:
            agregar_gasto()
        elif opcion == 2:
            total_por_categoria()
        elif opcion == 3:
            total_mes()
        elif opcion == 4:
            gasto_mas_alto()
        elif opcion == 0:
            continuar=False
        else:
            print("Opción no válida. Por favor, intente nuevamente.")