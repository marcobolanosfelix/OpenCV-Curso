# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:04:55 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('img\\coca1.jpeg', 0) # Imagen en escala de grises.
#plt.imshow(imagen, cmap='gray')

mitad, imagen = cv2.threshold(imagen, 255/2, 255, cv2.THRESH_BINARY) # Muestra el umbral de imagen.
plt.imshow(imagen, cmap="gray")


