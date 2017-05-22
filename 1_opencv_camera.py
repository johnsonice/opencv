#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:24:00 2017

@author: huang
"""

## open cv tutorial
import cv2
import numpy as np
#import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0) ## 0 is the default camera
                          ## you can also put video in it

while True:
    ret,frame = cap.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('frame2',grey)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
