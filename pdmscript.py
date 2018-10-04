#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:15:48 2018

@author: jeaic
"""

import numpy
import matplotlib.pylab as plt
from PyAstronomy.pyTiming import pyPDM
import scipy.stats
import pandas as pd

# Create artificial data
period_1=(99)
frequency_1=(1/period_1)

period_2=(126)
frequency_2=(1/period_2)

period_3=(5)
frequency_3=(1/period_3)

#convolute the three sinusoidals
#the divisor on x changes the spacin of the poinsts along the line
x = numpy.arange(22018) /10
y = numpy.sin(x*2.0*numpy.pi*frequency_1 + 0)+numpy.sin(x*frequency_2*2.0*numpy.pi+1.7)++numpy.cos(x*frequency_3*2.0*numpy.pi+1.7)

#adding the noise
# we use a normal distibution with a std deviation of 1.0, centered at 0
stddevs=1.0
#shape our noise to the signal's dimensions
noise=numpy.random.normal(0,stddevs,x.shape)
#add to the signal
y1=y+noise


# Get a ``scanner'', which defines the frequency interval to be checked.
# Alternatively, also periods could be used instead of frequency.

#here since we have a lot of data, BinUp is the number of points per bin.
#has strong effect on the pvalue, needs to be big enough to contain fundamental
BinUp=200
S = pyPDM.Scanner(minVal=0.05, maxVal=BinUp, dVal=0.01, mode="period")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``period'') and associated Theta statistic (t).
P = pyPDM.PyPDM(x, y1)

f1, t1 = P.pdmEquiBinCover(10, 3, S)
#PDM analysis using  bins (no covers).
M=5

f2, t2 = P.pdmEquiBin(M, S)
#local minima empty list to be appended
minima=[]
theta=[]
#printing the local minima:
#what I've done is take the values where the three points either side of it
#are larger than it, then filtered such that to be accepted it must be withing
#20% of the global minimum
#)

for i in range (len(t2)-3):
    if t2[i] < t2[i+1] and t2[i] < t2[i-1]and t2[i] < t2[i-2]and t2[i] < t2[i-3]  and t2[i] < t2[i+2] and t2[i] < t2[i+3] and t2[i]  :
        then: minima.append(f2[i]) 
        theta.append(t2[i])
minima= [ '%.2f' % elem for elem in minima ]

theta=numpy.asarray(theta)
fvalue=1./theta
p_value = scipy.stats.f.cdf(fvalue, len(x)-1,BinUp-M)
p_value = 1-p_value
#print("The identified peaks are at (days): "+str(minima))
#print ("The F-Values for each of the above periods are: "+str(fvalue))
#print("The corresponding p-values are: "+str(p_value))
combined=pd.DataFrame({'p-value':p_value,'F-Value':fvalue,'Id Period':minima})
combined=combined.set_index('p-value')
combined=combined.sort_index(ascending=False)
print(combined)
stat_significant=combined.loc[combined.index < 0.05]
print("The statistically significant identified periods, and their associated p and F-values are (in days): ")
print(stat_significant)
"""
indexes=numpy.argpartition(p_value,5)[5:]
print(indexes)
print(minima[indexes[0]])
print(minima[indexes[1]])
print(minima[indexes[2]])
print(minima[indexes[3]])
print(minima[indexes[4]])"""

#props will set up the conditions we like for the textbox in the graphs
props = dict(boxstyle='round', facecolor='wheat', alpha=0.9)


#create each subplot for the input and output:
#input
plt.subplot(2,1,1)
plt.title('convoluted sinusoidals')
plt.scatter(x,y1, s=2)
plt.text(1,1,'input period 1 =' +str(period_1)+ "[days] \n "+" input period 2=" +str(period_2)+'[days]'+"\n "+" input period 3=" +str(period_3)+'[days]' + "\n Noise= normal dist with std of "+ str(stddevs),fontsize=7, bbox=props)
#output
plt.subplot(2,1,2)
plt.title("Result of PDM analysis ")
plt.xlabel("freq")
plt.ylabel("Theta")
plt.text(0.85,0.85,'output periods are: ' + str(minima)+'[days]',fontsize=7, bbox=props)
plt.plot(f2, t2, 'gp-')
plt.plot(f1,t1, 'rp-')
plt.legend([" Bins without covers","Bins with covers"])
plt.show()
