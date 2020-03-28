#!/usr/bin/env python
# -*- coding: latin-1 -*-

def es_bisiesto(anio):
    '''Formato anio: s�lo n�meros. Divisible por 400 o 100 es cambio de siglo. Si es divisible por 4 es a�o bisiesto siempre que no sea divisible por 100.'''
    if (anio%400==0) or (anio%4==0 and anio%100!=0):
        bisiesto=True
    else:
        bisiesto=False
    return bisiesto

def cant_dias_mes(mes,anio):
    '''Se introducen mes y a�o. Formato mes: sin cero adelante, s�lo n�meros. Formato anio: cuatro d�gitos, s�lo n�meros. Esta funci�n devolver� la cantidad de d�as correspondiente al mes introducido manualmente.'''
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
    '''Dados los par�metros, devolver� un resultado booleano que indicar� si es v�lida o no.'''
    fecha=0
    if mes<1 or mes>12: #meses inv�lidos
        fecha=False
    elif mes>1 or mes<12: #meses v�lidos
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
    


def main():
    '''Este sistema permite al encargado ingresar datos de telegramas de votos emitidos en la escuela. Ingresar� fecha, datos de la escuela y los datos de cada telegrama.'''

    print "Recuento de votos\n"

    ing_dia = input("Ingrese d�a: ")
    ing_mes = input("Ingrese mes, num�rico: ")
    ing_anio = input("Ingrese a�o, cuatro cifras: ")


    verificar_anio = anios_posibles(ing_anio)
    while verificar_anio != True:
        print "S�lo se permiten a�os entre 2015 y 2027, inclusive."
        ing_anio = input("Reingrese a�o: ")
        verificar_anio = anios_posibles(ing_anio)
        
        
    validar_fecha = fecha_valida (ing_dia,ing_mes,ing_anio)
    while validar_fecha != True:
        print 'Ha dado una fecha no v�lida, reingrese la fecha por favor.'
        ing_dia = input("Reingrese d�a: ")
        ing_mes = input("Reingrese mes: ")
        ing_anio = input("Reingrese a�o: ")

        validar_fecha = fecha_valida (ing_dia,ing_mes,ing_anio)

    if validar_fecha == True:
        print ing_dia,'/',ing_mes,'/',ing_anio

main()


