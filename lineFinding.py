#!/usr/bin/python2.7

from SimpleCV import *

while 1:
    img = Image("floorImages/floor.jpg")
    whiteLine = img.colorDistance(Color.WHITE)
    line = img - whiteLine
    blobArray = line.findBlobs()
    #print blobs[:].meanColor()
    for blob in blobArray:
        if blob.area() > 200:
            blob.draw(color=Color.RED, width=-1)
            line.drawCircle((blob.centroid()),10,color=Color.BLUE)
    line.show()
