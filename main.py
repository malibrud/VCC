#! /usr/bin/python2.7

from SimpleCV import *
from motorControl import *
from coordConvert import *
from imageProcessing import *
#from robotModel import *
import time

mc = MotorControl()
cc = CoordConvert()
ip = ImageProcessing()
#rm = RobotModel()
cam = Camera(1)

robotX = 0
robotY = 0

lineArray = []
paperArray = []
colorFoundArray = [0,0,0,0,0,0,0,0,0,0]
colorSequenceArray = []
speed = 22.1
rps = 1.26

#mc.forward()

while 1:
    #mc.left()
    #time.sleep(1)
    #mc.right()
    #time.sleep(1)
    paperArray = []
    lineArray = []
    
    img = 0
    # Get an image
    img = cam.getImage()
    img = cam.getImage()
    img.show()
    # find blobs
    t = time.time()
    ip.findGarbage(img)
    print "time " + str(time.time() - t)
    #raw_input("hit enter")
    # for each located blob, convert the position from camera to robot
    # and them from robot to world coordinate system
    # We may need to filter them based on which ones are fully in the view 
    # (i.e. exclude those which are on the edge).
    # We may also want to find other features such as corners` or edges.
    # For each paper, there will be 4 corners.  Also corners can be used 
    # if a partial paper or tape is in view.

    print len(ip.lineSegmentArray)
    for i in range(0, len(ip.lineSegmentArray)):
        s = ip.lineSegmentArray[i]
        r = cc.rasterToRobot(s[0], s[1])
        lineArray.append(r)
        w = cc.robotToWorld(0,0, r.item((0,0)), r.item((1,0)), 0)

    print len(ip.paperArray)
    for i in range(0, len(ip.paperArray)):
        s = ip.paperArray[i]
        r = cc.rasterToRobot(s[0], s[1])
        paperArray.append(r)
        w = cc.robotToWorld(0,0, r.item((0,0)), r.item((1,0)), 0)

    driveTo = 0


    print "found " + str(len(paperArray)) + " papers"
    print "found " + str(len(lineArray)) + " lines"
    if len(paperArray) > 0:
	    closest = 1000
	    closestIDX = 0
	    print "processing " + ip.cnames[i]
	    for i in range(0,len(paperArray)):
                if colorFoundArray[ip.colorValueArray[i]] == 0:
		    print "color found: " + ip.cnames[i]
	            colorSequenceArray.append(ip.colorValueArray[i])
		    colorFoundArray[ip.colorValueArray[i]] = 1
		    print "colors found: " + str(colorFoundArray[:])
                if paperArray[i][1] < closest:
	            closest = paperArray[i][1]
	            closestIDX = i
            driveTo = paperArray[closestIDX]
	    print "closest paper: " + ''.join(str(e) for e in driveTo) 

    if len(paperArray) == 0 and len(lineArray) > 0:
	    closest = 1000
	    closestIDX = 0
	    for i in range(0,len(lineArray)):
                if lineArray[i][1] < closest:
	            closest = lineArray[i][1]
	            closestIDX = i
            driveTo = lineArray[closestIDX]
	    print "closest line segment: " + ''.join(str(e) for e in driveTo) 
        
    if len(paperArray) == 0 and len(lineArray) == 0:
	mc.stop()
        break

    print "driving to: " + ''.join(str(e) for e in driveTo) 
    closestBlob = driveTo 
    
    #angle = math.atan2(closestBlob.item((1,0)) , closestBlob.item((0,0)))
    angle = math.atan2(closestBlob[1] , closestBlob[0])
    angle = angle - (math.pi/2)

    print angle

    if angle < -.05:
        mc.right()
        time.sleep(-angle/rps) 
        mc.coast()

    if angle > .05:
	    mc.left()
	    time.sleep(angle/rps)
	    mc.coast()
        
    dist = (closestBlob[1] - 25 ) * 0.25
    print "dist: " + str(float(dist[0]))

    if dist > 0:
        mc.forward()
        time.sleep(float(dist)/speed)
        #time.sleep(.1)
        mc.coast()
	#time.sleep(.1)

    else:
	mc.stop()

    time.sleep(0.5)
    
    #if closestBlob.item((0,0)) > 10:
	#mc.right()
	#time.sleep(.1)

    #if closestBlob.item((0,0)) < -10:
	#mc.left()
	#time.sleep(.1)
    
    # We will need to compare each blob  the world or robot coordinate system
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
