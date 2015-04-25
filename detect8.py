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
PINK = (193,157,171)
ORANGE = (209,158,129)
BROWN = (147,126,100)
colors = [BLUE, RED, GREEN, YELLOW, PURPLE, PINK, ORANGE, BROWN]
cnames = ["blue", "red", "green", "yellow", "purple", "pink", "orange", "brown"]

i = 0
for c in colors:
    blue_dist = image.colorDistance(colors[i])
    bw = blue_dist.binarize(50)
    ba = bw.findBlobs()
    if ba:
        blob = ba[-1]
        x = blob.centroid()[0]
        y = blob.centroid()[1]
        print x
        print y
        image.drawText(cnames[i],x, y, color=Color.RED, fontsize=28)  
        i=i+1

image.show()

hist = image.hueHistogram()
peaks = image.huePeaks()
print peaks
#plt.plot(hist)
#plt.draw()

time.sleep(100)
