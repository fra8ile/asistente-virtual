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
        print("║              MÓDULO ESTUDIANTE              ║")
        print("╠══════════════════════════════════════════════╣")
        print("║              1 - Agregar Materias            ║")
        print("║              2 - Ver Materias                ║")
        print("║              3 - Registrar Notas            ║")
        print("║              4 - Ver Notas                  ║")
        print("║              5 - Calcular promedio general   ║")
        print("║              6 - Registrar examen           ║")
        print("║              7 - Ver exámenes               ║")
        print("║              8 - Registrar horas de estudio  ║")
        print("║              9 - Ver horas de estudio       ║")
        print("║             10 - Ver boletín académico      ║")
        print("╠══════════════════════════════════════════════╣")
        print("║             11 - Volver al menú principal    ║")
        print("╚══════════════════════════════════════════════╝")
        print("\033[0m")