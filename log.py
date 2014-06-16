import datetime
import vision

name = 'error-notafile'

def init():
	global name
	name = 'vehicle' + str(datetime.datetime.now().strftime("D%m-%d-%yT%H%M")) + '.txt'
	log = open('./logs/'+ str(name),'w+')

def store(data):
	log = open('./logs/'+str(name), 'a')
	log.write(datetime.datetime.now().strftime("%H:%M:%S:%f")+': '+str(data)+'\n')
	print str(data)
    
def video():
	print 'This is hard! I can\'t do it.'

def picture():
	vision.init()
	vision.picture()


#picture()
