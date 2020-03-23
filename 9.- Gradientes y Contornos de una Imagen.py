# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:27:13 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('img\\sudoku.png', 0)
#plt.imshow(imagen, cmap='gray')
sobelX = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=5) # Toma la parte vertical.
sobelY = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=5) # Toma la parte horizontal.
#plt.imshow(sobelY, cmap='gray')
imagen_2 = cv2.addWeighted(src1=sobelX, alpha=0.5, src2=sobelY, beta=0.5, gamma=0) # Mezcla las imagenes anteriores.
#plt.imshow(imagen_2, cmap='gray')

laplacian = cv2.Laplacian(imagen, cv2.CV_64F) # Hace lo mismo que Sobel, pero es Laplaciano.
plt.imshow(laplacian, cmap='gray')
