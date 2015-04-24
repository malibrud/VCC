#!/usr/bin/python2.7

from SimpleCV import *
import matplotlib.pyplot as plt
import time

plt.ion()

image = Image("image8.bmp")
BLUE = (85,118,179)
RED = (170,90,113)
GREEN = (99, 160, 127)
YELLOW = (181, 196, 104)
PURPLE = (127,131,177)
YELLOW = (127,131,177)
blue_dist = image.colorDistance(RED)
blue_only = image-blue_dist
gray = blue_only.toGray() 
bw = blue_dist.binarize(45)
bw.show()

hist = image.hueHistogram()
peaks = image.huePeaks()
print peaks
#plt.plot(hist)
#plt.draw()

time.sleep(100)
