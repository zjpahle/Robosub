import serial
import struct
import time
import datetime
import log
import math
import numpy

####################################################
#global sensor data
#errors
data_err = 0

#time
timer = 0
timer_old = time.time()

#theta data
magdata = [0,0,0]
magset = [0,0,0]
gyrodata = [0,0,0]
theta = [0,0,0]
gyrotheta = [0,0,0]
gyrodata = [0,0,0]

#position data
acceldata = [0,0,0]
vel = [0,0,0]
position = [0,0,0]
####################################################

def serial_init():
	global ser2
	
	IMUdevice = '/dev/ttyUSB0' #IMU
	ser2 = serial.Serial(IMUdevice, 115200, timeout=1)

def IMU_init():		# sda-->a4	scl-->a5
	global magdata
	global magset
	global acceldata
	global gyrotheta

	log.store('initializing IMU')
	rawdata = ser2.readline()
	#check to see if data coming in is numerical
	trooth = True
	while trooth:
		rawdata = ser2.readline().strip('\r\n').split(':') #reads in data, delimit around ':'
		log.store(rawdata[0])
		if rawdata[0].strip('-').isdigit(): #check to see if data is numerical
			trooth = False
			log.store('Successfully Initialized')
	for x in range(0,300):	
		IMU_get_data(False)
		print gyrotheta
	gyrotheta = [0,0,0]
	magset = magdata	

def IMU_get_pressure():
	global data_err
	global pressuredata
	
	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'
	try:
		pressuredata = 5./1024.*float(data[9]) #grab the first 3 values (magnetometer)
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	except(IndexError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	log.store('pressure = '+str(pressuredata))
	return pressuredata

def IMU_get_data(logging):
	
	global timer
	global timer_old
	global vel
	global position
	global timer_delta
	global data_err
	global theta
	global gyrotheta
	global acceldata
	global gyrodata
	global magdata
	global accel_g

	rawdata = ser2.readline()
	timer = time.time()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'
	if (logging is True): log.store(data)#change to match all data
	
	try:
		magdata = [float(data[x]) for x in [0,1,2]]
		gyrodata = [float(data[x])/1400*90 for x in [3,4,5]]
		#1632 is the conversion from miles/sec^2 to meters/sec^2
		acceldata = [float(data[x])/1632 for x in [6,7,8]]
		pressuredata = float(data[9])

		#data wrangling
		if (gyrodata < .2):
			gyrodata = .0
		if (acceldata < .5):
			acceldata = .0
		magdata = [magdata[x]-magset[x] for x in range(0,3)]	

	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	except(IndexError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))

	#gravity compensation
	gx = math.sin(numpy.deg2rad(gyrodata[0]))*9.8
	gy = math.sin(numpy.deg2rad(gyrodata[1]))*9.8
	xyratio = math.cos(numpy.deg2rad(2*gyrodata[0]))+math.cos(numpy.deg2rad(2*gyrodata[1]))
	gz = .707106*math.sqrt(math.fabs(xyratio))*9.8
	accel_g = [gx,gy,gz]
	acceldata = [acceldata[x] - accel_g[x] for x in range(0,3)]
	timer_delta = round(timer-timer_old,2)
	vel = [vel[x] + (acceldata[x] * timer_delta) for x in range(0,3)]
	position = [position[x] + (vel[x] * timer_delta) for x in range(0,3)]
	gyrotheta = [gyrotheta[x] + gyrodata[x] * timer_delta for x in range(0,3)]

	timer_old = timer

def IMU_log_rawdata():
	
	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'
	try:
		floatdata = [float(data[x]) for x in range(0,len(data))]
		log.store(floatdata)
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))

serial_init()
IMU_init()
timer_old =  time.time()
timer = time.time()

while 1:
	IMU_get_data(False)
	#print magdata, gyrodata
	#print [round(magdata[x],3)for x in range(0,3)], [round(gyrotheta[x],3)for x in range(0,3)]
	print [round(gyrotheta[x],2)for x in range(0,3)]
	#print [round(vel[x],3)for x in range(0,3)], [round(position[x],3)for x in range(0,3)]
	#print round(timer_delta,5)
	#print [round(acceldata[x],3)for x in range(0,3)]
