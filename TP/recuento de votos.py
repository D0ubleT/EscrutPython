#!/usr/bin/env python
# -*- coding: latin-1 -*-

Recuento de votos
'''Este sistema permite al encargado ingresar datos de telegramas de votos emotidos en la escuela. Ingresar� fecha, datos de la esuela y los datos de cada telegrama.'''

Ingreso de fecha
    #Validez de d�a, mes y a�o (2015 a 2027 inclu�dos)
Ingreso de datos de la escuela:
    N�mero
    Nombre
    Secci�n electoral
        #Validez entre 1 y 15
    Circuito
        #Validez entre 1 y 167
    
Ingreso de cada telegrama:
    Numero de mesa electoral
        #Validez entre 1 y 7413
    Agrupaci�n o clase de voto: (Diccionario para el conteo)
        Alfa
        Beta
        En Blanco
    Cantidad de votos para la categor�a "Jefe de Gobierno" obtenidos en la mesa por agrupaci�n o clase de voto
        #Validez que no supere 350 por cada mesa.

    Que muestre simult�neamente en pantalla todos los datos validados de cada telegrama (mesa, agrupaci�n o clase de voto, categor�a, cantidad de votos) a medida que son ingresados.
    Que determine y muestre junto a los datos de la escuela la cantidad total de votos.
    Que deterime y muestre la cantidad de votos obtenidos por cada agrupaci�n y su respectivo porcentaje sobre el total (excluyendo del mismo la cantidad de votos en blancoque ser�n mostrados aparte.)
    
