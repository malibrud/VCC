from SimpleCV import *
import time

#colorArray = [(85,118,179), (147,126,100), (99,160,127),(209,158,129),(193,157,171),(127,131,177),(181, 196, 104)]  
blobCenterArray = []
while 1:
	img = Image("image.bmp")
	colorSelect = img.colorDistance((193,216,224)).binarize(40)
	blobArray = colorSelect.findBlobs()
	for blob in blobArray:
		if blob.mHoleContour < 2:
			if blob.area() > 1500:
				x = blob.centroid()[0]
				y = blob.centroid()[1]
			 	img.drawText("line",x, y, color=Color.RED, fontsize=28)	

	img.show()
	time.sleep(2)

