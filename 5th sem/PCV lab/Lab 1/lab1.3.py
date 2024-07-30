# importing the module 
import cv2 

# reading the video 
source = cv2.VideoCapture("C:/Users/Student/Documents/90198/CV lab/video.mp4") 

# running the loop 
while True: 

	# extracting the frames 
	ret, img = source.read() 
	
	# converting to gray-scale 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

	# displaying the video 
	cv2.imshow("Live", gray) 

	# exiting the loop 
	key = cv2.waitKey(1) 
	if key == ord("q"): 
		break
	print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(source.get(cv2.CAP_PROP_FRAME_WIDTH))) 
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(source.get(cv2.CAP_PROP_FRAME_HEIGHT))) 
print("CAP_PROP_FPS : '{}'".format(source.get(cv2.CAP_PROP_FPS))) 
print("CAP_PROP_POS_MSEC : '{}'".format(source.get(cv2.CAP_PROP_POS_MSEC))) 
print("CAP_PROP_FRAME_COUNT  : '{}'".format(source.get(cv2.CAP_PROP_FRAME_COUNT))) 
print("CAP_PROP_BRIGHTNESS : '{}'".format(source.get(cv2.CAP_PROP_BRIGHTNESS))) 
print("CAP_PROP_CONTRAST : '{}'".format(source.get(cv2.CAP_PROP_CONTRAST))) 
print("CAP_PROP_SATURATION : '{}'".format(source.get(cv2.CAP_PROP_SATURATION))) 
print("CAP_PROP_HUE : '{}'".format(source.get(cv2.CAP_PROP_HUE))) 
print("CAP_PROP_GAIN  : '{}'".format(source.get(cv2.CAP_PROP_GAIN))) 
print("CAP_PROP_CONVERT_RGB : '{}'".format(source.get(cv2.CAP_PROP_CONVERT_RGB))) 
# closing the window 
cv2.destroyAllWindows() 
source.release()
