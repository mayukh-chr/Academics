import cv2

# Load the image (replace 'image.jpg' with the actual image file path)
image = cv2.imread("image2.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=10, threshold2=60)

# Display the Canny edge-detected image
cv2.imshow("Canny Edge Detection", edges)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('original.jpg', image)
    cv2.imwrite('processed.jpg', edges)
cv2.destroyAllWindows()
