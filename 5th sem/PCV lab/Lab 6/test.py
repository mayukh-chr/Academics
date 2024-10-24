import cv2

img1 = cv2.imread('book1.jpg', cv2.IMREAD_GRAYSCALE)  
img2 = cv2.imread('table1.jpg', cv2.IMREAD_GRAYSCALE)
# convert images to grayscale
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

k1, d1 = sift.detectAndCompute(img1, None)
k2, d2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(d1, d2)

matches = sorted(matches, key= lambda x : x.distance)

matched_img = cv2.drawMatches(img1, k1, img2, k2, matches[:50], img2, flags=2)

cv2.imshow("matched", matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()