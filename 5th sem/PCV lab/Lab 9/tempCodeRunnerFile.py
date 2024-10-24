import cv2

# Load the input video
cap = cv2.VideoCapture('video.mp4')

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Loop over the frames in the video
while True:
    # Read the current frame
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video Playback', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
