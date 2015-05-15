#! /usr/bin/python2.7

from SimpleCV import *

cam = Camera(1)

img = cam.getImage()
img.show()
img.save("image.bmp")

