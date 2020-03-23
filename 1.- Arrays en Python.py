# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:55:33 2020

@author: Marco
"""

import numpy as np

lista = [1,2,3]
array = np.array(lista)

#print("Numero:", array[1])

print("1.- ",np.arange(0, 20),"\n") # Crea una secuencia de números del 0 al 20.
print("2.- ",np.arange(0, 30, 2),"\n") # Crea una secuencia de números del 0 al 30, de 2 en 2.

print("3.- ",np.zeros(shape=(10,2)),"\n") # Crea una matriz de ceros, de 10 filas por 2 columnas.

print("4.- ",np.ones(shape=(10,2)),"\n") # Crea una matriz de unos, de 10 filas por 2 columnas.

aleatorios = np.random.randint(0,100,50) # Crea 50 números del 0 al 100.
print("5.- ",aleatorios,"\n")
print("6.- Posición del Máximo: ",aleatorios.argmax(),"\n") # Toma la posición del valor máximo de aleatorios.
print("7.- Valor Máximo: ", aleatorios.max(), "\n") # Toma el valor máximo de aleatorios.
print("8.- Valor Mínimo: ", aleatorios.min(), "\n") # Toma el valor mínimo de aleatoeios.

print("9.- Dimensión: ", aleatorios.shape, "\n") # La variable es de 50 filas por 1 columna (el 1 no se muestra).
aleatorios = aleatorios.reshape(10,5) # Cambia la variable a 10 filas por 5 columnas.
print("10.- ", aleatorios, "\n") 
print("11.- ", aleatorios[5,4], "\n") # Toma el valor de la posición [5,4] de la variable.


