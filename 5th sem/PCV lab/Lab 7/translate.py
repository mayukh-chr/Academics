import numpy as np
import cv2
img = cv2.imread('puppy.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('img', dst)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('translated.jpg', dst)
cv2.destroyAllWindows()