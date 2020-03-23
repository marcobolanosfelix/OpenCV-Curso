# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:42:27 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('img\\grietas_concreto.jpg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen)

imagen_2 = cv2.imread('img\\grietas_concreto_recortado.jpg')
imagen_2 = cv2.cvtColor(imagen_2, cv2.COLOR_BGR2RGB)
plt.imshow(imagen_2)

metodo = cv2.TM_CCOEFF
resultado = cv2.matchTemplate(imagen, imagen_2, metodo) # Genera un mapa de calor donde resalta donde es parecido.
plt.imshow(resultado)

valor_min, valor_max, pos_min, pos_max = cv2.minMaxLoc(resultado) # Extrae las características de resultado.
alto, ancho, colores = imagen_2.shape # Extrae las características de la imagen_2.

top_izquierda = pos_max
botton_derecha = (pos_max[0]+ancho, pos_max[1]+alto)

cv2.rectangle(imagen, top_izquierda, botton_derecha, (255,0,0), 8)
plt.imshow(imagen)                      
