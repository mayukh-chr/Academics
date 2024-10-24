import cv2
import time

# Load the input video
cap = cv2.VideoCapture('video2.mp4')

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Set the desired frame rate
fps = 10
frame_time = 1 / fps

# Loop over the frames in the video
while True:
    # Record the start time of processing this frame
    start_time = time.time()
    
    # Read the current frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Display the frame
    cv2.imshow('Video Playback', frame)
    
    # Calculate how long to wait
    processing_time = time.time() - start_time
    wait_time = max(1, int((frame_time - processing_time) * 1000))
    
    # Wait and check for 'q' key press
    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()