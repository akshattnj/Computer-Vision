# Simple program to draw a rectangle 
import cv2
import numpy as np

# create a black image 500x500 pixels in size
blank_page = np.zeros((500,500,3), np.uint8)

# fill the image with white i.e. 255
blank_page.fill(255)

# Draw a rectangle from Corner A to Corner C
corner_A = (100,100)
corner_C = (400,400)
colour = (0,0,0)
thickness = 10

cv2.rectangle(blank_page, corner_A, corner_C, colour, thickness)

# display the rectangle
cv2.imshow('page', blank_page)
cv2.waitKey()
cv2.destroyAllWindows()
