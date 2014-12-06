#!/usr/bin/python2.7

from SimpleCV import *

while True:
    blue_stuff = Camera().getImage().channel(blue)
    blue_blobs = blue_stuff.findBlobs()
    blue_stuff.show()
    print "largest blue blob at " + str(blue_blobs[-1].x) + ", " + str(blue_blobs[-1].y)