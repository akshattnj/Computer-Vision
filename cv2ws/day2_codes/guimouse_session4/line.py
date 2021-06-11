# Simple program to draw 2 lines 
import cv2
import numpy as np

# create a black image 500x500 pixels in size
blank_page = np.zeros((500,500,3), np.uint8)

# fill the image with white i.e. 255
blank_page.fill(255)

# draw a blue line from point A to point B 
point_A = (50,70)
point_B = (400, 260)
line_colour = (255,0,0)

cv2.line( blank_page, point_A, point_B, line_colour)

# draw a green line from C to D of thickness 5 pixels
point_C = (100, 100)
point_D = (500,100)
line_colour = (0,255,0)
thickness = 5

cv2.line(blank_page, point_C, point_D, line_colour, thickness)

# Display the lines
cv2.imshow('page', blank_page)
cv2.waitKey(0)
cv2.destroyAllWindows()
