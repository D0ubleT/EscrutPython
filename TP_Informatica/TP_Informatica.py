#!/usr/bin/env python
# -*- coding: latin-1 -*-

from funciones_validacion import es_bisiesto, cant_dias_mes, dia_valido, fecha_valida, anios_posibles, mesa_valida, circuito_valido, seccion_valida, carga_votos

def main():
    '''Este sistema permite al encargado ingresar datos de telegramas de votos emitidos en la escuela. Ingresar� fecha, 
    datos de la escuela y los datos de cada telegrama'''

    print "Recuento de votos\n"

    #Fecha
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

    #Escuela
        #N�mero
            #Validez entre 1 y 167
    ing_num_esc = input("Ingrese el n�mero de la escuela: ")
    validar_circuito = circuito_valido(ing_num_esc)
    while validar_circuito != True:
        print 'Ha dado un n�mero de escuela no v�lida, reingreselo por favor.'
        ing_num_esc = input("Ingrese el n�mero de la escuela: ")
        validar_circuito = circuito_valido(ing_num_esc)
    if validar_circuito == True:
        print ing_num_esc
        
        #Nombre
    ing_nombre_esc = raw_input("Ingrese el nombre de la escuela: ")

        #Secci�n electoral
            #Validez entre 1 y 15
    seccion_electoral = input("Ingrese secci�n electoral: ")
    validar_seccion = seccion_valida(seccion_electoral)
    while validar_seccion != True:
        print 'Ha dado una secci�n no v�lida, reingresela por favor.'
        seccion_electoral = input("Ingrese secci�n electoral: ")
        validar_seccion = seccion_valida (seccion_electoral)
    if validar_seccion == True:
        print seccion_electoral
        
        #Carga
    continua_escuela = True
    votos_totales={}
    while continua_escuela == True:
        votos_por_mesa, mesa, votos_totales = carga_votos(True)
        print ing_nombre_esc,': Los datos del telegrama son:',votos_por_mesa,'votos de la mesa',mesa
        continuar_carga = raw_input("Desea continuar cargando telegramas? (S/N): ")
        if continuar_carga == 'N' or continuar_carga == 'n':
            continua_escuela = False
            print "Escuela",ing_nombre_esc," N�mero",ing_num_esc,".\n"
            print "Secci�n electoral",seccion_electoral,".\n"
            print "Votos totales:",votos_totales['votos'],".\n"

            print "Votos para Alfa:",votos_totales['Alfa'],((votos_totales['Alfa']*100)/(votos_totales['votos']-votos_totales['Blanco'])),"%"
            print "Votos para Beta:",votos_totales['Beta'],((votos_totales['Beta']*100)/(votos_totales['votos']-votos_totales['Blanco'])),"%"
            print "Votos en blanco:",votos_totales['Blanco'],((votos_totales['Alfa']*100)/votos_totales['votos']),"%"

main()    
            
