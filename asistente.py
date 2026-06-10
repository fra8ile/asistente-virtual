from recordatorios import agregar_recordatorio, ver_recordatorios
from estudiante import agregar_materia,modulo_estudiante,ver_materias
from gastos import agregar_gasto,modulo_gastos,total_por_categoria,total_mes,gasto_mas_alto

recordatorios = []

def asistente():

    continuar=True

    while continuar:
        print("¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
        print("1- Ingresar al Módulo Estudiante")
        print("2- Ingresar al Módulo Gastos")
        print("3- Agregar Recordatorio")
        print("4- Ver Recordatorios")
        print("5- Borrar Recordatorio")
        print("6- Salir")

        opcion= int(input("Seleccione una opción: "))
        
        if opcion == 1:
            modulo_estudiante()
        elif opcion == 2:
            modulo_gastos()
        elif opcion == 3:
            agregar_recordatorio(recordatorios)
        elif opcion == 4:
            ver_recordatorios(recordatorios)
        elif opcion == 5:
            print("Borrar Recordatorio en desarrollo")
        elif opcion == 6:
            print("¡Hasta luego!")
            continuar = False
        else:
            print("Opción no válida. Por favor, intente nuevamente.")



if __name__ == "__main__":
    asistente()