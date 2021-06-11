# Simple program to draw different types of lines
import cv2
import numpy as np

# create a black image 500x500 pixels in size
blank_page = np.zeros((500,500,3),np.uint8)
print(blank_page)

# fill the image with white i.e. 255
blank_page.fill(255)

# create a blue line of type LINE_4
cv2.line(blank_page, (20,20),(480,200),(255,0,0),1,cv2.LINE_4)

# create a green line of type LINE_8
cv2.line(blank_page, (20,120),(480,300),(0,255,0),1,cv2.LINE_8)

# create a red line of type LINE_AA
cv2.line(blank_page, (20,220),(480,400),(0,0,255),1,cv2.LINE_AA)

# display
cv2.imshow('page', blank_page)

cv2.waitKey(0)

cv2.destroyAllWindows()
