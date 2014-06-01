import robot



robot.motor.serial_init()

for i in range(1,7):
	robot.motor.power(i,0,True)
