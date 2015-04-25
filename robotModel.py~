import time
import math
class RobotModel:

     def __init__(self):
          self.x = 0
          self.y = 0
          self.th = 0
          self.t = time.time()
          self.speed = 30
          self.vl = 0
          self.vr = 0
	  self.w = 34.5
     def forward(self):
        tn = time.time()
        dt = tn - self.t
        self.t = tn
        self.vl = self.speed
        self.vr = self.speed
        self.vy (self.vl + self.vr)/2
        self.vth (self.vr - self.vl)/self.w
        
        if vth == 0:
            self.x = self.x - self.vy * math.sin(self.th)* dt 
            self.y = self.y + self.vy * math.cos(self.th)* dt 
	elif self.vl == 0:
            dth = self.vth * dt 
            self.th = self.th + self.vth    
            dx = (math.cos(dth)-1) * self.w/2
            dy = math.sin(dth) * self.w/2
            self.x = self.x + dx * math.cos(self.th)* dt - dy * math.sin(self.th)* dt 
            self.y = self.y + dx * math.sin(self.th)* dt + dy * math.cos(self.th)* dt 
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

