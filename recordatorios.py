
recordatorios=[]

def fecha_valida(dia, mes, año):

    valido = 1

    if mes < 1 or mes > 12:
        valido = 0
    else:

        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dias_en_el_mes = dias_por_mes[mes - 1]

        if mes == 2 and año % 4 == 0:
            dias_en_el_mes = 29

        if dia < 1 or dia > dias_en_el_mes:
            valido = 0

    return valido

def hora_valida(hora, minuto):

    valido = 1

    if hora < 0 or hora > 23:
        valido = 0
    elif minuto < 0 or minuto > 59:
        valido = 0

    return valido


def agregar_recordatorio():
    print('agregar recordatorio:')

    titulo=input('ingrese el titulo del recordatorio')

    dia = int(input('ingrese el dia (numero): '))
    mes = int(input('ingrese el mes (numero): '))
    año = int(input('ingrese el año (numero, ej 2026): '))

    fecha=fecha_valida(dia, mes, año)

    while fecha == 0:

        print('fecha invalida, intentelo nuevamente')
        
        dia = int(input('ingrese el dia (numero): '))
        mes = int(input('ingrese el mes (numero): '))
        año = int(input('ingrese el año (numero, ej 2026): '))
    
    hora = int(input('ingrese la hora (0 a 23): '))
    minuto = int(input('ingrese los minutos (0 a 59): '))

    hora_total = hora_valida(hora, minuto)

    while hora_total == 0:
        
        print('hora invalida, intentelo nuevamente')

        hora = int(input('ingrese la hora (0 a 23): '))
        minuto = int(input('ingrese los minutos (0 a 59): '))
        
    prioridad = input('ingrese la prioridad (ALTA/MEDIA/BAJA): ')

    while prioridad != 'ALTA' and prioridad != 'MEDIA' and prioridad != 'BAJA' and prioridad != 'alta' and prioridad != 'media' and prioridad != 'baja':
        
        print('prioridad invalida, intentelo nuevamente')
        
        prioridad = input('ingrese la prioridad (ALTA/MEDIA/BAJA): ')

    
    recordatorio = [titulo, [dia, mes, año], [hora, minuto], prioridad]
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

            fecha = recordatorio[1]
            hora_completa = recordatorio[2]

            print(i+1, '-', recordatorio[0], '|', fecha[0], '/', fecha[1], '/', fecha[2], '|', hora_completa[0], ':', hora_completa[1], '|', recordatorio[3])

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

            nuevo_titulo=input('ingrese el nuevo titulo del recordatorio:')

            fecha_nueva= 0
            while fecha_nueva == 0:
                
                nuevo_dia = int(input('ingrese el nuevo dia (numero): '))
                nuevo_mes = int(input('ingrese el nuevo mes (numero): '))
                nuevo_año = int(input('ingrese el nuevo año (numero, ej 2026): '))

                if fecha_valida(nuevo_dia, nuevo_mes, nuevo_año) == 0:
                    print('fecha invalida, intentelo nuevamente')
                
                else:
                    fecha_nueva= 1

            hora_nueva = 0
            
            while hora_nueva == 0:
                
                nueva_hora = int(input('ingrese la nueva hora (0 a 23): '))
                nuevo_minuto = int(input('ingrese los nuevos minutos (0 a 59): '))

                if hora_valida(nueva_hora, nuevo_minuto) == 0:
                    print('hora invalida, intentelo nuevamente')
               
                else:
                    hora_nueva= 1

            nueva_prioridad = 0
            
            while nueva_prioridad == 0:
                
                cambio_prioridad = input('ingrese la nueva prioridad (ALTA/MEDIA/BAJA): ')

                if cambio_prioridad != 'ALTA' and cambio_prioridad != 'MEDIA' and cambio_prioridad != 'BAJA' and cambio_prioridad != 'alta' and cambio_prioridad != 'media' and cambio_prioridad != 'baja':
                    print('prioridad invalida, intentelo nuevamente')
                
                else:
                
                    nueva_prioridad= 1

            recordatorio= recordatorios[indice-1]

            recordatorio[0] = nuevo_titulo
            recordatorio[1] = [nuevo_dia, nuevo_mes, nuevo_año]
            recordatorio[2] = [nueva_hora, nuevo_minuto]
            recordatorio[3] = cambio_prioridad

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
                
                fecha = recordatorio[1]
                hora_completa = recordatorio[2]
                
                print('-', recordatorio[0], '|', fecha[0], '/', fecha[1], '/', fecha[2], '|', hora_completa[0], ':', hora_completa[1], '|', recordatorio[3])
                
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

