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
			frame = cv2.GaussianBlur(frame, (5,5), 0)
			hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			orange_min = np.array([5, 100, 100],np.uint8)
			orange_max = np.array([10, 255, 255],np.uint8)
			
			mask = cv2.inRange(hsv_img, orange_min, orange_max)
			kernel = np.ones((5,5),np.uint8)
			opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
			closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
			closing, contours, hierarchy = cv2.findContours(closing,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
			#cv2.drawContours(closing,contours,1,(0,255,0),3)
			#cv2.imshow('frame',frame)
			cv2.imshow('hue',mask)
			cv2.imshow('mask',closing)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()

init_video()
test_stream()
