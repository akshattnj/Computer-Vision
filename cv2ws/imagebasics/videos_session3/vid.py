cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while Truee:
_, frame = cap.read()
Cv2.imshow(‘frame’, frame


           K=cv2.waitkey(0)
           If k == 27
           Break
Cv2.destroyAllWindows()
Cap.release
