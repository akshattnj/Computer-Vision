import cv2

img = cv2.imread("C:/Users/akshat/Desktop/ML/cv2/cv2WS/ImageBasics/pikachu.jpeg")
print("image read")

# print("size of image is", img.shape)
# imres=cv2.resize(img,(40,70))
# cv2.imshow("imresize",imres)
# cv2.imshow("pikachu", img)
# cv2.waitKey(0)
b, g, r = cv2.split(img)
cv2.imwrite('b.jpg', b)
cv2.imwrite('g.jpg', g)
cv2.imwrite('r.jpg', r)
