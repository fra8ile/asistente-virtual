from interfaz import pedir_input,limpiar_pantalla,menu_gastos


def agregar_gasto(gastos):
    nombre = pedir_input("Nombre del gasto: ")
    categoria = pedir_input("Categoría (comida/transporte/ocio/otro): ")
    cantidad = float(pedir_input("Cantidad: $"))
    gastos.append((nombre, categoria, cantidad))
    print("Gasto agregado exitosamente.")

def total_por_categoria(gastos):
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

def total_mes(gastos):
    total = 0
    for gasto in gastos:
        nombre, categoria, cantidad = gasto
        total += cantidad
    print("\nTotal del mes: $" + str(total))

def gasto_mas_alto(gastos):
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

def modulo_gastos(gastos,ingresos):
    continuar=True
    while continuar:
        limpiar_pantalla()
        menu_gastos(gastos,ingresos)

        opcion = int(pedir_input("Seleccione una opción: "))

        if opcion < 0 or opcion > 4:
            print("Opción no válida. Por favor, intente nuevamente.")
        else:
            if opcion == 1:
                ingresos.append(pedir_input("Ingrese el ingreso: "))
            if opcion == 2:
                agregar_gasto(gastos)
            elif opcion == 3:
                total_por_categoria(gastos)
            elif opcion == 4:
                total_mes(gastos)
            elif opcion == 5:
                gasto_mas_alto(gastos)
            else:
                continuar=False