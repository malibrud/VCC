#!/usr/bin/python2.7

from SimpleCV import *
import matplotlib.pyplot as plt
import time

plt.ion()

black = Image("image9.bmp")
image = Image("red.bmp")
#image = image.scale(0.25)

bhist = black.hueHistogram()
hist = image.hueHistogram()
peaks = image.huePeaks()
print peaks
plt.plot(hist)
plt.plot(bhist)
plt.plot(hist-bhist)
plt.draw()

time.sleep(100)
