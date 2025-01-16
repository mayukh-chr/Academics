import cv2
import numpy as np

#load image
img = cv2.imread('image.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#compute negative
neg = np.invert(img)

cv2.imshow('input image', img)
cv2.imshow('negative image', neg)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('negative_image.jpg', neg)

cv2.destroyAllWindows() 




