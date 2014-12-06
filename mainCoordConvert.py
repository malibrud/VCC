#!/usr/bin/python2.7

from coordConvert import *

conversion = CoordConvert()

print conversion.rasterToRobot(60, 120)

print conversion.robotToWorld(10, 10, 5, 5, math.pi / 4)

print conversion.worldToRobot(10, 10, 15, 15, math.pi / 4)