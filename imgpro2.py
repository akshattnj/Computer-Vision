import cv2
img = cv2.imread("pyimage.jpg")
height, width = img.shape[0:2]
startRow = int(height*.15)

startCol = int(width*.15)

endRow = int(height*.85)

endCol = int(width*.85)

crop_img = img[startRow:endRow, startCol:endCol]

blur_image = cv2.GaussianBlur(img, (9,9), 0)

cv2.imshow('Original Image', img)

cv2.imshow('Blur Image', blur_image)

cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
