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

log_motor = True

robot.log.init()
robot.motor.serial_init()
robot.sensor.serial_init()
robot.sensor.IMU_init()

#time.sleep(60)
init_time = time.time()
current_time = time.time()-init_time
while(current_time<=(5*60)):
	robot.sensor.IMU_get_theta()
	current_time = time.time()-init_time

#test.pressuretest()

