import robot

logging = True

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
    robot.motor.power(1, 100, True)
    robot.motor.power(2, 100, True)
    init_time = time.time()
    current_time = time.time()-init_time
    while(current_time<=10):
        robot.sensor.get_pressure()
        current_time = time.time()-init_time
    init_time = time.time()
    robot.motor.power(1, 0, True)
    robot.motor.power(2, 0, True)
    while(current_time<=10):
        robot.sensor.get_pressure()
        current_time = time.time()-init_time
