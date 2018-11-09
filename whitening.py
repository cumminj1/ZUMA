#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Whitening.

The last step in checking for the lesser amplitude harmonics is to
create a signal for the primary which has been identified and then 
to subtract it from the overall original processed signal. The resuling
signals should be easier to identify
Created on Tue Nov  6 10:00:15 2018

@author: CUMMINJ1
"""

import matplotlib.pylab as plt
from PyAstronomy.pyTiming import pyPDM
import scipy.stats
import pandas as pd
import numpy as np

white_raw=pd.read_pickle("white")
start=1970
end=1995
index= np.arange(0,len(white_raw),1)
print(white_raw)
period_1=(193.5)
freq_1=(1/period_1)
#x = np.linspace(start,end,int((365*(end-start)/30)))
x=np.arange(len(white_raw))*30
y = 1*np.sin(x*2.0*np.pi*freq_1)+8

whitened=white_raw.Magnitude - y
print(whitened)

plt.style.use("ggplot")
plt.plot(x,whitened, '.')
plt.show()

#=============================================================
#=============================================================
#=============================================================
#=============================================================
NO=15
#here since we have a lot of data, BinUp is the number of points per bin.
#has strong effect on the pvalue, needs to be big enough to contain fundamental
BinUp=750


S = pyPDM.Scanner(minVal=0.5, maxVal=BinUp, dVal=.1, mode="period")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``period'') and associated Theta statistic (t).

#here is where we feed te data
P = pyPDM.PyPDM(index, whitened)   #fixed data
#P = pyPDM.PyPDM(mvps0,mvps1)    #moving data

f1, t1 = P.pdmEquiBinCover(10, 3, S)
#PDM analysis using  bins (no covers).
M=7

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
#minima= [ '%.2f' % elem for elem in minima ]

theta=np.asarray(theta)
fvalue=1./theta
p_value = scipy.stats.f.cdf(fvalue, len(index)-1,BinUp-M)
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















