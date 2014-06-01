from SimpleCV import *
import datetime

def init():
	global location
	global cam1
	cam1 = Camera()
	location = './logs/pictures/picture'+str(datetime.datetime.now().strftime('%H%M%S'))+'.jpg'

def picture():
	cam1.getImage().save(location)

#init()
#picture(location)
