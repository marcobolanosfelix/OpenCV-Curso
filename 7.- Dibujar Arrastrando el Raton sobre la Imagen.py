# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:30:53 2020

@author: Marco
"""

import numpy as np
import cv2

# Variables globales.
dibujando = False
valorX = 0
valorY = 0

# Definimos nuestra función para dibujar.
def dibujar(event, x, y, etiquetas, parametros):
    global dibujando, valorX, valorY
    
    if event == cv2.EVENT_LBUTTONDOWN: # Si pulsamos el botón izquierdo.
        dibujando = True
        valorX = x
        valorY = y
    elif event == cv2.EVENT_MOUSEMOVE: # Mientras movemos el ratón.
        if dibujando == True:
            cv2.rectangle(imagen, (valorX, valorY), (x,y), (255,0,0), -1)
    elif event == cv2.EVENT_LBUTTONUP: # Si soltamos el botón izquierdo.
        dibujando = False        
        cv2.rectangle(imagen, (valorX, valorY), (x,y), (255,0,0), -1)
        
        
# Conectamos la imagen con la función dibujar.
cv2.namedWindow(winname="mi_imagen")
cv2.setMouseCallback("mi_imagen", dibujar)        
        

# Mostrar la imagen donde vamos a dibujar.
imagen = np.zeros((500,500,3), np.int8)

while True:
    cv2.imshow("mi_imagen", imagen)
    if cv2.waitKey(10) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()    