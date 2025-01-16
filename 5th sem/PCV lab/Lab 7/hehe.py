import cv2
import numpy as np

img = cv2.imread('puppy.jpg')
print(img.shape)
h, w = img.shape[:2]

angle = 30  # Changed angle
M_rot = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
rotated_img = cv2.warpAffine(img, M_rot, (w, h))

scale_factor = 1.2  # Changed scale factor
scaled_img = cv2.resize(rotated_img, None, fx=scale_factor, fy=scale_factor)

M_shear = np.float32([[1, 0, 0], [0, 1, 0]])  # Changed shear parameters
sheared_img = cv2.warpAffine(scaled_img, M_shear, (w,h))

M_trans = np.float32([[1, 0, 50], [0, 1, 30]])  # Changed translation parameters
translated_img = cv2.warpAffine(sheared_img, M_trans, (w, h))



cv2.imshow('Original Image', img)
cv2.imshow('Augmented Image', translated_img)

key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('rotated.jpg', rotated_img)
    cv2.imwrite('scaled.jpg', scaled_img)
    cv2.imwrite('sheared.jpg', sheared_img)
    cv2.imwrite('translated.jpg', translated_img)

cv2.destroyAllWindows()
