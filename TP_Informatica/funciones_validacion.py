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
    '''Dados los parámetros, devolverá un resultado booleano que indicará si el día es válido dependiendo el mes y el año correspondiente a la fecha ingresada.'''
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
    
def circuito_valido(ing_num_esc):
    '''Dados los parámetros, devolverá un resultado booleano que indicará si es válida.'''
    if (ing_num_esc <= 0 or ing_num_esc >= 167):
        return False
    else:
        return True

def seccion_valida(seccion_electoral):
    '''Dados los parámetros, devolverá un resultado booleano que indicará si es válida.'''
    if (seccion_electoral <= 0 or seccion_electoral >= 16):
        return False
    else:
        return True

def carga_votos(True):
#mesa
    mesa = input ("Favor de ingresar Nro de mesa, ej. 1: ")
    validar_mesa = mesa_valida(mesa)
    while validar_mesa != True:
        print 'Ha dado una mesa no válida, reingresela por favor.'
        mesa = raw_input("Ingrese mesa (Entre 1 y 7413): ")
        validar_mesa = mesa_valida(mesa)
        if validar_mesa == True:
             print mesa
#votos
    d_votos_totales={}
    d_votos = {'Alfa':0,'Beta':0,'Blanco':0,'votos':0}
    continuar = True
    while continuar == True and d_votos['votos'] <=349:
        ingreso_voto = raw_input("Ingrese voto: ")
        if ingreso_voto in d_votos:
            d_votos[ingreso_voto]+=1
        else:
            print "Error. La agrupación mencionada no se encuentra entre las candidatas."
            ingreso_voto = raw_input("Ingrese voto: ")
        d_votos['votos']+=1
        #d_votos_totales.update(d_votos) #Debería sumarse con cada vuelta, pero sólo suma el ultimo telegrama. #ERROR #cómo hacemos?
        
        continuar_carga = raw_input("Desea continuar ingresando votos? (S/N): ")
        if continuar_carga == 'N' or continuar_carga == 'n' or d_votos==350:
            continuar = False
    return d_votos,mesa,d_votos_totales

