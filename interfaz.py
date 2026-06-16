import os

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo (Windows o Unix)."""
    os.system("cls" if os.name == "nt" else "clear")

def pedir_input(mensaje):
    """Solicita un dato al usuario con formato visual y limpia la pantalla al confirmar.
    Args:
        mensaje (str): Texto a mostrar antes del input.
    Returns:
        str: Valor ingresado por el usuario.
    """
    entrada = input(f"\033[32m  ➜  {mensaje} ")
    print("\033[0m")
    limpiar_pantalla()
    return entrada

def promedio_materia(notas):

    if len(notas) == 0:
        return 0

    return sum(notas) / len(notas)

def ver_materias(materias):

    print("\033[32m╠══════════════════════════════════════════════════════╣")
    print("║                    \033[1;4mMATERIAS\033[0m  \033[32m                        ║")
    print("╠══════════════════════════════════════════════════════╣")

    if len(materias) == 0:

        print("║             Sin materias registradas                 ║")

    else:

        for materia, notas in materias:

            promedio = promedio_materia(notas)

            texto = f"• {materia}"

            print(f"║ {texto[:52].ljust(52)} ║")

            texto_notas = f"  Notas: {notas}"

            print(f"║ {texto_notas[:52].ljust(52)} ║")

            texto_prom = f"  Promedio: {promedio:.2f}"

            print(f"║ {texto_prom[:52].ljust(52)} ║")

            print("║                                                      ║")
    if len(materias) > 0:

        suma = 0

        for materia, notas in materias:

            suma += promedio_materia(notas)

        promedio_general = suma / len(materias)

        print("╠══════════════════════════════════════════════════════╣")

        texto = f"PROMEDIO GENERAL: {promedio_general:.2f}"

        print(f"║ {texto.center(52)} ║")


def menu_inicio(materias,recordatorios,gastos,ingresos):
        print("\033[32m")  # Blanco brillante sobre negro
        print("╔══════════════════════════════════════════════════════╗")
        print("║                    \033[1;4mASISTENTE PERSONAL\033[0m \033[32m               ║")
        print("╠══════════════════════════════════════════════════════╣")
        
        print(f"║   Materias registradas: {len(materias):<29}║")
        print(f"║   Recordatorios pendientes: {len(recordatorios):<25}║")

        ver_materias(materias)
        
        print("╠══════════════════════════════════════════════════════╣")
        print("║                    \033[1;4mRECORDATORIOS\033[0m  \033[32m                   ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║  Próximos recordatorios:                             ║")

        for recordatorio in recordatorios[:3]:
            texto = f"• {recordatorio}"
            print(f"║ {texto[:52].ljust(52)} ║")                      
        print("╠══════════════════════════════════════════════════════╣")
        print("║                    \033[1;4mBILLETERA\033[0m          \033[32m               ║")
        print("╠══════════════════════════════════════════════════════╣")

        if len(gastos) == 0:
            print("║              Sin gastos registrados                  ║")
        else:
            for gasto in gastos[-3:]:
                nombre, categoria, cantidad = gasto
                texto = f"• {nombre} | {categoria} | ${cantidad}"
                print(f"║ {texto[:52].ljust(52)} ║")
        print("╠══════════════════════════════════════════════════════╣")
        if len(ingresos) == 0:
            print("║              Sin ingresos registrados                ║")
        else:
            for ingreso in ingresos[-3:]:
                texto = f"• ${ingreso}"
                print(f"║ {texto[:52].ljust(52)} ║")
        print("\033[32m╠══════════════════════════════════════════════════════╣")
        print("║                                                      ║")
        print("║                [1]  Módulo Escolar                   ║")
        print("║                [2]  Recordatorios                    ║")
        print("║                [3]  Control de Gastos                ║")
        print("║                                                      ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                [0]  Salir                            ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("\033[0m")

def menu_gastos(gastos,ingresos):
        print("\033[32m")
        print("╔══════════════════════════════════════════════════════╗")
        print("║                Modulo Gastos                         ║")
        print("╠══════════════════════════════════════════════════════╣")
        if len(gastos) == 0:
            print("║              Sin gastos registrados                  ║")
        else:
            for gasto in gastos[-3:]:
                nombre, categoria, cantidad = gasto
                texto = f"• {nombre} | {categoria} | ${cantidad}"
                print(f"║ {texto[:52].ljust(52)} ║")
        print("╠══════════════════════════════════════════════════════╣")
        if len(ingresos) == 0:
            print("║              Sin ingresos registrados                ║")
        else:
            for ingreso in ingresos[-3:]:
                texto = f"• ${ingreso}"
                print(f"║ {texto[:52].ljust(52)} ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                [1] - Agregar ingresos                ║")
        print("║                [2] - Agregar gasto                   ║")
        print("║                [3] - Total por categoría             ║")
        print("║                [4] - Total del mes                   ║")
        print("║                [5] - Gasto más alto                  ║")
        print("╠══════════════════════════════════════════════════════╠")
        print("║                [0] - Regresar                        ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("\033[0m")

def menu_estudiante(materias):
        print("\033[32m")
        print("╔══════════════════════════════════════════════════════╗")
        print("║                Modulo Estudiante                     ║")
        ver_materias(materias)
        print("\033[32m╠══════════════════════════════════════════════════════╣")
        print("║                [1] - Agregar Materias                ║")
        print("║                [2] - Registrar Notas                 ║")
        print("║                [3] - Registrar horas de estudio      ║")
        print("║                [4] - Ver horas de estudio            ║")
        print("║                [5] - Ver boletín académico           ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                [0] - Regresar                        ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("\033[0m")
def ver_recordatorios(recordatorios, limite=None):

    print("╠══════════════════════════════════════════════════════╣")
    print("║                    RECORDATORIOS                     ║")
    print("╠══════════════════════════════════════════════════════╣")

    if len(recordatorios) == 0:

        print("║          Sin recordatorios pendientes                ║")

    else:

        lista = recordatorios

        cantidad = len(recordatorios)

        if limite is not None and limite < cantidad:
            cantidad = limite
        for i in range(cantidad):

            texto = f"• {lista[i][0]}"
            print(f"║ {texto[:52].ljust(52)} ║")

            texto_fecha = f"  Fecha: {lista[i][2]} - Hora: {lista[i][1]}"
            print(f"║ {texto_fecha[:52].ljust(52)} ║")

            print("║                                                      ║")
def menu_recordatorio(recordatorios):
        print("\033[32m")
        print("╔══════════════════════════════════════════════════════╗")
        print("║                Modulo Recordatorios                  ║")
        ver_recordatorios(recordatorios, 3)
        print("╠══════════════════════════════════════════════════════╣")
        print("║                [1] - Agregar Recordatorio            ║")
        print("║                [2] - Modificar Recordatorio          ║")
        print("║                [3] - Buscar Recordatorio             ║")
        print("║                [4] - Eliminar Recordatorio           ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                [0] - Regresar                        ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("\033[0m")

def mensaje_error(mensa):
    print("\033[31m")
    print("════════════════════════════════════════════════════════")
    print( ' ➜  ' + mensa)
    print("════════════════════════════════════════════════════════\033[0m")
    