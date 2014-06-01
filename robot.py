import motor
import sensor
import time
import log

move_time = [1,1,1] #amount of distance per second
rot_time = [x/360 for x in [1,1,1]]#am unt of time per degree

def rotate_ol(axis, degrees):
	log.store('Rotate(ol) '+str(degrees)+' along '+str(axis))
	sel_axis = select_axis(axis)[0]	
	motora = select_axis(axis)[1]	
	motorb = select_axis(axis)[2]	
	
	motor.power(motora, 100, True)
	motor.power(motorb,-100, True)
	total_time = degrees/rot_time[sel_axis]
	start_time = time.time()
	current_time = time.time()-start_time
	while(current_time<total_time):
		motor.power(motora, 100, True)
		motor.power(motorb, -100, True)
		current_time = time.time()-start_time
	motor.power(motora, 0, True)
	motor.power(motorb, 0, True)

def rotate_cl(axis, degrees):
	log.store('Rotate '+str(degrees)+' along '+str(axis))
	sel_axis = select_axis(axis)[0]	
	motora = select_axis(axis)[1]	
	motorb = select_axis(axis)[2]	

	motor.power(motora, 40, True)
	motor.power(motorb,-40, True)
	theta_0 = sensor.IMU_get_theta()[sel_axis]
	theta = sensor.IMU_get_theta()[sel_axis]-theta_0
	while theta < degrees:
		theta = sensor.IMU_get_theta()[sel_axis]-theta_0
		log.store('theta = ' + str(theta))
	motor.power(motora, 0, True)
	motor.power(motorb, 0, True)

def move_ol(axis, distance):
	log.store('Move Distance '+str(degrees))
	sel_axis = select_axis(axis)[0]	
	motora = select_axis(axis)[1]	
	motorb = select_axis(axis)[2]	

	total_time = distance/move_time[sel_axis]
	start_time = time.time()
	current_time = time.time()-start_time
	while(current_time<total_time):
		motor.power(motora, 100, True)
		motor.power(motorb, 100, True)
		print '100'
		current_time = time.time()-start_time
	motor.power(1,0, True)
	motor.power(2,0, True)

def move_cl(axis, distance):
	log.store('Move Distance '+str(degrees))
	sel_axis = select_axis(axis)[0]	
	motora = select_axis(axis)[1]	
	motorb = select_axis(axis)[2]	
	
	dist = sensor.IMU_get_theta()[sel_axis]
	while(dist<=distance):
		mout = (distance-dist)*kp
		motor.power(motora, mout, True)
		motor.power(motorb, mout, True)
		dist = sensor.IMU_get_theta()[axis]
	motor.power(motora, 0, True)
	motor.power(motorb, 0, True)

def motor_test():
	for i in range(1,7):
		motor.power(i, 25, True)
		time.sleep(.25)
		motor.power(i, 50, True)
		time.sleep(.25)
		motor.power(i, 75, True)
		time.sleep(.25)
		motor.power(i, 100, True)
		time.sleep(.25)
		motor.power(i, 0, True)

def select_axis(axis):
	if (axis is 'y'):
		axis1 = 0
		motora = 1
		motorb = 2
	elif (axis is 'x'):
		axis1 = 1
		motora = 3
		motorb = 4
	elif (axis is 'z'):
		axis1 = 2
		motora = 5
		motorb = 6
	else:
		 log.store('not an axis')
	return axis1,motora, motorb
