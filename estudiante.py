from interfaz import pedir_input,limpiar_pantalla

def modulo_estudiante():

    materias = []
    examenes = []
    horas_estudio = []

    opcion = 0

    while opcion !=11:
        print("\n=== MÓDULO ESTUDIANTE ===")
        print("1. Agregar Materias")
        print("2. Ver Materias")
        print("3. Registrar Notas")
        print("4. Ver Notas")
        print("5. Calcular promedio general")
        print("6. Registrar examen")
        print("7. Ver exámenes")
        print("8. Registrar horas de estudio")
        print("9. Ver horas de estudio")
        print("10. Ver boletín académico")
        print("11. Volver al menú principal")

        opcion = int(input("Seleccione una opción: "))

        if opcion ==1:
            materia = input("Ingrese el nombre de la materia: ")
            
            fila = [materia, 0]
            materias.append(fila)

        elif opcion ==2:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
            
            else:
                
                for fila in materias:
                    print("Materia:", fila[0], "- Nota:", fila[1])

        elif opcion ==3:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
            else:
                print("Materias:")

                for i in range(len(materias)):
                    print(i + 1, "-", materias[i][0])

                posicion = int(input("Seleccione la materia para registrar la nota: "))

                nota = float(input("Ingrese la nota: "))

                materias[posicion - 1][1] = nota
                print("Nota registrada correctamente.")

        elif opcion ==4:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
            else:

                print("Notas registradas:")
                for fila in materias:
                    print(fila[0], ":", fila[1])

        elif opcion ==5:
            
            suma = 0

            for fila in materias:
                suma = suma + fila[1]

            promedio = suma / len(materias)

            print("El promedio general es:", promedio)

        if opcion ==6:
            
            examen = input("Ingrese el nombre del examen: ")
            examenes.append(examen)

        elif opcion ==7:

            if len(examenes) ==0:
                print("No hay exámenes registrados.")

            else:
                print("Exámenes registrados:")
                for examen in examenes:
                    print(examen)

        elif opcion ==8:
            horas = int(input("Ingrese las horas de estudio: "))
            horas_estudio.append(horas)

        elif opcion ==9:
            print("Horas de estudio registradas: ")
            for horas in horas_estudio:
                print(horas)

        elif opcion ==10:

            print("\n=== BOLETÍN ACADÉMICO ===")
            
            suma = 0

            for fila in materias:

                materia = fila[0]
                nota = fila[1]

                if nota >= 4:
                    estado = "Aprobado"
                else:
                    estado = "Reprobado"

                print(materia, "- Nota:", nota, "-", estado)
                
                suma = suma + nota
            
            if len(materias) > 0:
                promedio = suma / len(materias)
                print("Promedio general:", promedio)