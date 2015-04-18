#! /usr/bin/python2.7

from SimpleCV import *

cam = Camera(1)
blobArray = []

img = cam.getImage()

blobArray = img.findBlobs()

for blob in blobArray:
    blob.draw(color=Color.GREEN, width=-1)
    img.show