import cv2
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))

img = cv2.imread('seeds.jpg', cv2.IMREAD_GRAYSCALE)

plt.subplot(221)
plt.title("original")
plt.imshow(img, cmap='gray')

hist_og = cv2.calcHist([img], [0], None, [256], [0,256])

plt.subplot(223)

img_equalised = cv2.equalizeHist(img)
