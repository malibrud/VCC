#!/usr/bin/python2.7

from SimpleCV import *
import time

class ImageProcessing:

    def __init__(self):
	self.lineSegmentArray = []
	self.paperArray = []
	self.colorValueArray = []
	self.BROWN = (183,111,94)
	self.BLACK = (128,128,128)
	self.WHITE = (255,255,255)
	self.BLUE = (0,130,255)
	self.RED = (252,8,147)
	self.GREEN = (8,202,153)
	self.YELLOW = (237, 246,93)
	self.PURPLE = (67,93,246)
	self.PINK = (255,139,234)
	self.ORANGE = (255,139,126)
	self.BROWN = (147,126,100)
	self.colors = [self.BLACK, self.BLUE, self.BROWN, self.GREEN, self.ORANGE, self.PINK, self.RED, self.PURPLE, self.WHITE, self.YELLOW]
	self.cnames = ["black", "blue", "brown", "green", "orange", "pink", "red", "purple", "white", "yellow"]

    def findGarbage(self, image):
	self.lineSegmentArray = []
	self.paperArray = []

	blobArray = image.findBlobs()

	for blob in blobArray:
		i = 0
		for c in self.colors:
			if abs(blob.meanColor()[0] - self.colors[i][0]) < 100 and abs(blob.meanColor()[1] - self.colors[i][1]) < 100 and abs(blob.meanColor()[2] - self.colors[i][2]) < 100:
				image.drawText(self.cnames[i], blob.centroid()[0], blob.centroid()[1], color=Color.GREEN, fontsize=28)
			i = i + 1
	image.show()

#	for c in self.colors:
#		#if i != 8:
#			#continue
#		colorSelect = image - image.colorDistance(self.colors[i])
#		bw = colorSelect.binarize(self.threshArray[i])
#        	blobArray = colorSelect.findBlobs()
#
#		if blobArray:
#			for blob in blobArray:
#				#if blob.mHoleContour < 2 and blob.area() > 600 and blob.area() < 7000 and i == 8:
#				if blob.mHoleContour < 2 and blob.area() > 600 and blob.area() < 10000 :
#					self.lineSegmentArray.append(blob.centroid())
#					blob.draw(color = (0,255,0), alpha = -1, width = -1)
#					image.drawText("line", blob.centroid()[0], blob.centroid()[1], color=Color.BLUE, fontsize=28)
#				if blob.mHoleContour < 2 and blob.area() > 10000 and i != 8:
#					self.paperArray.append(blob.centroid())
#					blob.draw(color = (255,0,0), alpha = -1, width = -1)
#					self.colorValueArray.append(i)
#					image.drawText(self.cnames[i], blob.centroid()[0], blob.centroid()[1], color=Color.GREEN, fontsize=28)

#		i = i + 1
#	image.show()

	
