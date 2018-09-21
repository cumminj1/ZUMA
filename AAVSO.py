# -*- coding: utf-8 -*-
"""
plotting the recent ZUMA data from AFOEV
updated to deal with larger datasets


Created on Wed Sep 12 17:53:56 2018
Last edited Thur Sep 13 2018

@author: jeaic
"""

#import the relevant packages
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from PyAstronomy.pyTiming import pyPDM
import numpy as np

# pull the date and magnitude into lists
AAVSO1= pd.read_excel('AAVSO.xlsx', sheetname='AAVSO_filter')

#assign the columns of interest variables
Observer=AAVSO1['Observer']
mod_jul=AAVSO1['Modified Julian Date']
mag=AAVSO1['Magnitude']


#we count how many observations each observer made
#this allows us to remove the fairweather observers
occur=Counter(AAVSO1['Observer'])
print(" ")
print ("The total number os observers, with their number of entries are: ")
print (occur)
print(" ")
print(" ")
print(" ")
print(" ")


#We create an empty list of approved users and "no" sets out how far down the list of most prolific we go
#here 147 is chosen so as to exlude those with under 100 observations
safe=[]
no=147



#for loop through the observers, taking the observers with greatest number of observations
#we appent the list.
for value, count in occur.most_common(no):
    safe.append(value)
    
print("The users stored for use are" + str(safe))
print(" ")
print(" ")
print(" ")
print(" ")


#we apply filter that our users must be the only ones
AAVSO1.Observer.isin(safe)

#assign the filtered dataset a variable
filtered=AAVSO1[AAVSO1.Observer.isin(safe)]
print (filtered)
print(" ")
print(" ")
print(" ")
print(" ")

#lets now add the second filter by extreme magnitude
filtered2=filtered[(filtered.Magnitude > 6) | (filtered< 9.6)]

#now reassign the column variables to the filtered data
obs_filt=filtered2['Observer']
mod_jul_filt=filtered2['Modified Julian Date']
mag_filt=filtered2['Magnitude']


#we check the observers' counts to ensure filter works
occur_filt=Counter(filtered['Observer'])
print (occur_filt)

#in hindsight this was a terrible idea; figure out a better way of making 
#1 month averages
#want to make a way to average in groups of N to reduce the number of datapoints





























"""
N=100
def groupedAvg(myArray, N):
    result = np.cumsum(myArray, 0)[N-1::N]/float(N)
    result[1:] = result[1:] - result[:-1]
    return result



print ("this is the value of N......................"+str(N))
mod_jul_filt_avg=groupedAvg(mod_jul_filt, N)
mag_filt_avg=groupedAvg(mag_filt, N)
"""
"""
#plot the cleaned up data
plt.plot(mod_jul_filt,mag_filt,'r.')
plt.xlabel('modified julian date')
plt.ylabel('approx vis magnitude')
plt.title(" AAVSO data on ZUMa using top " + str(no) +  " observers' data")
plt.show()
"""
































# Get a ``scanner'', which defines the frequency interval to be checked.
# Alternatively, also periods could be used instead of frequency.
S = pyPDM.Scanner(minVal=0.5, maxVal=500, dVal=0.1, mode="frequency")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``frequency'') and associated Theta statistic (t).
# Use 10 phase bins and 3 covers (= phase-shifted set of bins).
P = pyPDM.PyPDM(mod_jul_filt_avg, mag_filt_avg)
#f1, t1 = P.pdmEquiBinCover(3, 6, S)
# For comparison, carry out PDM analysis using  bins (no covers).
f2, t2 = P.pdmEquiBin(100, S)




#plot the cleaned up data
plt.subplot(2,1,1)
plt.plot(mod_jul_filt_avg,mag_filt_avg,'r.')
plt.xlabel('modified julian date')
plt.ylabel('approx vis magnitude')
plt.title("AAVSO recent data on ZUMa")

plt.subplot(2,1,2)
plt.title("Result of PDM analysis ")
plt.xlabel("Frequency")
plt.ylabel("Theta")
#plt.plot(f1, t1, 'bp-')
plt.plot(f2, t2, 'gp-')
#plt.xticks(numpy.arange(min(f2)+0.5, max(f2)+1.5,1.0))
plt.legend([" Bins without covers"])
plt.show()
















