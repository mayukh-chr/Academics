import cv2
import numpy as np

# Read the input image
img = cv2.imread('puppy.jpg')
h, w = img.shape[:2]

# Rotation
angle = 30  # Changed angle
M_rot = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
rotated_img = cv2.warpAffine(img, M_rot, (w, h))

# Scaling
scale_factor = 1.2  # Changed scale factor
scaled_img = cv2.resize(rotated_img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

# Shearing
M_shear = np.float32([[1, 0.4, 0], [0, 1, 0]])  # Changed shear parameters
sheared_img = cv2.warpAffine(scaled_img, M_shear, (int(w*1.3), int(h*1.3)))

# Translation
M_trans = np.float32([[1, 0, 50], [0, 1, 30]])  # Changed translation parameters
translated_img = cv2.warpAffine(sheared_img, M_trans, (w, h))

# Create a larger window to fit the transformed image
cv2.namedWindow('Augmented Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Augmented Image', 1200, 800)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Augmented Image', translated_img)

# Wait for a key event
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('rotated.jpg', rotated_img)
    cv2.imwrite('scaled.jpg', scaled_img)
    cv2.imwrite('sheared.jpg', sheared_img)
    cv2.imwrite('translated.jpg', translated_img)

# Release the memory and destroy all windows
cv2.destroyAllWindows()
