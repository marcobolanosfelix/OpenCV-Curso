# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:57:40 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = np.zeros(shape=(500,500,3), dtype=np.int16) # Crea una imagen de (500x500,RGB) color negro por que 
                                                        # solo hay ceros.
print(imagen.shape)

# Crea un rectángulo de color rojo con coordenadas (20,20) y (100,100), y un contorno de 5 dentro de imagen.
cv2.rectangle(imagen, pt1=(20,20), pt2=(100,100), color=(255,0,0), thickness=5)

# Crea un círculo de color verde con coordenadas (250,250) en el centro, radio de 100 y contorno de 5 dentro 
# de imagen.
cv2.circle(imagen, center=(250,250), radius=100, color=(0,255,0), thickness=10)

# Crea una línea de color azul con coordenadas (0,400) y (500,400), y contorno de 7 dentro de imagen.
cv2.line(imagen, pt1=(0,400), pt2=(500,400), color=(0,0,255), thickness=7)

plt.imshow(imagen)
