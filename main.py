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

lineArray = []
paperArray = []
colorFoundArray = [0,0,0,0,0,0,0,0,0,0]
colorSequenceArray = []
speed = 22.1
rps = 1.26
driveTo = 0

#drive coarse and find blobs
while 1:
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
	break

    #print "driving to: " + ''.join(str(e) for e in driveTo) 
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
        #mc.coast()
        mc.stop()
	time.sleep(.3)
	#time.sleep(.1)

    else:
	mc.stop()

    #time.sleep(0.5)


mc.stop()
mc.right()
time.sleep(math.pi/rps)
mc.stop()
time.sleep(.1)

i = 0
maxColor = 0

for color in colorFoundArray:
	if colorFoundArray[i] == 1:
		maxColor = i
	i = i + 1
minIDX = 0
maxIDX = 0
colorMin = 10
colorMax = -1
i = 0
for c in colorSequenceArray:
        if c < colorMin:
		colorMin = c
		minIDX = i
        if c > colorMax:
		colorMax = c
		maxIDX = i
	i = i + 1
if minIDX < maxIDX:
	turnAgain = False
else:
	turnAgain = True
        
                
##########################################################################
#drive towards maximum
while 1: 
    brake = 0
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
	    target = 1000
	    targetIDX = 0
	    closest = 1000
	    closestIDX = 0
	    print "processing " + ip.cnames[i]
	    for i in range(0,len(paperArray)):
		if colorValueArray[i] == maxColor:
			brake = 1
			targetIDX = i
			target = paperArray[i][1]
			break
                if paperArray[i][1] < closest:
	            closest = paperArray[i][1]
	            closestIDX = i
            driveTo = paperArray[closestIDX]
	    print "target paper: " + ''.join(str(e) for e in driveTo)
	    if brake == 1:
		    driveTo = paperArray[targetIDX]
		    break

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
	mc.right()
	time.sleep(math.pi/rps)
	mc.stop()
	time.sleep(.1)
	print "found end the line"
        
	break

    #print "driving to: " + ''.join(str(e) for e in driveTo) 
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
        
    dist = (closestBlob[1] - 25 )
    print "dist: " + str(float(dist[0]))

    if dist > 0:
        mc.forward()
        time.sleep(float(dist)/speed)
        #time.sleep(.1)
        #mc.coast()
        mc.stop()
	time.sleep(.3)
	#time.sleep(.1)

    else:
	mc.stop()
	
# Drive to the max waypoint
closestBlob = driveTo 
angle = math.atan2(closestBlob[1] , closestBlob[0])
angle = angle - (math.pi/2)


if angle < -.05:
    mc.right()
    time.sleep(-angle/rps) 
    mc.coast()

if angle > .05:
    mc.left()
    time.sleep(angle/rps)
    mc.coast()
        
    dist = (closestBlob[1] - 25 )
    print "dist: " + str(float(dist[0]))

if dist > 0:
    mc.forward()
    time.sleep(float(dist)/speed)
    #time.sleep(.1)
    #mc.coast()
    mc.stop()
    time.sleep(.3)
    #time.sleep(.1)

else:
    mc.stop()

#Spin twice
mc.right()
time.sleep(math.pi * 4 / rps)
mc.stop()
time.sleep(1)

if turnAgain:
	mc.right()
	time.sleep(math.pi / rps)
	mc.stop()

##########################################################################
#drive towards minimum paper
while 1: 
    brake = 0
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
	    target = 1000
	    targetIDX = 0
	    closest = 1000
	    closestIDX = 0
	    print "processing " + ip.cnames[i]
	    for i in range(0,len(paperArray)):
		if colorValueArray[i] == colorMin:
			brake = 1
			targetIDX = i
			target = paperArray[i][1]
			break
                if paperArray[i][1] < closest:
	            closest = paperArray[i][1]
	            closestIDX = i
            driveTo = paperArray[closestIDX]
	    print "target paper: " + ''.join(str(e) for e in driveTo)
	    if brake == 1:
		    driveTo = paperArray[targetIDX]
		    break

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
	mc.right()
	time.sleep(math.pi/rps)
	mc.stop()
	time.sleep(.1)
	print "found end the line"
        
	break

    #print "driving to: " + ''.join(str(e) for e in driveTo) 
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
        
    dist = (closestBlob[1] - 25 )
    print "dist: " + str(float(dist[0]))

    if dist > 0:
        mc.forward()
        time.sleep(float(dist)/speed)
        #time.sleep(.1)
        #mc.coast()
        mc.stop()
	time.sleep(.3)
	#time.sleep(.1)

    else:
	mc.stop()
	
# Drive to the max waypoint
closestBlob = driveTo 
angle = math.atan2(closestBlob[1] , closestBlob[0])
angle = angle - (math.pi/2)


if angle < -.05:
    mc.right()
    time.sleep(-angle/rps) 
    mc.coast()

if angle > .05:
    mc.left()
    time.sleep(angle/rps)
    mc.coast()
        
    dist = (closestBlob[1] - 25 )
    print "dist: " + str(float(dist[0]))

if dist > 0:
    mc.forward()
    time.sleep(float(dist)/speed)
    #time.sleep(.1)
    #mc.coast()
    mc.stop()
    time.sleep(.3)
    #time.sleep(.1)

else:
    mc.stop()
