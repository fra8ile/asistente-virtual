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
    print("║                        MATERIAS                      ║")
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


def menu_inicio(materias,recordatorios,gastos):
        print("\033[32m")  # Blanco brillante sobre negro
        print("╔══════════════════════════════════════════════════════╗")
        print("║                    ASISTENTE PERSONAL                ║")
        print("╠══════════════════════════════════════════════════════╣")
        
        print(f"║   Materias registradas: {len(materias):<29}║")
        print(f"║   Recordatorios pendientes: {len(recordatorios):<25}║")

        ver_materias(materias)
        
        print("╠══════════════════════════════════════════════════════╣")
        print("║  Próximos recordatorios:                             ║")

        for recordatorio in recordatorios[:3]:
            texto = f"• {recordatorio}"
            print(f"║ {texto[:52].ljust(52)} ║")

        if len(recordatorios) == 0:
            print("\033[32m║\033[0m"+"\033[31m  Sin recordatorios pendientes                        \033[0m"+"\033[32m║\033[0m")
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

def menu_gastos():
        print("\033[32m")
        print("╔══════════════════════════════════════════════════════╗")
        print("║                Modulo Gastos                         ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                [1] - Agregar gasto                   ║")
        print("║                [2] - Total por categoría             ║")
        print("║                [3] - Total del mes                   ║")
        print("║                [4] - Gasto más alto                  ║")
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

def menu_recordatorio():
        print("\033[32m")
        print("╔══════════════════════════════════════════════════════╗")
        print("║                Modulo Recordatorios                  ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                [1] - Agregar Recordatorio            ║")
        print("║                [2] - Ver Recordatorios               ║")
        print("║                [3] - Modificar Recordatorio          ║")
        print("║                [4] - Buscar Recordatorio             ║")
        print("║                [5] - Eliminar Recordatorio           ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                [0] - Regresar                        ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("\033[0m")

def mensaje_error(mensa):
    print("\033[31m")
    print("════════════════════════════════════════════════════════")
    print( ' ➜  ' + mensa)
    print("════════════════════════════════════════════════════════\033[0m", end="")
    