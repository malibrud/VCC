#! /usr/bin/python2.7

from SimpleCV import *
#from motorControl import *
from coordConvert import *
from imageProcessing import *
import time

#mc = MotorControl()
cc = CoordConvert()
ip = ImageProcessing()
cam = Camera(1)

robotX = 0
robotY = 0

while 1:
    img = cam.getImage()
    lineSegments = ip.lineFinding(img)
    for i in range(0, lineSegments.length()):
        s = lineSegments[i]
        r = cc.rasterToRobot(s[0], s[1])
        print r
    print lineSegments
