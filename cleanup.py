#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is a revised version of the datafiltering script
used to clean up the large amateur datasets. The script uses 
max and minimum magnitude filters, and allows you to filter by 
user also. The data are then grouped by N-day means, using both
fixed and moving means.

Data should be read from a pickle format to save on readtime

Created on Wed Oct 10 15:12:00 2018

@author: Jeaic O Cuimin
"""

#import the relevant packages
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from PyAstronomy.pyTiming import pyPDM
import numpy as np
import matplotlib.dates as mdates


#the columns needed are:
#"Observer"
#"Magnitude"
#Datetime index: "Gregorian"
#AAVSO1=pd.read_pickle("AAVSO2012")
#AAVSO1=pd.read_pickle("AAVSOCCD")
AAVSO1=pd.read_pickle("AFOEV")

#we set ndays to be the number of days we want our averages to cover
ndays="7d"
ndaysfix=7

occur=Counter(AAVSO1['Observer'])
print(" ")
print ("The total number of observers, with their number of entries are: ")
print (occur)
print(" ")


#We create an empty list of approved users and "no" sets out how far down the list of most prolific we go
#here 147 is chosen so as to exlude those with under 100 observations
safe=[]
no=5

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

#filter by user and assign the filtered dataset a variable
filtered=AAVSO1[AAVSO1.Observer.isin(safe)]

#print (AAVSO1)
print(" ")
print(" ")
print(" ")
print(" ")

#magntidue must be made of floats to filter it properly
#we have to convert the dtype of the magnitude column; reading as object!!
float_mag=pd.to_numeric( filtered['Magnitude'], errors='coerce')
print ("making columns float has been successful")


#let's now add the second filter by extreme magnitude
filtered2=filtered[(float_mag > 6.0) & (float_mag< 11)]

print("the float magnitude has been successfully filtered to 6<mag<9.6")

#now reassign the column variables to the filtered data
obs_filt=filtered2['Observer']


date=filtered2["Gregorian"]

mag_filt=filtered2['Magnitude']
calendar=pd.to_datetime(date, errors='coerce')


#confirm that our data are all the correct and same length
#as one another
print("the length of observers: " + str(len(obs_filt)))
print("the length of magnitude: "+ str(len(mag_filt)))
print("the length of date: "+ str(len(date)))
print("the length of converted date: "+ str(len(filtered2.index)))

filtered4=pd.DataFrame(filtered2.Magnitude)
#confirming the index is properly datetime
print(filtered4.index)

#before rolling mean, the timeindex must be sorted
filtered4=filtered4.sort_index()


#here we apply .rolling and .mean to get a rolling mean the first kwarg can be an integer or timeperiod
#we use the timeperiod so the data is gropued by timeperiod rather than the number of entries
daymean=filtered4.rolling(ndays,min_periods=1 ).mean()
daymean=daymean[~daymean.index.duplicated(keep='first')]
#daymean.to_pickle("AAVSO_processed_moving")
daymean.to_pickle("AFOEV_processed_moving")
print("The rolling mean magnitude values (visual) are: ")
print(daymean)


#fixed test is the data with fixed 10d averages
filtered4.Magnitude=pd.to_numeric( filtered4['Magnitude'], errors='coerce')
fixedtest=filtered4.resample(ndays).mean()


#fixedtest.to_pickle("AAVSO_processed_fixed")
fixedtest.to_pickle("AFOEV_processed_fixed")
#plt.figure()
fig,(ax1, ax2)=plt.subplots(nrows=2,ncols=1)

#plot the fixed averages
fixedtest.plot(ax=ax1,style='c.', title="%i day fixed averages of ZUMa" %ndaysfix)
ax1.set_ylabel('Apparent Visual Magnitude')
ax1.set_ylim(max(fixedtest.Magnitude)+0.1, min(fixedtest.Magnitude)-0.1)
ax1.grid(b=True, which='minor',  linewidth=.5)
ax1.grid(b=True, which='major',  linewidth=1)
#plt.plot(AAVSOccd["Gregorian"], AAVSOccd["Magnitude"], 'r.')
plt.tight_layout()

#plot the moving averages
daymean.plot(ax=ax2,style='m.', title="%s moving averages of ZUMa" %ndays)
ax2.set_ylabel('Apparent Visual Magnitude')
ax2.set_ylim(max(daymean.Magnitude)+0.1, min(daymean.Magnitude)-0.1)
ax2.grid(b=True, which='minor',  linewidth=.5)
ax2.grid(b=True, which='major',  linewidth=1)
plt.tight_layout()