#!/usr/bin/python2.7

from SimpleCV import *

class ImageProcessing:

    def lineFinding(self, image):
        lineSegmentArray = []
        whiteLine = image.colorDistance(Color.WHITE)
        line = image - whiteLine
        blobArray = line.findBlobs()
        for blob in blobArray:
            if blob.area() > 200:
                blob.draw(color=Color.RED, width=-1)
                lineSegmentArray.append(blob.centroid())
                line.drawCircle((blob.centroid()),10,color=Color.BLUE)
                line.show()
