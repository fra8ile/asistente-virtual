from interfaz import menu_recordatorio,mensaje_error,pedir_input

def agregar_recordatorio(recordatorios):

    print("Agregar recordatorio")

    titulo = pedir_input("Ingrese el título del recordatorio (0 para cancelar)")

    if titulo == "0":
        return

    while len(titulo.strip()) == 0:
        mensaje_error("El título no puede estar vacío")
        titulo = pedir_input("Ingrese el título del recordatorio (0 para cancelar)")

        if titulo == "0":
            return

    # DIA
    while True:

        dd = int(pedir_input("Ingrese día (1-31) [0 cancelar]:"))

        if dd == 0:
            return

        if 1 <= dd <= 31:
            break

        mensaje_error("Día no válido")

    # MES
    while True:

        mm = int(pedir_input("Ingrese mes (1-12) [0 cancelar]:"))

        if mm == 0:
            return

        if 1 <= mm <= 12:
            break

        mensaje_error("Mes no válido")

    # AÑO
    while True:

        aaaa = int(pedir_input("Ingrese año [0 cancelar]:"))

        if aaaa == 0:
            return

        if aaaa >= 2025:
            break

        mensaje_error("Año no válido")

    # HORA
    while True:

        hh = int(pedir_input("Ingrese hora (0-23) [-1 cancelar]:"))

        if hh == -1:
            return

        if 0 <= hh <= 23:
            break

        mensaje_error("Hora no válida")

    # MINUTOS
    while True:

        mn = int(pedir_input("Ingrese minutos (0-59) [-1 cancelar]:"))

        if mn == -1:
            return

        if 0 <= mn <= 59:
            break

        mensaje_error("Minutos no válidos")

    fecha = f"{dd:02d}/{mm:02d}/{aaaa}"
    hora = f"{hh:02d}:{mn:02d}"

    recordatorio = [titulo, hora, fecha]
    recordatorios.append(recordatorio)

    print("Recordatorio agregado exitosamente")


def ver_recordatorios(recordatorios):

    cant_recordatorios= len(recordatorios)

    if cant_recordatorios ==0 :
        print('no hay recordatorios registrados')
    else:
        print('recordatorios registrados:')

        i=0

        while i < cant_recordatorios:

            recordatorio= recordatorios[i]

            print(i+1, '-',recordatorio[0],'|',recordatorio[1],'|', recordatorio[2])

            i = i+1 


def modificar_recordatorio(recordatorios):
    
    ver_recordatorios(recordatorios)

    cant_recordatorios= len(recordatorios)

    if cant_recordatorios==0:
        print('no hay recordatorios registraodos')
    else:

        indice= int(input('ingrese el numero del item que desea modificar:'))

        if indice<1 or indice> cant_recordatorios:
            print('indice no valido, intentelo nuevamente')

        else:

            nuevo_titulo=input('ingrese el nuevo tituilo del recordatorio:')
            nueva_fecha=input('ingrese la nueva fecha en formato dd/mm/aaaa:')
            nueva_hora=input('ingrese la nueva hora en formato hh:mm :')

            recordatorio= recordatorios[indice-1]

            recordatorio[0]= nuevo_titulo
            recordatorio[1]=nueva_hora
            recordatorio[2]=nueva_fecha

            print('recordatorio modificado exitosamente')



def eliminar_recordatorio(recordatorios):
    
    ver_recordatorios(recordatorios)

    cant_recordatorios= len(recordatorios)

    if cant_recordatorios==0:
        print('no hay recordatorios registrados')
    else: 
        indice=int(input('ingrese el numero del item que desea eliminar:'))

        if indice<1 or indice>cant_recordatorios:
            print('indece no valido, intentelo nuevamente')
        else:
            recordatorios.pop(indice-1)
            
            print('recordatorio elimnado exitosamente')

    

def buscar_recordatorio(recordatorios):

    cant_recordatorios= len(recordatorios)
    
    if cant_recordatorios==0:
        print('no hay recordatorios registrados')
    else:
        titulo_buscado=input('ingrese el titulo del recordatorio que desea buscar:')

        i=0
        contador=0

        while i<cant_recordatorios:

            recordatorio=recordatorios[i]

            if recordatorio[0] == titulo_buscado:
                print('recordatorio encontrado:')
                print('-',recordatorio[0],'|',recordatorio[1],'|',recordatorio[2])
            
                contador= contador+1
            i= i+1
            
        if contador==0:
            print('no se encontro el recordatorio con el titulo ingresado')
            
def modulo_recordatorios(recordatorios):

    continuar=True

    while continuar:
        
        menu_recordatorio(recordatorios)
        opcion=int(pedir_input('seleccionar una opcion:'))
        if opcion <0 or opcion>5:
            mensaje_error('opcion invalida, intentelo nuevamnete')
        else:
            if opcion ==1:
                agregar_recordatorio(recordatorios)
            elif opcion==2:
                modificar_recordatorio(recordatorios)
            elif opcion==3:
                buscar_recordatorio(recordatorios)
            elif opcion==4:
                eliminar_recordatorio(recordatorios)
            
            elif opcion ==0:
                print('volviendo al menu principal...')
                continuar=False
            else:
                print('opcion invalida, intentelo nuevamnete')


