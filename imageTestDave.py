from SimpleCV import *
import time

while 1:

	img = Image("image8.bmp")
	colorSelect = img.colorDistance((85,118,179)).binarize(40)
	blobs = colorSelect.findBlobs()
 	blobs.draw(color=Color.GREEN, width=-1)		
	colorSelect.show()	
	time.sleep(5)

