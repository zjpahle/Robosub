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

#calibrate camera
#################

#################

#wait to start
#time.sleep(60)

#find gate
print vision2.find_gate()[0]
if vision.find_gate()[0]>0:
	while vision2.find_gate() > 1:
		robot.motor.power(1, 100, True)
		robot.motor.power(2, -100, True)
	robot.motor.power(1, 0, True)
	robot.motor.power(2, 0, True)

if vision.find_gate()[0]<0:
	while vision2.find_gate() < -1:
		robot.motor.power(1, -100, True)
		robot.motor.power(2, 100, True)
	robot.motor.power(1, 0, True)
	robot.motor.power(2, 0, True)
