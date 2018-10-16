#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
This script will run a pdm analysis on timeseries data where
the index is a pandas datetime format. The data is read using a 
pickle file to save read times. The upperdate and lowerdate allow
you to choose what timeperiod you want to investigate, and as it uses
a searchsort, if there's no data on the days you want, it will move to the
nearest available date.


Created on Fri Sep 14 17:15:48 2018

@author: Jeaic O Cuimin
"""

import numpy
import matplotlib.pylab as plt
from PyAstronomy.pyTiming import pyPDM
import scipy.stats
import pandas as pd
#read the real data
"""mv_data=pd.read_pickle("AAVSO_processed_moving")
print(mv_data)
mv_data=mv_data.interpolate(method='linear')
print(mv_data)
lowerdate='1934-01-08'
upperdate='1945-01-02'
mv_period_slice=mv_data[lowerdate:upperdate]
mvps=mv_period_slice.reset_index()
mvps0=mvps.index.values
mvps1=mvps.Magnitude.values
print(mvps0, mvps1)"""

#fixed data
fx_data=pd.read_pickle("AAVSO_full_dataset_cleanup")
loweryear=1950
upperyear=2018
lowerdate=fx_data.index.searchsorted(pd.datetime(loweryear,1,1))
upperdate=fx_data.index.searchsorted(pd.datetime(upperyear,1,1))
fx_period_slice=fx_data[lowerdate:upperdate]
fx_period_slice=fx_period_slice.dropna()
fxps=fx_period_slice.reset_index()
fxps0=fxps.index.values
fxps1=fxps.Magnitude.values
print(fxps0, fxps1)
#the day averages
NO=10
#here since we have a lot of data, BinUp is the number of points per bin.
#has strong effect on the pvalue, needs to be big enough to contain fundamental
BinUp=2500
#going to have to change the datetime index to a daycount index if i want halfway decent results



#============================================================================
#==========================simulated======================================
#==========================dataset=========================================
#============================================================================
"""
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
y1=y+noise"""
#============================================================================
#============================================================================
#============================================================================
#============================================================================

# Get a ``scanner'', which defines the frequency interval to be checked.
# Alternatively, also periods could be used instead of frequency.
S = pyPDM.Scanner(minVal=0.5, maxVal=BinUp, dVal=.1, mode="period")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``period'') and associated Theta statistic (t).

#here is where we feed te data
P = pyPDM.PyPDM(fxps0, fxps1)   #fixed data
#P = pyPDM.PyPDM(mvps0,mvps1)    #moving data

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
        #then: minima.append(f2[i]) 
        #if using 10d means
        then: minima.append(f2[i]*NO) 
        theta.append(t2[i])
minima= [ '%.2f' % elem for elem in minima ]

theta=numpy.asarray(theta)
fvalue=1./theta
p_value = scipy.stats.f.cdf(fvalue, len(fxps0)-1,BinUp-M)
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

#props will set up the conditions we like for the textbox in the graphs
props = dict(boxstyle='round', facecolor='indigo', alpha=0.9)


#create each subplot for the input and output:
#input
plt.style.use('dark_background')
plt.subplot(2,1,1)
plt.title('Z-UMa data for:' + str(loweryear) + " to "+ str(upperyear))
plt.scatter(fx_period_slice.index,fxps1, s=2, color='magenta')
plt.ylim(max(fxps1)+0.1, min(fxps1)-0.1)
plt.ylabel('Magnitude')
plt.xlabel('Days')
#plt.text(1,1,'input period 1 =' +str(period_1)+ "[days] \n "+" input period 2=" +str(period_2)+'[days]'+"\n "+" input period 3=" +str(period_3)+'[days]' + "\n Noise= normal dist with std of "+ str(stddevs),fontsize=7, bbox=props)
plt.tight_layout()
plt.grid(True)
#output
plt.subplot(2,1,2)
plt.title("Result of PDM analysis ")
plt.xlabel("Period[days]")
plt.ylabel("Theta")
plt.text(850,0.85,'output periods are: \n' + str(stat_significant['Id Period'])+'',fontsize=7, bbox=props)
plt.grid(True)
#if using 10 day  etc
plt.plot(f2*NO, t2, 'gp-')
#plt.plot(f1*NO,t1, 'rp-')
#if using daycount
#plt.plot(f2, t2, 'gp-')
#plt.plot(f1,t1, 'rp-')
plt.legend([" Bins without covers","Bins with covers"])
plt.tight_layout()

plt.show()
