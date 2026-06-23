from recordatorios import modulo_recordatorio
from estudiante import modulo_estudiante
from gastos import modulo_gastos
from interfaz import pedir_input,limpiar_pantalla,menu_inicio


def asistente():
    materias = []
    examenes = []
    horas_estudio = []
    notas = []

    recordatorios = []

    continuar=True

    while continuar:
        
        limpiar_pantalla()

        menu_inicio(materias,recordatorios)

        opcion= int(pedir_input("Seleccionar una opción: "))
        
        if opcion == 1:
            modulo_estudiante(materias,examenes,horas_estudio,notas)
        elif opcion == 2:
            modulo_recordatorio(recordatorios)
        elif opcion == 3:
            modulo_gastos()
        elif opcion == 0:
            print("¡Hasta luego!")
            continuar = False
        else:
            print("Opción no válida. Por favor, intente nuevamente.")



if __name__ == "__main__":
    asistente()