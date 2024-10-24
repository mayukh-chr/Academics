import cv2
import numpy as np

img = cv2.imread('image.jpg')

kernel = np.ones((5,5),np.float32)/25

print(kernel)
mean = cv2.filter2D(img, -1, kernel)

median = cv2.medianBlur(img, 5)

gauss = cv2.GaussianBlur(img, (5,5), 0)

lablace = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow("mean,", mean)

cv2.waitKey(0)

cv2.destroyAllWindows()