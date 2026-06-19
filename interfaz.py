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
    entrada=input(f"\033[96m  ➜  {mensaje}\033[0m ")
    limpiar_pantalla()
    return entrada

def menu_inicio():
        print("\033[96m")
        print("╔══════════════════════════════════════════════╗")
        print("║       ¡Hola! Soy tu asistente virtual.       ║")
        print("╠══════════════════════════════════════════════╣")
        print("║              1 - Menu escolar                ║")
        print("║              2 - Recordatorios               ║")
        print("║              3 - Controlar gastos            ║")
        print("╠══════════════════════════════════════════════╣")
        print("║              0 - Regresar                    ║")
        print("╚══════════════════════════════════════════════╝")
        print("\033[0m")

def menu_estudiante():
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