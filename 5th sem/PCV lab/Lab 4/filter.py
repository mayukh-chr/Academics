import cv2
import numpy as np
img = cv2.imread('hehe.jpg', cv2.IMREAD_GRAYSCALE)
img_noisy = cv2.imread('hehe_noisy.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5))/25

mean_filtered = cv2.filter2D(img_noisy, -1, kernel)


median_filtered = cv2.medianBlur(img_noisy, 5)


img_noisy = cv2.GaussianBlur(img_noisy, (5,5), 0)


sharpened_image2 = cv2.Laplacian(img, 6)


# Display filtered images
cv2.imshow('Original Image', img_noisy)
cv2.imshow('Mean Filtered Image', mean_filtered)
cv2.imshow('Median Filtered Image', median_filtered)
cv2.imshow('laplacian Image', sharpened_image2)
# Wait for user input
key = cv2.waitKey(0)

# Save the filtered images when 's' key is pressed
if key == ord('s'):
    cv2.imwrite('mean_filtered.jpg', mean_filtered)
    cv2.imwrite('median_filtered.jpg', median_filtered)
    # cv2.imwrite('sharpened_image.jpg', sharpened_image2)
# Destroy all windows
cv2.destroyAllWindows()