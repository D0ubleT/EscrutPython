#!/usr/bin/env python
# -*- coding: latin-1 -*-

def mesa_valida(mesa_electoral):
    '''Dados los par�metros, devolver� un resultado booleano que indicar� si es v�lida.'''
    if (mesa_electoral <= 0 or mesa_electoral >= 7414):
        return False
    else:
        return True




def main():

    mesa_electoral = input("Ingrese mesa: ")

    validar_mesa = mesa_valida (mesa_electoral)
  
    while validar_mesa != True:
        print 'Ha dado una mesa no v�lida, reingresela por favor.'
        mesa_electoral = input("Ingrese mesa: ")

        validar_mesa = mesa_valida (mesa_electoral)


    if validar_mesa == True:
        print mesa_electoral

main()
