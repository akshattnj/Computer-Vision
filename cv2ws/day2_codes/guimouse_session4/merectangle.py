# draw rectangle with the mouse
import cv2
import numpy as np

# create a black image 500x500 pixels in size
blank_page = np.zeros((500,500,3), np.uint8)

# fill the image with white i.e. 255
blank_page.fill(255)

#declare 3 extra variables 
top_left_x = 0
top_left_y = 0
is_bottom_right_corner = False

#define a mouse callback function with a FIXED set of arguements
def callback(event, x, y, flag, param):
    global is_bottom_right_corner,top_left_x,top_left_y
    
    if event == cv2.EVENT_LBUTTONDBLCLK and is_bottom_right_corner == False:
    # the mouse double clicked AND we are NOT selecting the bottom right corner

        print('Top left : ',x,y)
        top_left_x = x
        top_left_y = y
        is_bottom_right_corner = True

    elif event == cv2.EVENT_LBUTTONDBLCLK and is_bottom_right_corner == True:
    # the mouse double clicked and we are selecting bottom right corner
        
        print('Bottom right :',x,y)
        cv2.rectangle(blank_page, (top_left_x, top_left_y), (x,y), (0,0,0), 10)
        is_bottom_right_corner = False 

# Create a Window
cv2.namedWindow('page',cv2.WINDOW_AUTOSIZE)  

# Set the callback
cv2.setMouseCallback('page',callback)

# Display Window
while True:
    cv2.imshow('page', blank_page)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()