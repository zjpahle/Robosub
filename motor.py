import serial
import struct 
import time
import log

def serial_init():
	global ser
	mcdevice  = '/dev/ttyUSB0'
	ser = serial.Serial(mcdevice, 115200, timeout=1)
	log.store('initializing motor serial device:'+ str(mcdevice))

def init(device): #device number is set using SmcCenter.exe tool (0-6)
    log.store('Initializing Motor: '+str(device))
    device_hex = struct.pack("B", int(device)) #packs device number into serial value
    ser.write('\xAA') #if using auto baud rate, tells controller the speed
    ser.write(device_hex) #device command
    ser.write('\x03') #0 power on a scale of -127 to 127

def power(device, power, logging): #device: 0-6 power: -100 to 100
	if logging is True:
		log.store('Motor '+str(device)+' Power = '+ str(power))
	ser.write('\xFF')      #set miniSSC protocol
	device_hex = struct.pack("B", int(device)) #pack int value to hex value
	ser.write(device_hex)      #set device number

# input scaling
	if (power > 100):
		power = 100
	if(power < -100):
		power = -100
	power = (power + 100) * 254/200 #shift and scale input to the motor controller range
	speed_hex = struct.pack("B", int(power)) #pack int value to hex value
	ser.write(speed_hex)      #set speed

