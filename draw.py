import cv2


img = cv2.imread("flower.jpg")


def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_RBUTTONDOWN:
        print("hello")
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)


cv2.namedWindow(winname="Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_circle)

while True:
    cv2.imshow("Title of Popup Window", img)

    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
