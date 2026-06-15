from interfaz import menu_recordatorio,mensaje_error,pedir_input

def agregar_recordatorio(recordatorios):
    print('agregar recordatorio:')

    titulo=pedir_input('ingrese el titulo del recordatorio')
    if len(titulo) == 0:
        mensaje_error("Titulo no puede ser vacío")
    else:
        dd=int(pedir_input('ingrese dia (dd):'))
        mm=0
        aaaa=0
        fecha=""
        if dd>0 and dd<31:        
            mm=int(pedir_input('ingrese mes (mm):'))
            if mm>0 and mm<13:
                aaaa=int(pedir_input('ingrese año (aaaa):'))
                fecha=f'{dd}/{mm}/{aaaa}'
            else:
                mensaje_error("Mes no válido")
        else:
            mensaje_error("Dia no válido")

        hora= pedir_input('ingrese la hora en formato hh:mm:')

        recordatorio=[titulo, hora, fecha ]
        recordatorios.append(recordatorio)

        print('recordatorio agregado exitosamente')


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
        
        menu_recordatorio()
        opcion=int(pedir_input('seleccionar una opcion:'))
        if opcion <0 or opcion>6:
            mensaje_error('opcion invalida, intentelo nuevamnete')
        else:
            if opcion ==1:
                agregar_recordatorio(recordatorios)
            elif opcion ==2:
                ver_recordatorios(recordatorios)
            elif opcion==3:
                modificar_recordatorio(recordatorios)
            elif opcion==4:
                buscar_recordatorio(recordatorios)
            elif opcion==5:
                eliminar_recordatorio(recordatorios)
            
            elif opcion ==0:
                print('volviendo al menu principal...')
                continuar=False
            else:
                print('opcion invalida, intentelo nuevamnete')


