#! /usr/bin/python2.7

import time
import math
class RobotModel:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.th = 0
        self.t = time.time()
        self.speed = 3
        self.vl = 0
        self.vr = 0
        self.w = 34.5
    
    def forward(self):
        self.model()
        self.vl = self.speed
        self.vr = self.speed
        
    def backward(self):
        self.model()
        self.vl = -self.speed
        self.vr = -self.speed
        
    def left(self):
        self.model()
        self.vl = 0
        self.vr = self.speed

    def right(self):
        self.model()
        self.vl = self.speed
        self.vr = 0 

    def stop(self):
        self.model()
        self.vl = 0
        self.vr = 0

    def model(self):
        tn = time.time()
        dt = tn - self.t
        self.t = tn
        vy = (self.vl + self.vr)/2
        vth = (self.vr - self.vl)/self.w
        
        if vth == 0:
            self.x = self.x - vy * math.sin(self.th)* dt 
            self.y = self.y + vy * math.cos(self.th)* dt 
	    
        elif self.vl == 0:
            dth = vth * dt 
            self.th = self.th + vth    
            dx = (math.cos(dth)-1) * self.w/2
            dy = math.sin(dth) * self.w/2
            self.x = self.x + dx * math.cos(self.th)* dt - dy * math.sin(self.th)* dt 
            self.y = self.y + dx * math.sin(self.th)* dt + dy * math.cos(self.th)* dt 
        
        elif self.vr == 0:
            dth = -vth * dt 
            self.th = self.th + vth    
            dx = (1-math.cos(dth)) * self.w/2
            dy = math.sin(dth) * self.w/2
            self.x = self.x + dx * math.cos(self.th)* dt - dy * math.sin(self.th)* dt 
            self.y = self.y + dx * math.sin(self.th)* dt + dy * math.cos(self.th)* dt 


rm = RobotModel()
for i in range(0,50):
	rm.right()
	time.sleep(1)
	print rm.x
	print rm.y
	print " "
