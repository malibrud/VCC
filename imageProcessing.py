#!/usr/bin/python2.7

from SimpleCV import *
import time

class ImageProcessing:

    def __init__(self):
	self.lineSegmentArray = []
	self.paperArray = []
	self.BLUE = (0,50,185)
	self.RED = (170,90,113)
	self.GREEN = (99, 160, 127)
	self.YELLOW = (181, 196, 104)
	self.PURPLE = (127,131,177)
	self.PINK = (193,157,171)
	self.ORANGE = (209,158,129)
	self.BROWN = (147,126,100)
	self.LINE = (193,216,224)
	self.colors = [self.BLUE, self.RED, self.GREEN, self.YELLOW, self.PURPLE, self.PINK, self.ORANGE, self.BROWN, self.LINE]
	self.cnames = ["blue", "red", "green", "yellow", "purple", "pink", "orange", "brown", "line"]
	

    def findGarbage(self, image):
	lineSegmentArray = []
	paperArray = []

	i = 0
	for c in self.colors:
		colorSelect = image.colorDistance(self.colors[i]).binarize()	
        	blobArray = colorSelect.findBlobs()
		if blobArray:
			for blob in blobArray:
				if blob.area() > 1000:
					blob.draw(color = (255,0,0), alpha = -1, width = -1)
					print "found " + self.cnames[i]
					x = blob.centroid()[0]
					y = blob.centroid()[1]
					image.drawText(self.cnames[i],x, y, color=Color.RED, fontsize=28)

		i = i + 1

	image.show()
	
