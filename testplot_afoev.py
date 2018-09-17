# -*- coding: utf-8 -*-
"""
plotting the recent ZUMA data from AFOEV


Created on Wed Sep 12 17:53:56 2018

@author: jeaic
"""
#import the relevant packages
import pandas as pd
import matplotlib.pyplot as plt
#from collections import Counter
from PyAstronomy.pyTiming import pyPDM
import numpy 


# pull the date and magnitude into lists
afoev= pd.read_excel('ZUMa_recent_AFOEV_noNTS.xlsx', sheetname='Sheet1')
mod_jul=afoev['Modified Julian Date']
mag=afoev['Visual magnitude']

#we need to see the fairweather observers
#use counter to determine the number of times
#observer has taken measurements
#occur=Counter(afoev['Observer'])
#print (occur)
#this allows us to remove inconsistent observers


# Get a ``scanner'', which defines the frequency interval to be checked.
# Alternatively, also periods could be used instead of frequency.
S = pyPDM.Scanner(minVal=0.5, maxVal=250.0, dVal=.1, mode="frequency")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``frequency'') and associated Theta statistic (t).
# Use 10 phase bins and 3 covers (= phase-shifted set of bins).
P = pyPDM.PyPDM(mod_jul, mag)
#f1, t1 = P.pdmEquiBinCover(3, 6, S)
# For comparison, carry out PDM analysis using  bins (no covers).
f2, t2 = P.pdmEquiBin(10, S)




#plot the cleaned up data
plt.subplot(2,1,1)
plt.plot(mod_jul,mag,'r.')
plt.xlabel('modified julian date')
plt.ylabel('approx vis magnitude')
plt.title("AFOEV recent data on ZUMa")

plt.subplot(2,1,2)
plt.title("Result of PDM analysis ")
plt.xlabel("Frequency")
plt.ylabel("Theta")
#plt.plot(f1, t1, 'bp-')
plt.plot(f2, t2, 'gp-')
#plt.xticks(numpy.arange(min(f2)+0.5, max(f2)+1.5,1.0))
plt.legend([" Bins without covers"])
plt.show()