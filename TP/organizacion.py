#!/usr/bin/env python
# -*- coding: latin-1 -*-

def es_bisiesto(anio):
    '''Formato anio: sólo números. Divisible por 400 o 100 es cambio de siglo. Si es divisible por 4 es año bisiesto siempre que no sea divisible por 100.'''
    if (anio%400==0) or (anio%4==0 and anio%100!=0):
        bisiesto=True
    else:
        bisiesto=False
    return bisiesto

def cant_dias_mes(mes,anio):
    '''Se introducen mes y año. Formato mes: sin cero adelante, sólo números. Formato anio: cuatro dígitos, sólo números. Esta función devolverá la cantidad de días correspondiente al mes introducido manualmente.'''
    cant_dias=0
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        cant_dias=31
    elif mes==4 or mes==6 or mes==9 or mes==11:
        cant_dias=30
    elif mes==2:
        bisiesto = es_bisiesto(anio)
        if bisiesto==True:
            cant_dias=29
        else:
            cant_dias=28
    else:
        cant_dias=False
    return cant_dias

def dia_valido(dia,mes,anio):
    if (dia <= 0 or dia > cant_dias_mes(mes,anio)):
        return False
    else:
        return True

def fecha_valida(dia,mes,anio):
    '''Dados los parámetros, devolverá un resultado booleano que indicará si es válida o no.'''
    fecha=0
    if mes<1 or mes>12: #meses inválidos
        fecha=False
    elif mes>1 or mes<12: #meses válidos
        dia_val = dia_valido(dia,mes,anio)
        if dia_val==False:
            fecha=False
        else:
            fecha=True
    return fecha

def anios_posibles(anio):
    '''entre 2015 y 2027 incluidos'''
    if (anio < 2015 or anio > 2027):
        return False
    else:
        return True

def mesa_valida(mesa_electoral):
    '''Dados los parámetros, devolverá un resultado booleano que indicará si es válida.'''
    if (mesa_electoral <= 0 or mesa_electoral >= 7414):
        return False
    else:
        return True
    
def circuito_valido(circuito):
    '''Dados los parámetros, devolverá un resultado booleano que indicará si es válida.'''
    if (circuito <= 0 or circuito >= 167):
        return False
    else:
        return True

def seccion_valida(seccion_electoral):
    '''Dados los parámetros, devolverá un resultado booleano que indicará si es válida.'''
    if (seccion_electoral <= 0 or seccion_electoral >= 16):
        return False
    else:
        return True










#MAIN

def main():
    '''Este sistema permite al encargado ingresar datos de telegramas de votos emitidos en la escuela. Ingresará fecha, datos de la escuela y los datos de cada telegrama.'''

    print "Recuento de votos\n"

    #Fecha
        ing_dia = input("Ingrese día: ")
    ing_mes = input("Ingrese mes, numérico: ")
    ing_anio = input("Ingrese año, cuatro cifras: ")
    verificar_anio = anios_posibles(ing_anio)
    while verificar_anio != True:
        print "Sólo se permiten años entre 2015 y 2027, inclusive."
        ing_anio = input("Reingrese año: ")
        verificar_anio = anios_posibles(ing_anio)   
    validar_fecha = fecha_valida (ing_dia,ing_mes,ing_anio)
    while validar_fecha != True:
        print 'Ha dado una fecha no válida, reingrese la fecha por favor.'
        ing_dia = input("Reingrese día: ")
        ing_mes = input("Reingrese mes: ")
        ing_anio = input("Reingrese año: ")
        validar_fecha = fecha_valida (ing_dia,ing_mes,ing_anio)
    if validar_fecha == True:
        print ing_dia,'/',ing_mes,'/',ing_anio

    #Escuela
        #Número
    ing_num_esc= input("Ingrese el número de la escuela: ")
        #Nombre
    ing_nombre_esc= input_raw("Ingrese el nombre de la escuela: ")
        #Sección electoral
            #Validez entre 1 y 15
    seccion_electoral = input("Ingrese sección electoral: ")
    validar_seccion = seccion_valida (seccion_electoral)
    while validar_seccion != True:
        print 'Ha dado una sección no válida, reingresela por favor.'
        seccion_electoral = input("Ingrese sección electoral: ")
        validar_seccion = seccion_valida (seccion_electoral)
    if validar_seccion == True:
        print seccion electoral
        #Circuito
            #Validez entre 1 y 167
    circuito = input("Ingrese circuito: ")
    validar_circuito = circuito_valido (circuito)
    while validar_circuito != True:
        print 'Ha dado un circuito no válido, reingreselo por favor.'
        circuito = input("Ingrese circuito: ")
        validar_circuito = circuito_valido (circuito)
    if validar_circuito == True:
        print circuito


#CADA TELEGRAMA
        #Mesa
            #Validez entre 1 y 7413
    continuar_mesa = True

    while continuar_mesa == True:
        while (votos <= 350):
            mesa_electoral = input("Ingrese mesa: ")
            validar_mesa = mesa_valida (mesa_electoral)
            while validar_mesa != True:
                print 'Ha dado una mesa no válida, reingresela por favor.'
                mesa_electoral = input("Ingrese mesa: ")
                validar_mesa = mesa_valida (mesa_electoral)
            if validar_mesa == True:
                print mesa_electoral

        #Agrupación o Clase de Voto
                #Alfa, Beta, En Blanco
            votos+=1
            #aquí iría el tema del diccionario y todo eso. conteo por tipo de votos, voto en blanco y demás.

            
        while cantidad_votos == 350:
            print "Ha llegado a los 350 votos permitidos en la mesa."

        nueva_mesa = raw_input ("¿Desea agregar otra mesa? S/N \n")
        if nueva_mesa == 'S' or nueva_mesa == 's':
            continuar_mesa = True
        









        
    Ingreso de cada telegrama:
        Numero de mesa electoral
            #Validez entre 1 y 7413
        Agrupación o clase de voto: (Diccionario para el conteo)
            Alfa
            Beta
            En Blanco
        Cantidad de votos para la categoría "Jefe de Gobierno" obtenidos en la mesa por agrupación o clase de voto
            #Validez que no supere 350 por cada mesa.

        Que muestre simultáneamente en pantalla todos los datos validados de cada telegrama
        (mesa, agrupación o clase de voto, categoría, cantidad de votos) a medida que son ingresados.
        Que determine y muestre junto a los datos de la escuela la cantidad total de votos.
        Que deterime y muestre la cantidad de votos obtenidos por cada agrupación y su respectivo
        porcentaje sobre el total (excluyendo del mismo la cantidad de votos en blancoque serán mostrados aparte.)
        
            
