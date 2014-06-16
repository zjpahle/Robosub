import robot
import time
import log

log_motor = True

def system():
    robot.log.store('Starting system test')
    robot.motor.serial_init()
    robot.sensor.serial_init()
    for i in range(1,7):
        robot.motor.init(i)
    robot.motor_test()
    robot.log.store('System test complete')

def downthrust():
	log.store('Starting downthrust test:')
	robot.motor.power(3,100,logging)
	robot.motor.power(4,100,logging)
	robot.time.sleep(5)
	accel = robot.sensor.IMU_get_accel(logging)

def pressuretest():
    log.store('Starting Pressure Test')
    robot.motor.power(3, 100, True)
    robot.motor.power(4, 100, True)
    init_time = time.time()
    current_time = time.time()-init_time
    while(current_time<=10):
		robot.sensor.IMU_get_pressure()
		current_time = time.time()-init_time
    init_time = time.time()
    current_time = time.time()-init_time
    robot.motor.power(3, -50, True)
    robot.motor.power(4, -50, True)
    while(current_time<=10):
		robot.sensor.IMU_get_pressure()
		current_time = time.time()-init_time
    robot.motor.power(3, 0, True)
    robot.motor.power(4, 0, True)

def jasons_test():
	robot.motor.power(3,100,log_motor)
	robot.motor.power(4,100,log_motor)
	log.picture()
	time.sleep(2)
	robot.motor.power(3,0,log_motor)
	robot.motor.power(4,0,log_motor)
	time.sleep(2)
	robot.motor.power(1,100,log_motor)
	robot.motor.power(2,100,log_motor)
	log.picture()
	robot.motor.power(3,35,log_motor)
	robot.motor.power(4,35,log_motor)
	time.sleep(120)
	log.picture()
	robot.motor.power(1,0,log_motor)
	robot.motor.power(2,0,log_motor)
	robot.motor.power(3,-100,log_motor)
	robot.motor.power(4,-100,log_motor)
	time.sleep(8)
	log.picture()
	for x in range(0,7):
		robot.motor.power(x,0,log_motor)
		log.picture()
