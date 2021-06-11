import cv2 #importing cv2
import numpy as np #importing numpy as np

cap = cv2.VideoCapture(0) #capturing video from webcam by creating a video capture object

while True: #infinite loop
    ret, frame = cap.read() #ret is true/false based on whether there was something to be read

    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('gray',gray)

    k = cv2.waitKey(4) & 0xFF # 0xFF is 11111111 in binary. Doing & makes sure we only get 8 bits

    if k == 27: #27 is the value for esc
        break #break out of the infinite loop

cv2.destroyAllWindows()
cap.release()