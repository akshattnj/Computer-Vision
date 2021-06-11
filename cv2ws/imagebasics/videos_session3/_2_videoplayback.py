import cv2
import numpy as np

cap = cv2.VideoCapture('Resources/videoplayback.mp4')

fps = 0


if cap.isOpened(): #capture object should be opened
    fps = cap.get(cv2.CAP_PROP_FPS) #get fps
print(fps)

while cap.isOpened():
    ret, frame = cap.read()

    if ret == False: #nothing left to read
        break

    
    cv2.imshow('frame', frame)

    if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()