# Simple program to draw a circle
import cv2
import numpy as np

# create a black image 500x500 pixels in size
blank_page = np.zeros((500,500,3), np.uint8)

# fill the image with white i.e. 255
blank_page.fill(255)

# Draw a red circle in the middle of the blank_page of Arbitrary radius
centre =  (250, 250)
radius = 150
colour = (0,0,255)
thickness = 20

cv2.circle(blank_page, centre, radius, colour, thickness)

#draw another concentric circle filled in with black
centre =  (250, 250)
radius = 70
colour = (0,0,0)
thickness = -1           # if given -1 it WILL fill in the shape. 

cv2.circle(blank_page, (250, 250), radius, colour, thickness)

#display the circles
cv2.imshow('page', blank_page)
cv2.waitKey()
cv2.destroyAllWindows()