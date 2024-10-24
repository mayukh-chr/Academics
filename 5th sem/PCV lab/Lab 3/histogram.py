import cv2

import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('original.jpg')
desaturated_image = cv2.imread('desaturated.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
desaturated_gray_image = cv2.cvtColor(desaturated_image, cv2.COLOR_BGR2GRAY)

# Plot the original image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# Plot the desaturated image
plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(desaturated_image, cv2.COLOR_BGR2RGB))
plt.title('Desaturated Image')

# Plot the histogram of the original image
plt.subplot(2, 2, 3)
plt.hist(gray_image.ravel(), bins=256, color='gray')
plt.title('Histogram of Original Image')

# Plot the histogram of the desaturated image
plt.subplot(2, 2, 4)
plt.hist(desaturated_gray_image.ravel(), bins=256, color='gray')
plt.title('Histogram of Desaturated Image')

# Show the plots
plt.tight_layout()
plt.show()