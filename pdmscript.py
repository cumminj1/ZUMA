#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:15:48 2018

@author: jeaic
"""

import numpy
import matplotlib.pylab as plt
from PyAstronomy.pyTiming import pyPDM

# Create artificial data with frequency = 3,
# period = 1/3
period_1=(99)
frequency_1=(3)

period_2=(120)
frequency_2=(11)

period_3=(240)
frequency_3=(29)

x = numpy.arange(100) / 100.0
y = numpy.sin(x*2.0*numpy.pi*frequency_1 + 1.7)+numpy.sin(x*frequency_2*2.0*numpy.pi+1.7)++numpy.cos(x*frequency_3*2.0*numpy.pi+1.7)

noise=numpy.random.normal(0,1,x.shape)
y1=y+noise


# Get a ``scanner'', which defines the frequency interval to be checked.
# Alternatively, also periods could be used instead of frequency.
S = pyPDM.Scanner(minVal=0.05, maxVal=260, dVal=0.01, mode="frequency")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``frequency'') and associated Theta statistic (t).
# Use 10 phase bins and 3 covers (= phase-shifted set of bins).
P = pyPDM.PyPDM(x, y1)
f1, t1 = P.pdmEquiBinCover(10, 6, S)
# For comparison, carry out PDM analysis using  bins (no covers).
f2, t2 = P.pdmEquiBin(10, S)


# Show the result
#plt.figure(facecolor='white')
plt.subplot(2,1,1)
plt.title('convoluted sinusoidals')
plt.scatter(x,y1)
plt.text(0.5,0.8,'input period 1=' +str(period_1)+ "\n "+" input period 2=" +str(period_2)+"\n "+" input period 3=" +str(period_3),fontsize=7)

plt.subplot(2,1,2)
plt.title("Result of PDM analysis ")
plt.xlabel("freq")
plt.ylabel("Theta")
#plt.plot(f1, t1, 'bp-')
plt.plot(f2, t2, 'gp-')
plt.xticks(numpy.arange(min(f2)+0.5, max(f2)+0.5,1.0))
plt.legend([" Bins without covers"])
plt.show()
