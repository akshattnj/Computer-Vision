import cv2

img = cv2.imread('pyimage.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret , th1 = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
ret , th2 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

ret , th1_inv = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
ret , th2_inv = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)


cv2.imshow('original',img)
cv2.imshow('Threshold',th1)
cv2.imshow('Threshold_inv',th1_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()