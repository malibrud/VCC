#! /usr/bin/python2.7

from SimpleCV import Camera 
from SimpleCV import Image

cam = Camera(1)

while True:
    img = cam.getImage()
    print img
    img.show()

