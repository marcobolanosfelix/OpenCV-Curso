# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:51:31 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = np.zeros(shape=(500,500,3), dtype=np.int16)
fuente = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(imagen, text="Hola", org=(20,100), fontFace=fuente, fontScale=3, color=(0,255,0), thickness=5,
            lineType=cv2.LINE_AA)
#plt.imshow(imagen)

vertices = np.array([ [100,300], [300,200], [400,400], [200,400] ], dtype=np.int32)
puntos = vertices.reshape(-1,1,2)
cv2.polylines(imagen, [puntos], isClosed=True, color=(255,255,255), thickness=7)
plt.imshow(imagen)
