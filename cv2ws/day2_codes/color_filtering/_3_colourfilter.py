import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read() #read frames
	#convert to hsv color space
	hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	
	#range
	lower = np.array([100,100,100])
	upper = np.array([140,200,200])
	
	mask = cv2.inRange(hsv_frame,lower,upper) #thresholding
	
	res = cv2.bitwise_and(frame,frame,mask = mask) #bitwse and
	
	cv2.imshow('frame',frame)
	#cv2.imshow('hsv',hsv_frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	
	k = cv2.waitKey(1) & 0xff
	
	if k == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
