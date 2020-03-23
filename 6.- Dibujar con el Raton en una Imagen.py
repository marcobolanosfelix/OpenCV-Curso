# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:14:36 2020

@author: Marco
"""

import numpy as np
import cv2

# Definimos la función para dibujar con el ratón. 
def dibujar(event, x, y, etiquetas, parametros):
    if event == cv2.EVENT_LBUTTONDOWN: # Se pulsa el botón izquierdo del ratón.
        cv2.circle(imagen, (x,y), 50, (255,0,0), -1)
        
        
# Conectamos la imagen con la función dibujar.
cv2.namedWindow(winname="mi_imagen")
cv2.setMouseCallback("mi_imagen", dibujar)

# Mostramos la imagen donde vamos a pintar.
imagen = np.zeros((500,500,3), np.int8)

while True:
    cv2.imshow("mi_imagen", imagen)
    if cv2.waitKey(10) & 0XFF == 27: # Sale del programa con la tecla ESC.
        break
    

cv2.destroyAllWindows()