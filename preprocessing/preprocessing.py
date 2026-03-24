import cv2
import numpy as np
image=cv2.imread("indra.jpeg")
if image is not None:
    gaussian=cv2.GaussianBlur(image,(7,7),9)
    median=cv2.medianBlur(image,11)
    sharpen_kernel=np.array([[0,-1,0],
                             [-1,5,-1],
                             [0,-1,0]])
    sharpened=cv2.filter2D(image,-1,sharpen_kernel)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    enhanced=cv2.equalizeHist(gray)
    cv2.imshow("1. Original Image",image)
    cv2.imshow("2 Gaussian Blur",gaussian)
    cv2.imshow("3 Median Blur",median)
    cv2.imshow("4 sharpene",sharpened)
    cv2.imshow("5 Enhanced ", enhanced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")