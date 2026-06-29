# importacion de modulos funcionales del sistema 

from recordatorios import modulo_recordatorio
from estudiante import modulo_estudiante
from gastos import modulo_gastos
from interfaz import pedir_input,limpiar_pantalla,menu_inicio


def asistente():
    '''listas principales que mantienen el estado del sistema
    se conparten entre modulos para conservar la informacion'''

    materias = []
    examenes = []
    horas_estudio = []
    notas = []

    recordatorios = []

    continuar=True

    while continuar:   #bucle principal del sistema
        
        #limpia la pantalla para mejorar la interfaz visual
        limpiar_pantalla()

        # muestra el menu principal con los datos actuales        
        menu_inicio(materias,recordatorios)
        
        #solicita una opcion al usuario
        opcion= int(pedir_input("Seleccionar una opción: "))
        
        #redireccion a modulos segun la opcion elegida
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


#punto de entrada del programa
if __name__=="__main__":
    asistente()