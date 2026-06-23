import os

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo (Windows:'cls' o Unix:'clear')."""
    os.system("cls" if os.name == "nt" else "clear")


def pedir_input(mensaje):
    """Solicita un dato al usuario con formato visual y limpia la pantalla al confirmar.
    Args:
        mensaje (str): Texto a mostrar antes del input.
    Returns:
        str: Valor ingresado por el usuario.
    """
    entrada=input(f"\033[96m  ➜  {mensaje}\033[0m ")
    limpiar_pantalla()
    return entrada

def menu_inicio(materias, recordatorios):
    """""
    muestra el menu principal del asistente, 
    lista de materias y recordatorios.
    """""

    print("\033[96m")
    print("╔══════════════════════════════════════════════╗")
    print("║       ¡Hola! Soy tu asistente virtual.       ║")
    print("╠══════════════════════════════════════════════╣")
    
    #seccion de materias y recordatorios
    print("║ Materias:                                    ║")
    for i in range(len(materias)):
        print(f"║  {i + 1}. {materias[i]}")

    print("╠══════════════════════════════════════════════╣")

    print("║ Recordatorios:                               ║")
    for i in range(len(recordatorios)):
        print(f"║  {i + 1}. {recordatorios[i]}")
#opciones principales del asistente
    print("╠══════════════════════════════════════════════╣")
    print("║              1 - Menu escolar                ║")
    print("║              2 - Recordatorios               ║")
    print("║              3 - Controlar gastos            ║")
    print("╠══════════════════════════════════════════════╣")
    print("║              0 - Regresar                    ║")
    print("╚══════════════════════════════════════════════╝")
    print("\033[0m")

def menu_estudiante():
        """
        Menú del módulo académico (estudiante).
        Permite gestionar materias, notas, exámenes y horas de estudio.
        """
        print("\033[96m")
        print("╔══════════════════════════════════════════════╗")
        print("║              MÓDULO ESTUDIANTE               ║")
        print("╠══════════════════════════════════════════════╣")
        print("║              1 - Agregar Materias            ║")
        print("║              2 - Registrar Notas             ║")
        print("║              3 - Ver Notas                   ║")
        print("║              4 - Registrar examen            ║")
        print("║              5 - Ver exámenes                ║")
        print("║              6 - Registrar horas de estudio  ║")
        print("║              7 - Ver horas de estudio        ║")
        print("║              8 - Ver boletín académico       ║")
        print("╠══════════════════════════════════════════════╣")
        print("║              9 - Volver al menú principal    ║")
        print("╚══════════════════════════════════════════════╝")
        print("\033[0m")

def menu_recordatorio():
        """Menú del módulo de recordatorios."""
        
        print("\033[96m")
        print("╔══════════════════════════════════════════════╗")
        print("║              MÓDULO RECORDATORIOS            ║")            
        print("╠══════════════════════════════════════════════╣")
        print("║              1 - Agregar Recordatorio        ║")
        print("║              2 - Ver Recordatorios           ║")
        print("║              3 - Modificar Recordatorio      ║")
        print("║              4 - Buscar Recordatorio         ║")
        print("║              5 - Eliminar Recordatorio       ║")
        print("╠══════════════════════════════════════════════╣")
        print("║              0 - Volver al menú principal    ║")
        print("╚══════════════════════════════════════════════╝")
        print("\033[0m")