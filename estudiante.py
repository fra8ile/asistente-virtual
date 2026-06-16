from interfaz import pedir_input,limpiar_pantalla,menu_estudiante,mensaje_error,ver_materias
def prom_general(materias):
    acum = 0
    for i in range(len(materias)):
        sum=0
        for j in range(len(materias[i][1])):
            sum += materias[i][1][j]
        promedio = sum / len(materias[i][1])
        acum += promedio
        print(f"Promedio de {materias[i][0]}: {promedio}")

    print(f"Promedio general: {acum / len(materias)}")
def modulo_estudiante(materias,examenes,horas_estudio):

    opcion = 0
    continuar=True
    while continuar:

        menu_estudiante(materias)
        opcion = int(pedir_input("Seleccione una opción: "))
        if opcion <0 or opcion>5:
            mensaje_error("Opción no válida. Por favor, intente nuevamente.")
        else:
            if opcion ==1:
                materia = pedir_input("Ingrese el nombre de la materia [A-Z]: ")
                if len(materia) > 0:
                    materias.append([materia, []])

            elif opcion ==2:
                
                if len(materias) ==0:
                    mensaje_error("No hay materias registradas.")
                else:
                    print("\033[32m╔══════════════════════════════════════════════════════╗")
                    print("║                        MATERIAS                      ║")
                    print("╠══════════════════════════════════════════════════════╣\033[0m")

                    for i in range(len(materias)):
                        print(i + 1, "-", materias[i][0])

                    posicion = int(pedir_input("Seleccione la materia para registrar la nota: "))
                    
                    if posicion > len(materias) or posicion < 1:
                        mensaje_error("Posicion invalida. Intentelo nuevamente.")
                    
                    else:
                        nota = float(pedir_input(f"Ingrese la nota n°{len(materias[posicion - 1][1]) + 1}: "))
                        materias[posicion - 1][1].append(nota)
                        print("Nota registrada correctamente.")
                

            elif opcion ==3:
                horas = int(pedir_input("Ingrese las horas de estudio: "))
                horas_estudio.append(horas)

            elif opcion ==4:
                print("Horas de estudio registradas: ")
                for horas in horas_estudio:
                    print(horas)

            elif opcion == 5:

                print("\n╔══════════════════════════════════════════════╗")
                print("║              BOLETÍN ACADÉMICO               ║")
                print("╠══════════════════════════════════════════════╣")

                if len(materias) == 0:

                    print("║         No hay materias registradas         ║")

                else:

                    suma_promedios = 0

                    for materia, notas in materias:

                        if len(notas) == 0:
                            promedio = 0
                        else:
                            promedio = sum(notas) / len(notas)

                        suma_promedios += promedio

                        estado = "APROBADO" 
                        if promedio >7 :
                            estado="Promocionado" 
                        elif promedio >= 4 :
                            estado="Aprobado" 
                        else: estado="Reprobado"

                        texto = f"{materia[:20]:<20} {promedio:>5.2f}  {estado}"

                        print(f"║ {texto:<44} ║")

                    promedio_general = suma_promedios / len(materias)

                    print("╠══════════════════════════════════════════════╣")

                    texto = f"PROMEDIO GENERAL: {promedio_general:.2f}"

                    print(f"║ {texto.center(44)} ║")

                print("╚══════════════════════════════════════════════╝")
            else:
                print('volviendo al menu principal...')
                continuar=False