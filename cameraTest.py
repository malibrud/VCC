#! /usr/bin/python2.7

from SimpleCV import *
import time

cam = Camera(1)
blobColorArray = []
blobCenterArray = []
blobHSVArray = []
blobHeightArray = []
blobWidthArray = []
blobAreaArray = []

while 1:
    img = cam.getImage()

    blobArray = img.findBlobs()

    for blob in blobArray:
	if blob.mHoleContour < 1:
        	blob.draw(color=Color.GREEN, width=-1)
		img.drawCircle((blob.centroid()), 10, color=Color.RED)
		#img.drawCircle((blob.Corner()), 10, color=Color.Blue)
		blobHeightArray.append(blob.minRectHeight())
		blobWidthArray.append(blob.minRectWidth())
		blobAreaArray.append(blob.area())
		blobColorArray.append(blob.meanColor())

   # for i in range(0,len(blobColorArray)):
#	hsv = Color.hsv(blobColorArray[i])
#	blobHSVArray.append(hsv)
#
 #   for i in range(0,len(blobHSVArray)):
#	print blobHSVArray[i]
 #       print ' '
#

    print blobHeightArray[0]
    print blobWidthArray[0]
    print blobAreaArray[0]
    print ' '    

    img.show()

    time.sleep(2)
