# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:07:52 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = np.zeros((300,600))
fuente = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen, text='ABCDE', org=(50,200), fontFace=fuente, fontScale=5, color=(255,255,255), thickness=8)
#plt.imshow(imagen, cmap='gray')
nucleo = np.ones((5,5), dtype=np.int8)
imagen_2 = cv2.erode(imagen, nucleo, iterations=1) # Imagen ersionado con nucleo.
#plt.imshow(imagen_2, cmap='gray')

ruido = np.random.randint(low=0, high=2, size=(300,600)) # Crear una imagen con ruido del mismo tamaño que 
                                                                # la anterior.
#plt.imshow(ruido, cmap='gray')

ruido = ruido * 255
imagen_ruido = imagen + ruido
#plt.imshow(imagen_ruido, cmap='gray')

imagen_sin_ruido = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, nucleo) # Elimina el ruido de la imagen anterior.
#plt.imshow(imagen_sin_ruido, cmap='gray')

gradiente = cv2.morphologyEx(imagen, cv2.MORPH_GRADIENT, nucleo) # Elimina relleno de las letras.
plt.imshow(gradiente, cmap='gray')
