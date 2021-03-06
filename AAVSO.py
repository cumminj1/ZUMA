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
#AAVSO1= pd.read_excel('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/ZUMa_AFOEV_AAVSO.xlsx', sheet_name='ZUMa_4Mar1920_1Mar2012_aavsodat', index='False')
#AAVSO1=pd.DataFrame(AAVSO1)
#
AAVSO1=pd.read_pickle("AAVSO2012")


#we set ndays to be the number of days we want our averages to cover
ndays="7d"
ndaysfix=7



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
filtered2=filtered[(float_mag > 6.0) & (float_mag< 9.6)]

print("the float magnitude has been successfully filtered to 6<mag<9.6")

#now reassign the column variables to the filtered data
obs_filt=filtered2['Observer']

#date=filtered2['Calendar Date']
date=filtered2["Gregorian"]

mag_filt=filtered2['Magnitude']
calendar=pd.to_datetime(date, errors='coerce')

#confirm that our data are all the correct and same length
#as one another
print("the length of observers: " + str(len(obs_filt)))
print("the length of magnitude: "+ str(len(mag_filt)))
print("the length of date: "+ str(len(date)))
print("the length of converted date: "+ str(len(calendar)))

"""#now let's move on to the movin averages and statisitics 
group=filtered2.groupby(["Year","Month"])
print("Grouping has been successful")

monthly_averages=group.aggregate({'Magnitude':np.mean})

print("the monthly averages are" + str(monthly_averages))


"""

#plot1=filtered2.groupby(["Year","Month"])['Magnitude'].mean().plot(ax=ax)


"""plot1=filtered2.groupby(["Year","Month"]).mean()['Magnitude']
fig,ax=plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Apparent Visual Magnitude')
ax.set_xticks(range(len(plot1)))
ax.set_xticklabels(["%s-%01d" % item for item in plot1.index.tolist()], rotation=0)
plot1.plot(ax=ax)"""


#let's try and refine the search a bit, lets try 7
#day means

#here Im setting the index to be a datetime format
filtered3=filtered2.set_index(calendar)
#refining search to just magnitude
filtered4=pd.DataFrame(filtered3.Magnitude)
#confirming the index is properly datetime
print(filtered4.index)

#before rolling mean, the timeindex must be sorted
filtered4=filtered4.sort_index()


#here we apply .rolling and .mean to get a rolling mean the first kwarg can be an integer or timeperiod
#we use the timeperiod so the data is gropued by timeperiod rather than the number of entries
daymean=filtered4.rolling(ndays,min_periods=1 ).mean()
daymean=daymean[~daymean.index.duplicated(keep='first')]
daymean.to_pickle("AAVSO_processed_moving")
print(daymean)

#fixed test is the data with fixed 10d averages
fixedtest=filtered4.resample(ndays).mean()
fixedtest.to_pickle("AAVSO_processed_fixed")
#plt.figure()
fig,(ax1, ax2)=plt.subplots(nrows=2,ncols=1)

#plot the fixed averages
fixedtest.plot(ax=ax1,style='.', title="%i day fixed averages of ZUMa" %ndaysfix)
ax1.set_ylabel('Apparent Visual Magnitude')
ax1.set_ylim(max(fixedtest.Magnitude), min(fixedtest.Magnitude))
ax1.grid(True)
plt.tight_layout()

#plot the moving averages
daymean.plot(ax=ax2,style='.', title="%s moving averages of ZUMa" %ndays)
ax2.set_ylabel('Apparent Visual Magnitude')
ax2.set_ylim(max(daymean.Magnitude), min(daymean.Magnitude))
ax2.grid(True)
plt.tight_layout()

















