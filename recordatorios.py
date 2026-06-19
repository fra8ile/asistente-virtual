
recordatorios=[]


def agregar_recordatorio():
    print('agregar recordatorio:')

    titulo=input('ingrese el titulo del recordatorio')
    fecha=input('ingrese la fecha en formato dd/mm/aaaa:')
    hora= input('ingrese la hora en formato hh:mm:')

    recordatorio=[titulo, hora, fecha ]
    recordatorios.append(recordatorio)

    print('recordatorio agregado exitosamente')


def ver_recordatorios():

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


def modificar_recordatorio():
    
    ver_recordatorios()

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



def eliminar_recordatorio():
    
    ver_recordatorios()

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

    

def buscar_recordatorio():

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
            
def menu_recordatorio():

    opcion=0

    while opcion!=6:
        print('\n ==MENU DE RECORDATORIOS==')
        print('1.agregar recordatorio')
        print('2. ver recordatorio')
        print('3. modificar recordatorio')
        print('4. buscar recordatorio')
        print('5. eliminar recordatorio')
        print('6. volver al menu principal')
        
        opcion=int(input('seleccionar una opcion:'))

        if opcion ==1:
            agregar_recordatorio()
        elif opcion ==2:
            ver_recordatorios()
        elif opcion==3:
            modificar_recordatorio()
        elif opcion==4:
            buscar_recordatorio()
        elif opcion==5:
            eliminar_recordatorio()
        
        elif opcion ==6:
            print('volviendo al menu principal...')
        else:
            print('opcion invalida, intentelo nuevamnete')

