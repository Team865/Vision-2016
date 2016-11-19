import cv2
#set to work with opencv 3.1.0
import numpy as np
#set to work with the latest version on numpy
cam = cv2.VideoCapture(0)

while(True):
	#gets frame input
	_, frame = cam.read()
	
	#switches to hsv
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#lowest and highest hsv values
	lower = np.array([84, 20, 0])
	upper = np.array([122, 63, 72])
	
	#gaussian blur
	hsv = cv2.GaussianBlur(hsv, (5,5), 0)
	
	#isolating the pixels 
	mask = cv2.inRange(hsv, lower, upper)
	
	#finding the contours
	img2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	#sorts the contours from smallest to largest 
	for i in range(1, len(contours)):
		val = contours[i]
		j = i - 1
		while( j >= 0) and (contours[j] > val):
			contours[j+1] = contours[j]
			j -= 1
		contours[j +1] = val
	
	#next part is to go through the sorted contour list and find the largest one that meets its critieria
	# it would look something like 
       '''for i in reversed(range(len(contours))):
		if( meet criteria):
			shape = contrours[i]
			break
		else:
			continue
		break
	 res = cv2.drawContours(mask, shape, 0, (0,255,0),3)
	'''	
cam.release()   
