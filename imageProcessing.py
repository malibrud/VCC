#!/usr/bin/python2.7

from SimpleCV import *
import time

class ImageProcessing:

    def __init__(self):
	self.lineSegmentArray = []
	self.paperArray = []

    def findGarbage(self, image):
	lineSegmentArray = []
	paperArray = []
        blobArray = image.findBlobs(150)
        for blob in blobArray:
            if blob.area() < 16000 and blob.area() > 2000:
                if blob.mHoleContour < 2:
                   blob.draw(color=Color.RED, width=-1)
                   lineSegmentArray.append(blob.centroid())
                   image.drawCircle((blob.centroid()),10,color=Color.BLUE)
                   image.show()

	    elif blob.area() > 16000: 
                if blob.mHoleContour < 2:
                   blob.draw(color=Color.GREEN, width=-1)
                   paperArray.append(blob.centroid())
                   image.drawCircle((blob.centroid()),10,color=Color.BLUE)
                   image.show()

