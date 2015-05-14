#!/usr/bin/python2.7

from SimpleCV import *
import time

class ImageProcessing:

    def __init__(self):
	self.lineSegmentArray = []
	self.paperArray = []
	self.colorValueArray = []
	self.BROWN = (148,124,104)
	self.BLACK = (128,128,128)
	self.WHITE = (255,255,255)
	self.BLUE = (0,49,243)
	self.RED = (255,0,155)
	self.GREEN = (0,235,157)
	self.YELLOW = (183, 177, 29)
	self.PURPLE = (127,131,177)
	self.PINK = (206,71,155)
	self.ORANGE = (209,158,129)
	self.BROWN = (147,126,100)
	self.colors = [self.BLACK, self.BLUE, self.BROWN, self.GREEN, self.ORANGE, self.PINK, self.RED, self.PURPLE, self.WHITE, self.YELLOW]
	self.cnames = ["black", "blue", "brown", "green", "orange", "pink", "red", "purple", "white", "yellow"]
	

    def findGarbage(self, image):
	self.lineSegmentArray = []
	self.paperArray = []

	i = 0

	for c in self.colors:
		#if i != 8:
			#continue
		colorSelect = image.colorDistance(self.colors[i]).binarize(100)	
        	blobArray = colorSelect.findBlobs()

		if blobArray:
			for blob in blobArray:
				#if blob.mHoleContour < 2 and blob.area() > 600 and blob.area() < 7000 and i == 8:
				if blob.mHoleContour < 2 and blob.area() > 600 and blob.area() < 7000 :
					self.lineSegmentArray.append(blob.centroid())
					blob.draw(color = (0,255,0), alpha = -1, width = -1)
					image.drawText("line", blob.centroid()[0], blob.centroid()[1], color=Color.BLUE, fontsize=28)
				if blob.mHoleContour < 2 and blob.area() > 7000 and i != 8:
					self.paperArray.append(blob.centroid())
					blob.draw(color = (255,0,0), alpha = -1, width = -1)
					self.colorValueArray.append(i)
					image.drawText(self.cnames[i], blob.centroid()[0], blob.centroid()[1], color=Color.GREEN, fontsize=28)

		i = i + 1
	image.show()

	
