# -*- coding: utf-8 -*-
"""
This is a test of PDM module using my own artificial dataset


Created on Fri Sep 14 16:47:45 2018

@author: jeaic
"""
import numpy as np
import matplotlib.pyplot as plt
from PyAstronomy.pyTiming import pyPDM


time=np.linspace(0,5*np.pi, 1000)

sin_1=np.sin(time)
sin_2=np.sin(2*time)

mag=sin_1+sin_2

check=plt.plot(time,mag)
plt.xlabel('time')
plt.ylabel('magnitude')
plt.title('PDM signal to analyse')
plt.show()




S = pyPDM.Scanner(minVal=0.005, maxVal=15.0*np.pi, dVal=0.01, mode="frequency")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``frequency'') and associated Theta statistic (t).
# Use 10 phase bins and 3 covers (= phase-shifted set of bins).
P = pyPDM.PyPDM(mag, time)
f1, t1 = P.pdmEquiBinCover(50, 9, S)
# For comparison, carry out PDM analysis using 10 bins equidistant
# bins (no covers).
f2, t2 = P.pdmEquiBin(10, S)


# Show the result
plt.figure(facecolor='white')
plt.title("Result of PDM analysis")
plt.xlabel("Frequency")
plt.ylabel("Theta")
plt.plot(f1, t1, 'bp-')
plt.plot(f2, t2, 'gp-')
plt.legend(["pdmEquiBinCover", "pdmEquiBin"])
plt.show()