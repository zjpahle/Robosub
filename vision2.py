import numpy as np
import cv2
import datetime
from subprocess import call

def init_video():
	global cap
	call(["v4l2-ctl", "--set-fmt-video=width=640,height=480,pixelformat=MJPG"])
	call(["v4l2-ctl", "--get-fmt-video"])
	cap = cv2.VideoCapture(0)

def video():
	logname = 'video'+str(datetime.datetime.now().strftime('%H%M%S'))+'.avi'
	out = cv2.VideoWriter('./logs/videos/'+logname,1145656920, 20.0, (640,480))
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret==True:
			frame = cv2.flip(frame,0)
			#out.write(frame)
			cv2.imshow('frame',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()

def test_stream():
	while(cap.isOpened()):
		ret, frame = cap.read()
		
		if ret == True:
			#Convert raw video into smoothed HSV
			flow = cv2.GaussianBlur(frame, (5,5), 0)
			flow = cv2.cvtColor(flow, cv2.COLOR_BGR2HSV)

			#threshold around color value (orange)
			orange_min = np.array([5, 100, 100], np.uint8)
			orange_max = np.array([10, 255, 255], np.uint8)
			flow = cv2.inRange(flow, orange_min, orange_max)

			#open and then close image to reduce noise
			kernel = np.ones((10,10), np.uint8)
			flow = cv2.morphologyEx(flow, cv2.MORPH_CLOSE, kernel)
			#flow = cv2.morphologyEx(flow, cv2.MORPH_OPEN, kernel)

			#finds orange blobs, passes two largest to be drawn on original
			contour_flow = flow
			contours = cv2.findContours(contour_flow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
			cv2.drawContours(frame, contours, len(contours)-1, (0,255,0), 1)
			cv2.drawContours(frame, contours, len(contours)-2, (0,255,0), 1)
			
			'''
			largest_contour = None
			for idx, contour in enumerate(contours):
				largest_contour = contour
				second_largest = contour-2
			'''
			
		#	for idx, new_contour in enumerate(contours)
		#	print type(new_contour)
			
			'''
			#find the center of the two blobs
			if largest_contour is not None:
				print 'largest: ' + str(largest_contour)
				moment = cv2.moments(largest_contour)
				if (moment['m00'] != 0):
					centroid_x = int(moment['m10']/moment['m00'])
					centroid_y = int(moment['m01']/moment['m00'])
					#print centroid_x, centroid_y
					cv2.circle(frame,(centroid_x,centroid_y), 5, (0,255,0), 1)

				print 'second largest: ' + str(second_largest)
				moment = cv2.moments(second_largest)
				if (moment['m00'] != 0):
					centroid_x = int(moment['m10']/moment['m00'])
					centroid_y = int(moment['m01']/moment['m00'])
					#print centroid_x, centroid_y
					cv2.circle(frame,(centroid_x,centroid_y), 5, (0,255,0), 1)
			'''

			#epsilon = 0.1*cv2.arcLength(cnt,True)
			#approx = cv2.approxPolyDP(cnt,epsilon,True)	

			#draw (for user)
			cv2.imshow('frame', frame)
			#cv2.imshow('hue', flow)
			#cv2.imshow('mask', mask)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				#print contours
				break
	cap.release()
	cv2.destroyAllWindows()

init_video()
test_stream()
