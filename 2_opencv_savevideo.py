#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:24:00 2017

@author: huang
"""

## open cv tutorial
import cv2
import numpy as np
from time import time as timer
import sys
#import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0) ## 0 is the default camera
                          ## you can also put video in it

#cv2.namedWindow('', 0)
_, frame = cap.read()
fps = cap.get(cv2.CAP_PROP_FPS)
height, width, _ = frame.shape
print(height,width)
cv2.resizeWindow('', width,height)  ## height and width has to match camera input

fourcc = cv2.VideoWriter_fourcc(*'MJPG')  ## i can only make MJPG work in ubuntu 
out = cv2.VideoWriter('data/video.avi', fourcc, 20.0, (width,height)) #
while True:
    ret,frame = cap.read()
    #grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #fps = cap.get(3)
    #sys.stdout.write('\r' + str(fps))
    #sys.stdout.flush()
    start = (200,200)
    end = (400,400)
    color = (0,255,0)  ## this is BGR
    width = 5
    cv2.rectangle(frame,start,end,color,width)
    
    out.write(frame)
    cv2.imshow('frame',frame)
    #cv2.imshow('frame2',grey)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

        
