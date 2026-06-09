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



    continuar=True

    while continuar:
        print("Hola, soy tu asistente vitual")
        print("1- Agregar Recordatorio")
        print("2- Ver Recordatorios")
        print("3- Borrar Recordatorio")
        opcion= int(input("Seleccione una opcion"))
        if opcion == 1:
            agregar_recordatorio(recordatorios)
        elif opcion == 2:
            ver_recordatorios(recordatorios)
        else:
            continuar=False
    
    return True

if __name__ == "__main__":
    asistente()