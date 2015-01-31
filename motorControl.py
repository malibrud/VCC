#! /usr/bin/python2.7

import serial
class MotorControl:


    def __init__(self):
        self.ser = serial.Serial()
        self.ser.port = "/dev/pts/3"
        print ser.portstr
        self.ser.baudrate = 2400
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_TWO
        self.ser.open()
    def forward(self):
        self.ser.write("x01\x6f\x6f")
        
    def backward(self):
        self.ser.write("x01\x5f\x5f")
        
    def left(self):
        self.ser.write("x01\x7f\x6f")
        
    def right(self):
        self.ser.write("x01\x6f\x7f")
        
    def stop(self):
        self.ser.write("\x01\x7f\x7f")
    
    while True:
        forward(self)
        stop(self)
        backward(self) 
