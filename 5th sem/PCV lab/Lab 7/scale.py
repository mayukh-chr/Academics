import numpy as np
import cv2
img = cv2.imread('puppy.jpg', 0)

rows, cols = img.shape

img_shrinked = cv2.resize(img, (800,800),
interpolation=cv2.INTER_AREA)
cv2.imshow('img', img_shrinked)
img_enlarged = cv2.resize(img_shrinked, None,
fx=1.5, fy=1.5,
interpolation=cv2.INTER_CUBIC)

cv2.imshow('Original Image', img) 
cv2.imshow('img', img_enlarged)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('scaled.jpg', img_enlarged)
cv2.destroyAllWindows()