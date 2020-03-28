#!/usr/bin/env python
# -*- coding: latin-1 -*-

Recuento de votos
'''Este sistema permite al encargado ingresar datos de telegramas de votos emotidos en la escuela. Ingresará fecha, datos de la esuela y los datos de cada telegrama.'''

Ingreso de fecha
    #Validez de día, mes y año (2015 a 2027 incluídos)
Ingreso de datos de la escuela:
    Número
    Nombre
    Sección electoral
        #Validez entre 1 y 15
    Circuito
        #Validez entre 1 y 167
    
Ingreso de cada telegrama:
    Numero de mesa electoral
        #Validez entre 1 y 7413
    Agrupación o clase de voto: (Diccionario para el conteo)
        Alfa
        Beta
        En Blanco
    Cantidad de votos para la categoría "Jefe de Gobierno" obtenidos en la mesa por agrupación o clase de voto
        #Validez que no supere 350 por cada mesa.

    Que muestre simultáneamente en pantalla todos los datos validados de cada telegrama (mesa, agrupación o clase de voto, categoría, cantidad de votos) a medida que son ingresados.
    Que determine y muestre junto a los datos de la escuela la cantidad total de votos.
    Que deterime y muestre la cantidad de votos obtenidos por cada agrupación y su respectivo porcentaje sobre el total (excluyendo del mismo la cantidad de votos en blancoque serán mostrados aparte.)
    
