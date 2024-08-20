import cv2
import numpy as np
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.float32) / 25
# Apply mean filtering
mean_filtered = cv2.filter2D(img, -1, kernel)
# Apply median filtering
median_filtered = cv2.medianBlur(img, 5)
#Sharpen the image using the Laplacian operator
img = cv2.GaussianBlur(img, (5,5), 0)
sharpened_image2 = cv2.Laplacian(img, cv2.CV_64F)
# Display filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Mean Filtered Image', mean_filtered)
cv2.imshow('Median Filtered Image', median_filtered)
cv2.imshow('laplacian Image', sharpened_image2)
# Wait for user input
cv2.waitKey(0)
# Destroy all windows
cv2.destroyAllWindows()
