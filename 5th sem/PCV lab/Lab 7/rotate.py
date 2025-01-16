import cv2 

img = cv2.imread('puppy.jpg') 

angle = 45 

h, w = img.shape[:2] 

M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)

rotated_img = cv2.warpAffine(img, M, (w, h)) 

cv2.imshow('Original Image', img) 

cv2.imshow('Rotated Image', rotated_img) 


key = cv2.waitKey(0) 
if key == ord('s'):
    cv2.imwrite('rotated.jpg', rotated_img)
# Release the memory and destroy all windows 
cv2.destroyAllWindows()