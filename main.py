#####################################
#Robosub Competition Code
#main.py
#Revision 2.0
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

robot.log.init()
robot.motor.serial_init()
robot.sensor.serial_init()
robot.sensor.IMU_init()

vision2.video
'''
#time.sleep(60)
init_time = time.time()
current_time = time.time()-init_time
while(current_time<=(10)):
	robot.sensor.IMU_get_data()
	current_time = time.time()-init_time
init_time = time.time()
robot.motor.power(3,100, True)
robot.motor.power(4,100, True)
while(current_time<=(10)):
	robot.sensor.IMU_get_data()
	current_time = time.time()-init_time
init_time = time.time()
current_time = 0
robot.motor.power(1,-100, True)
robot.motor.power(2,-100, True)
while(current_time<=(10)):
	robot.sensor.IMU_get_data()
	current_time = time.time()-init_time
init_time = time.time()
current_time = 0
'''
