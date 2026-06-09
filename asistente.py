materias=[]

def agregar_recordatorio(recordatorios):
    print("Agregar Recordatorio")
    print("0 - cancelar")
    recordatorio = input("-")
    recordatorios.append(recordatorio)
    return True

def ver_recordatorios(recordatorios):
    print(recordatorios)

def agregar_materia():
    print('agregar materia')
    materia= input('ingrese el nombre de la materia')
    materias.append(materia)
    print('materia agregada correctamente')

def ver_materias():
    if len(materias) == 0:
        print('no hay materias registradas')
    else:
        print('las materias registradas son:')

        i=0

        while i < len(materias):
            print(materias[i])
            i= i+1

def asistente():
    recordatorios=["Beber agua"]

def modulo_estudiante():

    opcion = 0

    while opcion !=10:
        print("\n=== MÓDULO ESTUDIANTE ===")
        print("1. Agregar Materias")
        print("2. Ver Materias")
        print("3. Registrar Materias")
        print("4. Ver Notas")
        print("5. Calcular promedio general")
        print("6. Registrar examen")
        print("7. Ve próximos exámenes")
        print("8. Registrar horas de estudio")
        print("9. Volver al menú principal")




    continuar=True

    while continuar:
        print("Hola, soy tu asistente vitual")
        print("1- Ingresar al Módulo Estudiante")
        print("2- Agregar Recordatorio")
        print("3- Ver Recordatorios")
        print("4- Borrar Recordatorio")
        opcion= int(input("Seleccione una opcion"))
        print("¡Hola! Soy tu asistente virtual.")
        print("1- Agregar Recordatorio")
        print("2- Ver Recordatorios")
        print("3- Borrar Recordatorio")
        opcion= int(input("Seleccione una opción: "))
        if opcion == 1:
            print("Módulo Estudiante en desarrollo")
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