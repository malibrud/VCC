import serial
import time

print "beginning of program"

ser = serial.Serial()
ser.port = "COM5"
ser.baudrate = 2400
ser.bytesize = serial.EIGHTBITS
#ser.parity =  PARITY.NONE
ser.stopbits = serial.STOPBITS_TWO
ser.open()
time.sleep(2)

if ser.isOpen():
    
    forward = "xo1\x6f\x6f"
    stop   =  "xo1\x7f\x7f"
    left  =   "xo1\x7f\x6f"
    right  =  "xo1\x6f\x7f"
    
    command = cmd1
    ser.write(command)
    time.sleep(2)
    ser.write(cmd2)
    
    command = cmd3
    ser.write(command)
    time.sleep(2)
    ser.write(cmd2)
    
    command = cmd4
    ser.write(command)
    time.sleep(2)
    ser.write(cmd2)
    
    ser.close()
    break
else:
    
    print "error opening serial port"
