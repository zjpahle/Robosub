import serial
import struct
import time
import datetime
import log

######################################
#Desired changes:
#make variables global
#
#
#
######################################
data_err = 0
magdata = [0,0,0]
acceldata = [0,0,0]
accel_old = [0,0,0]
accel_delta = [0,0,0]
vel = [0,0,0]
vel_old = [0,0,0]
vel_delta = [0,0,0]
position = [0,0,0]

def serial_init():
	global ser2
	IMUdevice = '/dev/ttyUSB0' #IMU
	ser2 = serial.Serial(IMUdevice, 115200, timeout=1)

def IMU_init():   # sda-->a4	scl-->a5
	log.store('initializing IMU')
	rawdata = ser2.readline()
	#check to see if data coming in is numerical
	trooth = True
	while trooth:
		rawdata = ser2.readline().strip('\r\n').split(':') #reads in data, delimit around ':'
		log.store(rawdata[0])
		if rawdata[0].strip('-').isdigit(): #check to see if data is numerical
			trooth = False
			log.store('its a number!')

def IMU_get_theta():
	global data_err
	global magdata
	
	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'
	try:
		magdata = [float(data[x]) for x in [0,1,2]] #grab the first 3 values (magnetometer)
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	log.store(magdata)
	return magdata

def IMU_get_accel(logging):
	global data_err
	global magdata
	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'
	global acceldata
	try:
		#1632 is the conversion from miles/sec^2 to meters/sec^2
		acceldata = [float(data[x])/1632 for x in [3,4,5]] #grab the second 3 value (Accelerometers)
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	if (logging is True): log.store(acceldata)
	return acceldata

def IMU_get_pressure():
	global data_err
	global pressuredata
	
	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'
	try:
		pressuredata = float(data[6]) #grab the first 3 values (magnetometer)
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	log.store('pressure = '+str(pressuredata))
	return pressuredata

def IMU_get_position(logging):
	global data_err
	global accel_total
	global accel_old
	global accel_delta
	global acceldata
	global vel
	global vel_old
	global vel_delta
	global position

	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'

	try:
		#1632 is the conversion from miles/sec^2 to meters/sec^2
		acceldata = [float(data[x])/1632 for x in [3,4,5]] #grab the second 3 value (Accelerometers)
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	if (logging is True): log.store(acceldata)
	

	accel_delta[0] = accel_old[0]-acceldata[0]
	accel_old[0] = acceldata[0]
	vel[0] = vel[0] + accel_delta[0]

	vel_delta[0] = vel_old[0]-vel[0]
	vel_old[0] = vel[0]
	position[0] = position[0] + vel_delta[0]

	'''
	accel_delta = [accel_old[x]-acceldata[x] for x in range(0,3)]
	accel_old = acceldata
	vel = [vel[x] + accel_delta[x] for x in range(0,3)]

	vel_delta = [vel_old[x]-vel[x] for x in range(0,3)]
	vel_old = vel
	position = [vel[x] + vel_delta[x] for x in range(0,3)]

	'''	
	return position
