import numpy as np
import cv2

img = np.zeros((400, 400, 3), dtype="uint8")
cv2.line(img, (20, 160), (100, 160), (0, 0, 255), 10)
cv2.circle(img, (200, 200), 80, (255, 0, 0), 3)
cv2.rectangle(img, (30, 30), (300, 200), (0, 255, 0), 5)
cv2.imshow('dark', img)

# Allows us to see image
# untill closed forcefully
cv2.waitKey(0)
cv2.destroyAllWindows()
