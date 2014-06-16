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
			out.write(frame)
			cv2.imshow('frame',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	cap.release()
	cv2.destroyAllWindows()


init_video()
video()

