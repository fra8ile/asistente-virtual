from recordatorios import agregar_recordatorio
# from gastos import 
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
            agregar_recordatorio()
        elif opcion == 3:
            modulo_gastos()
        elif opcion == 4:
            print("Borrar Recordatorio en desarrollo")
        else:
            continuar = False
    
    return True

if __name__ == "__main__":
    asistente()