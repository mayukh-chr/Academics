import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("C:/Users/Student/Documents/90198/CV lab/image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
neg = cv2.bitwise_not(gray) 

# cv2.imshow('Input Image', img)
# cv2.imshow('Grey image', gray)  
# cv2.imshow('Negative Image', neg) 

# img = cv.imread('gradient.png', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
 
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
 
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
 
# plt.show()
height, width = img.shape[:2]
gheight, gwidth = gray.shape[:2]

x= input("input x coordinate: ")
y = input("input x coordinate: ")


blue, green, red  = img[x,y,0], img[x,y,1], img[x,y,2]

print(img.shape)
print(gray.shape)

print(f"image size: {height}, {width}")
print(f"greyscale image size: {gheight}, {gwidth}")

print(blue, green ,red)


key = cv2.waitKey(0) 
if key == ord('s'): 
    cv2.imwrite('negative_image.jpg', neg) 
cv2.destroyAllWindows()