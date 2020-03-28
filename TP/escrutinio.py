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
    


def main():
    '''Este sistema permite al encargado ingresar datos de telegramas de votos emitidos en la escuela. Ingresará fecha, datos de la escuela y los datos de cada telegrama.'''

    print "Recuento de votos\n"

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

main()


