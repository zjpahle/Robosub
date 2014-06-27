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

def go_straight(distance_target, logging):
    #   get data, use known (approximate speed) to calculate distance at 100% forward power
    #   testing shows that at max power, sub covers approximatly 14 feet in 11 seconds @ 100% 
    #forward power converted to meters, the sub covers 1 meter ever 2.5578 seconds
    timer_travel = distance_target * 2.57780277465

    timer_initial = time.time()
    timer_new = time.time()-timer_initial
    motor_power1= 100
    motor_power2 = 100
    motor.power(1, motor_power1, logging)
    motor.power(2, motor_power2, logging)
    heading_now = sensor.gyrotheta[2]
    while(timer_new <= timer_travel):
        timer_new = time.time()-timer_initial
        sensor.IMU_get_data(True)
        print heading_now
        heading_now = sensor.gyrotheta[2]
        if (heading_now > 3):  # positive gyro readings are clockwise rotation
            if (motor_power2 < 100):
                motor_power2 = motor_power2 + .1
            motor_power1 = motor_power1 - .1
            motor.power(1, round(motor_power1), logging) # assuming motor 1 is on the right
            motor.power(2, round(motor_power2), logging) # assuming motor 1 is on the right
            if(motor_power1 > 100):
                motor_power1 = 100
            if(motor_power1 < -100):
                motor_power1 = -100
            if(motor_power2 > 100):
                motor_power2 = 100
            if(motor_power2 < -100):
                motor_power2 = -100
            heading_now = sensor.gyrotheta[2]
            print heading_now
            sensor.IMU_get_data(True)
            #heading_now = sensor.gyrotheta[2]

        if (heading_now < -3):  # neagative gyro readings counter clockwise rotation
            if (motor_power1 < 100):
                motor_power1 = motor_power1 + .1
            motor_power2 = motor_power2 - .1
            motor.power(1, round(motor_power1), logging)   
            motor.power(2, round(motor_power2), logging)
            if(motor_power1 > 100):
                motor_power1 = 100
            if(motor_power1 < -100):
                motor_power1 = -100
            if(motor_power2 > 100):
                motor_power2 = 100
            if(motor_power2 < -100):
                motor_power2 = -100
            heading_now = sensor.gyrotheta[2]
            print heading_now
            sensor.IMU_get_data(True)
            #heading_now = sensor.gyrotheta[2]
    motor.power(1,100,True)
    motor.power(2,100,True)
      
def debubblizeme():

    motor.power(1, 0, True) #Ensure the bot is not moving
    motor.power(2, 0, True)
    motor.power(3, 0, True)
    motor.power(4, 0, True)
    motor.power(5, 0, True)
    motor.power(6, 0, True)

    time.sleep(0.5)

    motor_power(3, 100)
    motor_power(4, -100)
    motor_power(5, 100)
    motor_power(6, -100)
    time.sleep(5)

    motor_power(3, -100)
    motor_power(4, 100)
    motor_power(5, -100)
    motor_power(6, 100)

    time.sleep(8)

    motor_power(3, 0)
    motor_power(4, 0)
    motor_power(3, 0)
    motor_power(4, 0)

    rawdata = sensor.rawdata
    data = rawdata.strip('\r\n').split(':')
    Zaccel=[float(data[x])/1632 for x in [8]] 

    while (Zaccel>=-9.3): #Allow Bot to right itself
        time.sleep(0.5)
        rawdata = ser2.readline()
        data = rawdata.strip('\r\n').split(':')
        Zaccel=[float(data[x])/1632 for x in [8]]

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
