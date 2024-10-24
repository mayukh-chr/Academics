import cv2
import numpy as np

#read input image
img = cv2.imread('image.jpg')


#perform log operation

c = 255 / np.log(1 + np.max(img)) 
c = 20
log_img = c * (np.log(img + 1)) 

log_img = log_img.astype(np.uint8)

#display 
cv2.imshow('gray image', img)
cv2.imshow('log image', log_img)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('log_image.jpg', log_img)

cv2.destroyAllWindows() 