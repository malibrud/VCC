#!/usr/bin/python2.7

from SimpleCV import *
import time

class ImageProcessing:

    def lineFinding(self, image):
        lineSegmentArray = []
        whiteLine = image.colorDistance(Color.WHITE)
        line = image - whiteLine
        blobArray = line.findBlobs(5)
        for blob in blobArray:
            if blob.area() > 200.0:
                if blob.mHoleContour < 2:
                   blob.draw(color=Color.RED, width=-1)
                   lineSegmentArray.append(blob.centroid())
                   line.drawCircle((blob.centroid()),10,color=Color.BLUE)
                   line.show()
        return lineSegmentArray

    def paperFinding(self, image):	
        lineSegmentArray = []
        redLine = image.colorDistance(Color.RED)
        line = image - redLine
        blobArray = line.findBlobs()
        if blobArray:
            for blob in blobArray:
                if blob.area() > 200.0:
                    if blob.mHoleContour < 2:
                       blob.draw(color=Color.BLUE, width=-1)
                       lineSegmentArray.append(blob.centroid())
                       line.drawCircle((blob.centroid()),10,color=Color.GREEN)
                       line.show()
            return lineSegmentArray
