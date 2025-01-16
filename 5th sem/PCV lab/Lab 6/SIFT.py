import cv2

# read the images
img1 = cv2.imread('book1.jpg')  
img2 = cv2.imread('table1.jpg')
# convert images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# create SIFT object
sift = cv2.SIFT_create()
# detect SIFT features in both images
keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

# print the number of keypoints detected in each image
print(f"Number of keypoints in image 1: {len(keypoints_1)}")
print(f"Number of keypoints in image 2: {len(keypoints_2)}")

# create feature matcher
bf = cv2.BFMatcher(2, crossCheck=True)
# match descriptors of both images
matches = bf.match(descriptors_1, descriptors_2)

# sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)
# draw first 50 matches
matched_img = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)

# show the image
cv2.imshow('image', matched_img)
# save the image
cv2.imwrite("matched_images.jpg", matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
