from interfaz import pedir_input,limpiar_pantalla,menu_estudiante

def modulo_estudiante():

    materias = []
    examenes = []
    horas_estudio = []
    notas = []

    opcion = 0

    while opcion !=10:
        limpiar_pantalla()
        menu_estudiante()

        opcion = int(pedir_input("Seleccione una opción: "))

        if opcion ==1:
            materia = pedir_input("Ingrese el nombre de la materia: ")

            materias.append(materia)
            notas.append([])

        elif opcion ==2:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
            
            else:
                
                for materia in materias:
                    print("Materia:", materia)

        elif opcion ==3:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
            else:
                print("Materias:")

                for i in range(len(materias)):
                    print(i + 1, "-", materias[i])

                posicion = int(pedir_input("Seleccione la materia para registrar la nota: "))

                nota = float(pedir_input("Ingrese la nota: "))

                notas[posicion - 1].append(nota)

                print("Nota registrada correctamente.")

        elif opcion ==4:
            
            if len(materias) ==0:
                print("No hay materias registradas.")
            else:

                for i in range(len(materias)):
                    print(i + 1, "-", materias[i])
                
                posicion = int(pedir_input("Seleccione la materia para ver las notas: "))
                
                lista_notas = notas[posicion - 1]

                print("Materia:", materias[posicion - 1])
                print("Notas:", lista_notas)

                if len(lista_notas) > 0:
                    promedio = sum(lista_notas) / len(lista_notas)
                    print("Promedio:", promedio)

                    if promedio >= 8:
                        print("PROMOCIONA")
                    elif promedio >= 4:
                        print("REGULAR")
                    else:
                        print("RECURSA")


        if opcion ==5:
            
            examen = pedir_input("Ingrese el nombre del examen: ")
            examenes.append(examen)

        elif opcion ==6:

            if len(examenes) ==0:
                print("No hay exámenes registrados.")

            else:
                print("Exámenes registrados:")
                for examen in examenes:
                    print(examen)

        elif opcion ==7 :
            horas = int(pedir_input("Ingrese las horas de estudio: "))
            horas_estudio.append(horas)

        elif opcion ==8:
            print("Horas de estudio registradas: ")
            for horas in horas_estudio:
                print(horas)

        elif opcion ==9:

            print("\n=== BOLETÍN ACADÉMICO ===")
            
            suma_promedios = 0
            cantidad_materias = 0

            for i in range(len(materias)):
               
                materia = materias[i]

                if len(notas[i]) > 0:

                    promedio = sum(notas[i]) / len(notas[i])

                    if promedio >= 8:
                        estado = "PROMOCIONA"
                    elif promedio >= 4:
                        estado = "REGULAR"
                    else:
                        estado = "RECURSA"
                    
                    print(materia)
                    print("Notas:", notas[i])
                    print("Promedio:", promedio)
                    print("Estado:", estado)
                    print()

                    suma_promedios += promedio
                    cantidad_materias += 1

            if cantidad_materias > 0:

                promedio_general = suma_promedios / cantidad_materias

                print("Promedio general:", promedio_general)

            else:
                print("No hay materias con notas registradas.")