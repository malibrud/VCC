#!/usr/bin/python2.7

from SimpleCV import Camera

cam = Camera()

while True:
    img = cam.getImage()
    img.show()