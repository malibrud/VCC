#! /usr/bin/python2.7

from SimpleCV import *
#from motorControl import *
from coordConvert import *
from imageProcessing import *
from robotModel import *
import time

#mc = MotorControl()
cc = CoordConvert()
ip = ImageProcessing()
rm = RobotModel()
cam = Camera(0)

robotX = 0
robotY = 0


#mc.forward()

while 1:
    # Get an image
    img = cam.getImage()

    # find blobs
    lineSegments = ip.lineFinding(img)

    # for each located blob, convert the position from camera to robot
    # and them from robot to world coordinate system
    # We may need to filter them based on which ones are fully in the view 
    # (i.e. exclude those which are on the edge).
    # We may also want to find other features such as corners or edges.
    # For each paper, there will be 4 corners.  Also corners can be used 
    # if a partial paper or tape is in view.
    rm.right()
    time.sleep(.1)
    print rm.x
    print rm.y
    print rm.th

    for i in range(0, len(lineSegments)):
        s = lineSegments[i]
        r = cc.rasterToRobot(s[0], s[1])
        w = cc.robotToWorld(0,0, r.item((0,0)), r.item((1,0)), 0)
        print w

    # We will need to compare each blob in the world or robot coordinate system
    # to those on the known landmark list.
    # If an object is on the known landmark list.  Do a match.
    # if an object is not on the known landmark list, add it to the list.

    # Based on our known land marks and the model output estimate our new robot
    # position.  This will be moderately complex.

    # Determine next position to drive toward.

    # Drive the robot

    # Sleep ??

    # Update current time.

    # run model to estimate current position
