from recordatorios import modulo_recordatorios
from estudiante import modulo_estudiante
from gastos import agregar_gasto,modulo_gastos,total_por_categoria,total_mes,gasto_mas_alto
from interfaz import pedir_input,limpiar_pantalla,menu_inicio,mensaje_error


def asistente():
    materias = []
    examenes = []
    horas_estudio = []

    recordatorios=[]

    gastos = []
    continuar=True
    limpiar_pantalla()
    while continuar:

        menu_inicio(materias,recordatorios,gastos)

        opcion= int(pedir_input("Seleccionar una opción: "))
        if opcion < 0 or opcion > 4:
            mensaje_error("Opción no válida. Por favor, intente nuevamente.")
        else:
            if opcion == 1:
                modulo_estudiante(materias,examenes,horas_estudio)
            elif opcion == 2:
                modulo_recordatorios(recordatorios)
            elif opcion == 3:
                modulo_gastos(gastos)
            elif opcion == 4:
                print("Borrar Recordatorio en desarrollo")
            else:
                print("¡Hasta luego!")
                continuar = False



if __name__ == "__main__":
    asistente()