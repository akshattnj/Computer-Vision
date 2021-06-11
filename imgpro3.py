# import computer vision library(cv2) in this code
import cv2

# main code
if __name__ == "__main__":

    # mentioning absolute path of the image
    img_path = "pyimage.jpg"

    # read/load an image
    image = cv2.imread(img_path)

    # show the input image on the newly created image window
    cv2.imshow('image window1', image)

    # detection of the edges
    img_edge = cv2.Canny(image, 100, 200)

    # show the image edges on the newly created image window
    cv2.imshow('image window2', img_edge)
    cv2.waitKey(0)