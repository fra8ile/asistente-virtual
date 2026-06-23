from interfaz import pedir_input,limpiar_pantalla

gastos = []   # Lista global que almacena todos los gastos

def agregar_gasto():
    """
    Registra un gasto con nombre, categoría y monto.
    """
    nombre = input("Nombre del gasto: ")
    categoria = input("Categoría (comida/transporte/ocio/otro): ")
    cantidad = float(input("Cantidad: $"))
    gastos.append((nombre, categoria, cantidad))
    print("Gasto agregado exitosamente.")

def total_por_categoria():
    """
    calcula y muestra el total de gastos por categoría.
    """
    categorias = []
    nombres_cat = []

    for gasto in gastos:
        nombre, categoria, cantidad = gasto
        encontrado = False
        for i in range(len(nombres_cat)): #busca haber si la categoria existe
            if nombres_cat[i] == categoria:
                categorias[i] += cantidad
                encontrado = True
                break
        if not encontrado: # si no existe la categoria, esta la crea y agrega a la lista
            nombres_cat.append(categoria)
            categorias.append(cantidad)

    print("\n--- Total por categoría ---")
    for i in range(len(nombres_cat)):
        print(nombres_cat[i] + ": $" + str(categorias[i]))

def total_mes(): 
    '''
    suma todos los gastos registrados y muestr el total del mes
    '''
    total = 0
    for gasto in gastos:
        nombre, categoria, cantidad = gasto
        total += cantidad
    print("\nTotal del mes: $" + str(total))

def gasto_mas_alto():
    '''
    busca el gasto mas alto registrado y lo muestra
    '''
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
    '''
    Menu interactivo del módulo para gestionar los gastos.
    '''
    while True:
        print("\n=== MÓDULO GASTOS ===")
        print("1. Agregar gasto")
        print("2. Total por categoría")
        print("3. Total del mes")
        print("4. Gasto más alto")
        print("5. Volver al menú principal")

        opcion = int(pedir_input("Seleccione una opción: "))

        if opcion == 1:
            agregar_gasto()
        elif opcion == 2:
            total_por_categoria()
        elif opcion == 3:
            total_mes()
        elif opcion == 4:
            gasto_mas_alto()
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")