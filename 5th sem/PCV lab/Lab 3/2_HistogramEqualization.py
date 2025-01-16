import cv2
import matplotlib.pyplot as plt

img = cv2.imread("seeds.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.subplot(221)
plt.title("original")
plt.imshow(img, cmap='gray')

oghist = cv2.calcHist([img_gray],[0],None,[256],[0,256])
plt.subplot(223)
plt.title('og hist')
plt.plot(oghist)
plt.xlim([0,256])

img_eq = cv2.equalizeHist(img_gray)

plt.subplot(222)
plt.title("original")
plt.imshow(img_eq, cmap='gray')

eqhist = cv2.calcHist([img_eq],[0],None,[256],[0,256])
plt.subplot(224)
plt.title('eq hist')
plt.plot(eqhist)
plt.xlim([0,256])

plt.tight_layout()
plt.show()