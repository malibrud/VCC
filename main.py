#! /usr/bin/python2.7

from SimpleCV import *
from motorControl import *
from coordConvert import *
from imageProcessing import *
import time

mc = MotorControl()
cc = CoordConvert()
ip = ImageProcessing()
cam = Camera(1)

robotX = 0
robotY = 0

mc.forward()

while 1:
    img = cam.getImage()
    lineSegments = ip.lineFinding(img)
    for i in range(0, len(lineSegments)):
        s = lineSegments[i]
        r = cc.rasterToRobot(s[0], s[1])
        w = cc.robotToWorld(0,0, r.item((0,0)), r.item((1,0)), 0)
        print w
    #print lineSegments
