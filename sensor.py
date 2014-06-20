import serial
import struct
import time
import datetime
import log
import math

####################################################
#global sensor data
#errors
data_err = 0

#time
timer = 0
timer_old = time.time()

#theta data
magdata = [0,0,0]
gyrodata = [0,0,0]
gyro_old = [0,0,0]
theta = [0,0,0]

#position data
acceldata = [0,0,0]
accel_old = [0,0,0]
accel_delta = [0,0,0]
vel = [0,0,0]
vel_old = [0,0,0]
vel_delta = [0,0,0]
position = [0,0,0]
####################################################
def serial_init():
	global ser2
	IMUdevice = '/dev/ttyUSB1' #IMU
	ser2 = serial.Serial(IMUdevice, 115200, timeout=1)

def IMU_init():		# sda-->a4	scl-->a5
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
	global gyrodata
	global gyro_old
	global theta
	
	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'
	try:
		gyrodata = [float(data[x]) for x in [3,4,5]] #grab the first 3 values (magnetometer)
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	theta = [theta[x] + (gyro_old[x]-gyrodata[x]) for x in range(0,3)]
	gyro_old = gyrodata
	log.store(theta)
	#return magdata
'''
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
'''

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
	global time_delta

	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'

	try:
		#1632 is the conversion from miles/sec^2 to meters/sec^2
		acceldata = [float(data[x])/1632 for x in [3,4,5]] #grab the second 3 value (Accelerometers)
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	if (logging is True): log.store(acceldata)
	

	
	'''
	accel_delta[0] = accel_old[0]-acceldata[0]
	accel_old[0] = acceldata[0]
	vel[0] = vel[0] + accel_delta[0]

	vel_delta[0] = vel_old[0]-vel[0]
	vel_old[0] = vel[0]
	position[0] = position[0] + vel_delta[0]


	accel_delta = [accel_old[x]-acceldata[x] for x in range(0,3)]
	accel_old = acceldata
	vel = [vel[x] + accel_delta[x] for x in range(0,3)]

	vel_delta = [vel_old[x]-vel[x] for x in range(0,3)]
	vel_old = vel
	position = [vel[x] + vel_delta[x] for x in range(0,3)]

	'''	
	return position
'''
def whateverYouWant(logging):
	
	global acceldata
	global magdata
	
	rawdata=ser2.readline()
	data = rawdata.strop('\r\n').split(':')
	
	try:
	acceldata = [float(data[x])/1632 for x in [6,7,8]]
	magdata = [float(data[x]) for x in [0,1,2]
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	if (logging is True): log.store(acceldata)
	
	magdataRad=math.pi/180*[magdata[x] for x in range(0,3)]
	phi=magdataRad[0]
	theta=magdataRad[2]
	gravStan=9.806

	accelDue2Grav=[0,0,0]
	
	accelDue2Grav[0]=
	'''
	


	
def integrate(logging):
	
	global timer
	global acceldata
	global timer_old
	global accel_old
	global accel_delta
	global vel
	global vel_old
	global position
	global timer_delta


	rawdata = ser2.readline()
	data = rawdata.strip('\r\n').split(':') #reads in data, delimits around ':'
	
	try:
		#1632 is the conversion from miles/sec^2 to meters/sec^2
		acceldata = [float(data[x])/1632 for x in [6,7,8]] #grab the second 3 value (Accelerometers)
		# divide by 1632
	except(ValueError):
		data_err = data_err+1
		log.store('Error Count = '+str(data_err))
	if (logging is True): log.store(acceldata)

	timer_delta = timer-timer_old
	accel_delta = [acceldata[x] - accel_old[x] for x in range(0,3)]
	#accel_delta=[round(accel_delta[x],3) for x in range(0,3)]
	vel = [vel[x] + (accel_delta[x] * timer_delta) for x in range(0,3)]
	vel_delta = [vel[x] - vel_old[x] for x in range(0,3)]
	#vel_delta =[round(vel_delta[x],3) for x in range(0,3)]
	position = [position[x] + (vel_delta[x] * timer_delta) for x in range(0,3)]

	timer_old = timer
	timer = time.time()
	accel_old = acceldata
	vel_old = vel
	return vel, acceldata
'''
serial_init()
IMU_init()
timer = time.time()
timer_old =  time.time()
while 1:
	test, timer_delta= integrate(False)
	global position_old
	print [round(test[x],3)for x in range(0,3)], [round(acceldata[x],3)for x in range(0,3)]

	#print [round(vel[x],3)for x in range(0,3)], [round(position[x],3) for x in range(0,3)]
'''
