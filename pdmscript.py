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
x = numpy.arange(100) / 100.0
y = numpy.sin(x*2.0*numpy.pi*3.0 + 1.7)+numpy.sin(x*7.0*2.0*numpy.pi+1.7)++numpy.cos(x*11*2.0*numpy.pi+1.7)

noise=numpy.random.normal(0,1,x.shape)
y1=y+noise


# Get a ``scanner'', which defines the frequency interval to be checked.
# Alternatively, also periods could be used instead of frequency.
S = pyPDM.Scanner(minVal=0.5, maxVal=20.0, dVal=0.01, mode="frequency")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``frequency'') and associated Theta statistic (t).
# Use 10 phase bins and 3 covers (= phase-shifted set of bins).
P = pyPDM.PyPDM(x, y1)
f1, t1 = P.pdmEquiBinCover(3, 6, S)
# For comparison, carry out PDM analysis using  bins (no covers).
f2, t2 = P.pdmEquiBin(3, S)


# Show the result
#plt.figure(facecolor='white')
plt.subplot(2,1,1)
plt.title('convoluted sinusoidals')
plt.scatter(x,y1)
plt.legend(['freq=3,7,11'])

plt.subplot(2,1,2)
plt.title("Result of PDM analysis ")
plt.xlabel("Frequency")
plt.ylabel("Theta")
#plt.plot(f1, t1, 'bp-')
plt.plot(f2, t2, 'gp-')
plt.xticks(numpy.arange(min(f2)+0.5, max(f2)+1.5,1.0))
plt.legend([" Bins without covers"])
plt.show()