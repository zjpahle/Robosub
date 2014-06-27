#####################################
#Robosub Competition Code
#main.py
#Revision 1.3
#May 22nd, 2014
#Maintained by: Zach Pahle
#Contact Email: zjpahle@yahoo.com
#####################################

import robot
import time
import test
import log
import vision2

log_motor = True


#initialize vehicle
robot.log.init()
robot.motor.serial_init()
robot.sensor.serial_init()
robot.sensor.IMU_init()
vision2.init_video()

#calibrate camera
#################
#################

#wait to start
#time.sleep(60)
#find gate
'''
center = vision2.find_center()
while vision2.find_center() is None:
	center = vision2.find_center()
	print type(center)

print type(center)
if center[0]>0:
	while center[0] > 1:
		print center[0]
		robot.motor.power(1, 100, log_motor)
		robot.motor.power(2, -100, log_motor)
		center = vision2.find_center()
	robot.motor.power(1, 0, log_motor)
	robot.motor.power(2, 0, log_motor)

elif center[0]<0:
	while center[0] < -1:
		print center
		robot.motor.power(1, -100, log_motor)
		robot.motor.power(2, 100, log_motor)
		center[0] = vision2.find_center()
	robot.motor.power(1, 0, log_motor)
	robot.motor.power(2, 0, log_motor)
'''
#debubblizeme()
robot.go_straight(10,True)

