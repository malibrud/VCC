#!/usr/bin/python2.7

from SimpleCV import *
import time

image = Image("image.bmp")
#image = image.scale(0.25)

lineSegmentArray = []
whiteLine = image.colorDistance(Color.WHITE)
line = image - whiteLine
blobArray = line.findBlobs()
for blob in blobArray:
    if blob.area() > 200.0:
        blob.draw(color=Color.RED, width=-1)
        lineSegmentArray.append(blob.centroid())
        line.drawCircle((blob.centroid()),10,color=Color.BLUE)
        line.show()
time.sleep(100)
