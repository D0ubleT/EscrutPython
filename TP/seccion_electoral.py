#!/usr/bin/env python
# -*- coding: latin-1 -*-

def seccion_valida(seccion_electoral):
    '''Dados los par�metros, devolver� un resultado booleano que indicar� si es v�lida.'''
    if (seccion_electoral <= 0 or seccion_electoral >= 16):
        return False
    else:
        return True




def main():

    seccion_electoral = input("Ingrese secci�n electoral: ")

    validar_seccion = seccion_valida (seccion_electoral)
  
    while validar_seccion != True:
        print 'Ha dado una secci�n no v�lida, reingresela por favor.'
        seccion_electoral = input("Ingrese secci�n electoral: ")

        validar_seccion = seccion_valida (seccion_electoral)


    if validar_seccion == True:
        print seccion electoral

main()
