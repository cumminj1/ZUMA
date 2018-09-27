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
import matplotlib.dates as mdates
# pull the data and convert it to a dataframe for pandas
AAVSO1= pd.read_excel('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/ZUMa_AFOEV_AAVSO.xlsx', sheet_name='ZUMa_4Mar1920_1Mar2012_aavsodat', index='False')
AAVSO1=pd.DataFrame(AAVSO1)

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
no=50

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
filtered2=filtered[(float_mag > 6.0) & (float_mag< 9.6)]

print("the float magnitude has been successfully filtered to 6<mag<9.6")

#now reassign the column variables to the filtered data
obs_filt=filtered2['Observer']
date=filtered2['Calendar Date']
mag_filt=filtered2['Magnitude']
calendar=pd.to_datetime(date, errors='coerce')

#confirm that our data are all the correct and same length
#as one another
print("the length of observers: " + str(len(obs_filt)))
print("the length of magnitude: "+ str(len(mag_filt)))
print("the length of date: "+ str(len(date)))
print("the length of converted date: "+ str(len(calendar)))

#now let's move on to the movin averages and statisitics 
group=filtered2.groupby(["Year","Month"])
print("Grouping has been successful")

monthly_averages=group.aggregate({'Magnitude':np.mean})

print("the monthly averages are" + str(monthly_averages))

plot1=filtered2.groupby(["Year","Month"])['Magnitude'].mean()
#plot2=plot1.unstack('Month').loc[:, 'Magnitude']
#plot2.index=pd.PeriodIndex()
fig,ax1=plt.subplots()

plot1.plot()


ax1.xaxis.set_major_locator(mdates.YearLocator(2))
ax1.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))

plt.xticks(rotation=45)
plt.ylabel("Apparent Visual Magnitude")
plt.show()






#plt.plot(monthly_averages.Magnitude)
#plt.show()
"""
#create the basis of the plot
fig,ax1=plt.subplots()
plt.plot(calendar, mag_filt, 'g.')

#add the title
plt.title("TEST3: AAVSO measurements of ZUMa Magnitude")
plt.ylabel("Apparent Visual Magnitude")
#add the date based locations
print("title check")
ax1.xaxis.set_major_locator(mdates.YearLocator(2))
ax1.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
print("Major Locator Check")

plt.xticks(rotation=45)
print("Tick Rotation check")
plt.grid(True)
plt.show()

#we check the observers' counts to ensure filter works
'''occur_filt=Counter(filtered['Observer'])
print (occur_filt)'''
"""









#PDM analysis can stay away for the time being
"""
# Get a ``scanner'', which defines the frequency interval to be checked.
# Alternatively, also periods could be used instead of frequency.
S = pyPDM.Scanner(minVal=0.5, maxVal=500, dVal=1, mode="frequency")

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``frequency'') and associated Theta statistic (t).
# Use 10 phase bins and 3 covers (= phase-shifted set of bins).
P = pyPDM.PyPDM(mod_jul_filt, mag_filt)
#f1, t1 = P.pdmEquiBinCover(3, 6, S)
# For comparison, carry out PDM analysis using  bins (no covers).
f2, t2 = P.pdmEquiBin(10, S)



#plot the cleaned up data
plt.subplot(2,1,1)
plt.plot(mod_jul_filt,mag_filt,'r.')
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
"""





