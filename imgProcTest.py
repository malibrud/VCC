from imageProcessingCalibration import *
from SimpleCV import *

ip = ImageProcessing()

cam = Camera(1)

red = (253,32,141)
purple = (96,95,255)
brown = (192,115,68)



while 1:
	img = cam.getImage()
	ip.findGarbage(img)
	raw_input(" >>> ")
