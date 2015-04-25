from SimpleCV import *
import time

colorArray = [(85,118,179), (147,126,100), (99,160,127),(209,158,129),(193,157,171),(127,131,177),(181, 196, 104)]  
blobCenterArray = []
while 1:

	img = Image("image8.bmp")
	for color in colorArray:
		colorSelect = img.colorDistance(color).binarize(40)
		blobArray = colorSelect.findBlobs()
		for blob in blobArray:
			if blob.mHoleContour < 2:
				if blob.area() > 10000:
 					blob.draw(color=Color.GREEN, width=-1)
					blobCenterArray.append(blob.centroid())			
					colorSelect.show()
	
	print blobCenterArray
	time.sleep(2)

