#!/usr/bin/env python
# -*- coding: latin-1 -*-

def circuito_valido(circuito):
    '''Dados los par�metros, devolver� un resultado booleano que indicar� si es v�lida.'''
    if (circuito <= 0 or circuito >= 167):
        return False
    else:
        return True




def main():

    circuito = input("Ingrese circuito: ")

    validar_circuito = circuito_valido (circuito)
  
    while validar_circuito != True:
        print 'Ha dado un circuito no v�lido, reingreselo por favor.'
        circuito = input("Ingrese circuito: ")

        validar_circuito = circuito_valido (circuito)


    if validar_circuito == True:
        print circuito

main()
