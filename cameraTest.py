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
img = cam.getImage()
img.show()
img.save("image15.bmp")
while 1:
    img = cam.getImage()

    blobArray = img.findBlobs()
    i = 0
    for blob in blobArray:
	if blob.mHoleContour < 1:
                if blob.area() > 16000:
        	   blob.draw(color=Color.GREEN, width=-1)
		   img.drawCircle((blob.centroid()), 10 + i, color=Color.RED)
		   #img.drawCircle((blob.Corner()), 10, color=Color.Blue)
		   blobHeightArray.append(blob.minRectHeight())
		   blobWidthArray.append(blob.minRectWidth())
		   blobAreaArray.append(blob.area())
		   blobColorArray.append(blob.meanColor())
                   i = i + 10

   # for i in range(0,len(blobColorArray)):
#	hsv = Color.hsv(blobColorArray[i])
#	blobHSVArray.append(hsv)
#
 #   for i in range(0,len(blobHSVArray)):
#	print blobHSVArray[i]
 #       print ' '
#

    print blobHeightArray
    print blobWidthArray
    print blobAreaArray
    print ' '    

    img.show()

    time.sleep(2)
