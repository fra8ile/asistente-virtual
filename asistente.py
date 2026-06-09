def agregar_recordatorio(recordatorios):
    print("Agregar Recordatorio")
    print("0 - cancelar")
    recordatorio = input("-")
    recordatorios.append(recordatorio)
    return True

def ver_recordatorios(recordatorios):
    print(recordatorios)

def asistente():
    recordatorios=["Beber agua"]

def modulo_estudiante():

    materias = []
    notas = []
    examenes = []
    horas_estudio = []

    opcion = 0

    while opcion !=9:
        print("\n=== MÓDULO ESTUDIANTE ===")
        print("1. Agregar Materias")
        print("2. Ver Materias")
        print("3. Registrar Notas")
        print("4. Ver Notas")
        print("5. Calcular promedio general")
        print("6. Registrar examen")
        print("7. Ver próximos exámenes")
        print("8. Registrar horas de estudio")
        print("9. Volver al menú principal")

        opcion = int(input("Seleccione una opción: "))

        if opcion ==1:
            print("Agregar materia")
        if opcion ==2:
            print("Ver materias")
        if opcion ==3:
            print("Registrar notas")
        if opcion ==4:
            print("Ver notas")
        if opcion ==5:
            print("Calcular promedio")
        if opcion ==6:
            print("Registrar examen")
        if opcion ==7:
            print("Ver próximos exámenes")
        if opcion ==8:
            print("Registrar horas de estudio")




    continuar=True

    while continuar:
        print("Hola, soy tu asistente vitual")
        print("1- Ingresar al Módulo Estudiante")
        print("2- Agregar Recordatorio")
        print("3- Ver Recordatorios")
        print("4- Borrar Recordatorio")
        opcion= int(input("Seleccione una opcion"))
        if opcion == 1:
            modulo_estudiante()
        elif opcion == 2:
            agregar_recordatorio(recordatorios)
        elif opcion == 3:
            ver_recordatorios(recordatorios)
        elif opcion == 4:
            print("Borrar Recordatorio en desarrollo")
        else:
            continuar = False
    
    return True

if __name__ == "__main__":
    asistente()