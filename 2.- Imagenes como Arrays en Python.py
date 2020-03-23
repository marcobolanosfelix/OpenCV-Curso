# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:52:11 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imagen = Image.open('img//coca1.jpeg')
print("1.- Tipo: ",type(imagen), "\n")
print("2.- Tamaño de Imagen: ", imagen.size, "\n") # Tamaño en pixeles (ancho, alto).

array_imagen = np.asarray(imagen) # Convertir imagen a array.
print("3.- Array de Imagen: ",array_imagen, "\n")
print("4.- Dimensión de Imagen: ", array_imagen.shape, "\n")

plt.imshow(array_imagen) # Muestra la imagen en array.
print("5.- Dimensión de Array_Imagen: ", array_imagen.shape, "\n") # Alto, ancho, numero de gama de colores (RGB).

print("6.- Canal de Rojos: ",array_imagen[:,:,0],"\n")
print("7.- Canal de Verdes: ",array_imagen[:,:,1],"\n")
print("8.- Canal de Azules: ",array_imagen[:,:,2],"\n")

                                       

