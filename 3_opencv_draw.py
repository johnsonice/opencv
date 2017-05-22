#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:16:22 2017

@author: huang
"""

#### open cv draw boxes 

import numpy as np
import cv2 

img = cv2.imread('data/dog.jpg',1)

## draw rectangle
start = (10,10)
end = (100,100)
color = (0,255,0)  ## this is BGR
width = 5
cv2.rectangle(img,start,end,color,width)

## draw polylines
path = np.array([[10,5],[200,200],[400,300],[100,200]],np.int32)
cv2.polylines(img,[path],True,color,width)

font = cv2.FONT_HERSHEY_SIMPLEX
pos = (100,200)
size = 1
thick = 2
cv2.putText(img,'opencv_text',pos,font,size,color,thick,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

