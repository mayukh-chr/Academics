import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
neg = cv2.bitwise_not(gray) 



height, width = img.shape[:2]
gheight, gwidth = gray.shape[:2]

# blue, green, red  = img[x,y,0], img[x,y,1], img[x,y,2]

print(img.shape)
print(gray.shape)

print(f"image size: {height}, {width}")
print(f"greyscale image size: {gheight}, {gwidth}")

# print(blue, green ,red)

cv2.imshow('Input Image', img)
cv2.imshow('Grey image', gray)  
cv2.imshow('Negative Image', neg) 
key = cv2.waitKey(0) 
if key == ord('s'): 
    cv2.imwrite('Lab 1/negative_image.jpg', neg) 
    cv2.imwrite('Lab 1/gray_image.jpg', gray) 
    
cv2.destroyAllWindows()