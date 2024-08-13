import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(20,20))

# Read and convert image to grayscale
img = cv2.imread('Lab 3/image.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Plot original grayscale image
plt.subplot(221)
plt.title('Original Grayscale')
plt.imshow(img_gray, cmap='gray')

# Calculate and plot histogram of original grayscale image
hist_original = cv2.calcHist([img_gray],[0],None,[256],[0,256])
plt.subplot(223)
plt.title('Histogram 1 (Original)')
plt.plot(hist_original)
plt.xlim([0,256])

# Equalize histogram
img_equalized = cv2.equalizeHist(img_gray)

# Plot equalized image
plt.subplot(222)
plt.title('Equalized Image')
plt.imshow(img_equalized, cmap='gray')

# Calculate and plot histogram of equalized image
hist_equalized = cv2.calcHist([img_equalized],[0],None,[256],[0,256])
plt.subplot(224)
plt.title('Histogram 2 (Equalized)')
plt.plot(hist_equalized)
plt.xlim([0,256])

plt.tight_layout()
plt.show()


