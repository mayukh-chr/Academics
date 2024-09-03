import numpy as np
import cv2
img = cv2.imread('puppy.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv2.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
cv2.imshow('img', sheared_img)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('sheared.jpg', sheared_img)
cv2.destroyAllWindows()