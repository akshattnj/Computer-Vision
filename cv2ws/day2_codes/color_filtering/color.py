import cv2 
import numpy as np

img = np.zeros((480,640,3),np.uint8)

while True:
    h = input("Enter h: ")
    s = input("Enter s: ")
    v = input("Enter v: ")
    img[:,:,0] = h
    img[:,:,1] = s
    img[:,:,2] = v
    bgr = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    cv2.imshow('bgr',bgr)
    
    k = cv2.waitKey(0)
   
    if k == 27:
        break