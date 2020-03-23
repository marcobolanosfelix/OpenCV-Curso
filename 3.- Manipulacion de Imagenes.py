# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:14:56 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('img\\coca1.jpeg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagen = cv2.resize(imagen, (600, 800)) # Reajusta el tamaño.
ratio_ancho = 0.5
ratio_alto = 0.5
imagen = cv2.resize(imagen, (0,0), imagen, ratio_ancho, ratio_alto) # Reajusta la imagen con diferentes parámetros.
imagen = cv2.flip(imagen, 1) # Invierte la imagen de derecha a izquierda o viceversa.
imagen = cv2.flip(imagen, 0) # Invierte la imagen de arriba a abajo o viceversa.
cv2.imwrite("img\\coca_al_reves.jpeg", imagen) # Escribe la imagen modificada.

plt.imshow(imagen)