# select points in a blank page using the mouse pointer 
import cv2
import numpy as np

# create a black image 500x500 pixels in size
blank_page = np.zeros((500,500,3), np.uint8)

# fill the image with white i.e. 255
blank_page.fill(255)

#define a mouse callback function with a FIXED set of arguements
def callback(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("the mouse double clicked at : ",x,y)

# Create a Window
cv2.namedWindow('page',cv2.WINDOW_AUTOSIZE)  

# Set the callback
cv2.setMouseCallback('page',callback)

# Display Window
cv2.imshow('page', blank_page)
cv2.waitKey()
cv2.destroyAllWindows()
