from recordatorios import recordatorio, agregar_recordatorio, ver_recordatorios, modificar_recordatorio
from estudiante import agregar_materia,modulo_estudiante,ver_materias
from gastos import agregar_gasto,modulo_gastos,total_por_categoria,total_mes,gasto_mas_alto
from interfaz import pedir_input,limpiar_pantalla,menu_inicio


def asistente():

    continuar=True

    while continuar:
        
        limpiar_pantalla()

        menu_inicio()

        opcion= int(pedir_input("Seleccionar una opción: "))
        
        if opcion == 1:
            modulo_estudiante()
        elif opcion == 2:
            recordatorio()
        elif opcion == 3:
            modulo_gastos()
        elif opcion == 4:
            print("Borrar Recordatorio en desarrollo")
        elif opcion == 6:
            print("¡Hasta luego!")
            continuar = False
        else:
            print("Opción no válida. Por favor, intente nuevamente.")



if __name__ == "__main__":
    asistente()