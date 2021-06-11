import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

background = 0

for i in range(0,30):
    ret, background = cap.read()
#cap.release()
print("Background captured")

#cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #frame = np.flip(imgaxis=1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2
    mask2 = cv2.bitwise_not(mask)
    #res = cv2.bitwise_and(frame, frame, mask = mask)
    res1 = cv2.bitwise_and(background, background, mask = mask)
    res2 = cv2.bitwise_and(frame, frame, mask = mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)


    cv2.imshow("Mask", mask)
    cv2.imshow("Mask2", mask2)
    cv2.imshow("res1", res1)
    cv2.imshow("res2",res2)
    cv2.imshow("INVISIBLE MAN", final_output)
    cv2.imshow("Original Feed", frame)
    #cv2.imshow("Background", background)


    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


'''mask = mask1 + mask2
mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
mask1 = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
mask2 = cv2.bitwise_not(mask1)
res1 = cv2.bitwise_and(frame, frame, mask = mask2)'''