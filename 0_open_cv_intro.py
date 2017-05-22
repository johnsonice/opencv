#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:24:00 2017

@author: huang
"""

## open cv tutorial
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/dog.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cv2.imwrite('data/testimg.jpg',img) ## save image 
cv2.waitKey(0)
cv2.destroyAllWindows()

#img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.imshow(img_rgb)
