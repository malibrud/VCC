#!/usr/bin/python2.7

from SimpleCV import *
import time

class ImageProcessing:

    def __init__(self):
	self.lineSegmentArray = []
	self.paperArray = []
	self.colorValueArray = []
	self.BROWN = (254,105,44)
	self.BLACK = (28,28,28)
	self.WHITE = (251,184,136)
	self.BLUE = (152,101,184)
	self.RED = (255,40,71)
	self.GREEN = (105,148,43)
	self.YELLOW = (253, 196 ,10)
	self.PURPLE = (180,37,106)
	self.PINK = (255,85,74)
	self.ORANGE = (253,121,32)
	self.colors = [self.BLACK, self.BLUE, self.BROWN, self.GREEN, self.ORANGE, self.PINK, self.RED, self.PURPLE, self.WHITE, self.YELLOW]
	self.cnames = ["black", "blue", "brown", "green", "orange", "pink", "red", "purple", "white", "yellow"]
	self.threshArray = [(50,50,50), (50,50,50), (50,50,50), (50,50,50),(50,50,50),(50,50,50),(50,50,50),(50,50,50),(50,50,50),(50,50,50)]

    def findGarbage(self, image):
	self.lineSegmentArray = []
	self.paperArray = []
	image.show()

	blobArray = image.findBlobs(minsize=400, threshval=80)
	print str(blobArray)

	
	if len(blobArray) == 0:
		image.show()
		print "No blobs found"
		return


	j = 0
	for blob in blobArray:
		#if blob.area() < 500 or blob.mHoleContour >=2:
		if blob.area() < 500:
			continue 
		print "processing blob " +str(j) + " of mean color " + str(blob.meanColor())
		print "  Area = " +str(blob.area()) 
		i = 0
		minDist = 1000.0
		minDistIDX = -1
		for c in self.colors:
			dist = abs(blob.meanColor()[0] - self.colors[i][0]) + abs(blob.meanColor()[1] - self.colors[i][1]) + abs(blob.meanColor()[2] - self.colors[i][2])
			if dist < minDist:
				minDist = dist
				minDistIDX = i
			print "distance for color " + self.cnames[i] + " is " + str(dist)
			i = i + 1
			
		#if abs(blob.meanColor()[0] - self.colors[i][0]) < self.threshArray[i][0] and abs(blob.meanColor()[1] - self.colors[i][1]) < self.threshArray[i][1] and abs(blob.meanColor()[2] - self.colors[i][2]) < self.threshArray[i][2]:
		blob.show()
		image.drawText(self.cnames[minDistIDX] + str(j), blob.centroid()[0], blob.centroid()[1], color=Color.BLACK, fontsize=28)
		j = j + 1
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

	
