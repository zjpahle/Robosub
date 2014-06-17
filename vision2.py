import numpy as np
import cv2
import datetime

def init_video():
	global cap
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
			ORANGE_MIN = np.array([5, 50, 50],np.uint8)
			ORANGE_MAX = np.array([15, 255, 255],np.uint8)
			hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
			frame = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
			kernel = np.ones((5,5),np.uint8)
			opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
			closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
			#contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
			#cv2.drawContours(frame,contours,1,(0,255,0),3)
			cv2.imshow('frame',closing)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()

init_video()
test_stream()
