from interfaz import pedir_input,limpiar_pantalla

def modulo_estudiante():

    materias = []
    examenes = []
    horas_estudio = []

    opcion = 0

<<<<<<< HEAD
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
=======
    while opcion !=9:
        limpiar_pantalla()
        menu_estudiante()
>>>>>>> 5aff0861b94aed7f7ce5d3729021109aca16543e

        opcion = int(input("Seleccione una opción: "))

        if opcion ==1:
            materia = input("Ingrese el nombre de la materia: ")
            
            fila = [materia, 0]
            materias.append(fila)

        elif opcion ==2:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
<<<<<<< HEAD
            
            else:
                
                for fila in materias:
                    print("Materia:", fila[0], "- Nota:", fila[1])

        elif opcion ==3:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
=======
>>>>>>> 5aff0861b94aed7f7ce5d3729021109aca16543e
            else:
                print("Materias:")

                for i in range(len(materias)):
                    print(i + 1, "-", materias[i][0])

                posicion = int(input("Seleccione la materia para registrar la nota: "))

                nota = float(input("Ingrese la nota: "))

                materias[posicion - 1][1] = nota
                print("Nota registrada correctamente.")

        elif opcion ==3:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
            else:

                print("Notas registradas:")
                for fila in materias:
                    print(fila[0], ":", fila[1])

<<<<<<< HEAD
        elif opcion ==5:
=======
                print("Materia:", materias[posicion - 1])
                print("Notas Registradas:")

                for nota in lista_notas:
                    print(nota)

                if len(lista_notas) > 0:
                    promedio = sum(lista_notas) / len(lista_notas)
                    print("Promedio:", promedio)

                    if promedio >= 8:
                        print("PROMOCIONA")
                    elif promedio >= 4:
                        print("REGULAR")
                    else:
                        print("RECURSA")


        if opcion ==4:
>>>>>>> 5aff0861b94aed7f7ce5d3729021109aca16543e
            
            suma = 0

            for fila in materias:
                suma = suma + fila[1]

            promedio = suma / len(materias)

            print("El promedio general es:", promedio)

        if opcion ==6:
            
            examen = input("Ingrese el nombre del examen: ")
            examenes.append(examen)

<<<<<<< HEAD
        elif opcion ==7:
=======
        elif opcion ==5:
>>>>>>> 5aff0861b94aed7f7ce5d3729021109aca16543e

            if len(examenes) ==0:
                print("No hay exámenes registrados.")

            else:
                print("Exámenes registrados:")
                for examen in examenes:
                    print(examen)

<<<<<<< HEAD
        elif opcion ==8:
            horas = int(input("Ingrese las horas de estudio: "))
            horas_estudio.append(horas)

        elif opcion ==9:
=======
        elif opcion ==6 :
            horas = int(pedir_input("Ingrese las horas de estudio: "))
            horas_estudio.append(horas)

        elif opcion ==7:
>>>>>>> 5aff0861b94aed7f7ce5d3729021109aca16543e
            print("Horas de estudio registradas: ")
            for horas in horas_estudio:
                print(horas)

<<<<<<< HEAD
        elif opcion ==10:
=======
        elif opcion ==8:
>>>>>>> 5aff0861b94aed7f7ce5d3729021109aca16543e

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