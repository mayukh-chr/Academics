import cv2
import numpy as np
img = cv2.imread("Lab 3/image.jpg",0)
row, column = img.shape
img1 = np.zeros((row, column), dtype = 'uint8')
min_range = 100
max_range =  200
for i in range (row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = 255
        else:
            img1[i,j] = 0
cv2.imshow('original.jpg', img)
cv2.imwrite('original.jpg', img)
cv2.imshow('slicedimage.jpg', img1)
cv2.imwrite('slicedimage.jpg', img1)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('Lab 3/original.jpg', img)
    cv2.imwrite('Lab 3/sliced.jpg', img1)
cv2.destroyAllWindows()