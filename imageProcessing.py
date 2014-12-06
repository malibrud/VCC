#!/usr/bin/python2.7

from SimpleCV import *

hist = Camera().getImage().histogram(20)
brightpixels = 0
darkpixels = 0
i = 0

for h in hist:
    if i < 10:
        darkpixels = darkpixels + hist[i]
    else:
        brightpixels = brightpixels + hist[i]
    i = i + 1

if (brightpixels > darkpixels):
    print "Bright"
else:
    print "Dark"