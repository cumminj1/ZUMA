# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:09:02 2018

@author: jeaic
"""

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


# pull the date and magnitude into lists
AAVSO1= pd.read_excel('AFOEV.xlsx', sheetname='ZUMa_AFOEV')

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
no=83



#for loop through the observers, taking the observers with greatest number of observations
#we appent the list.
for value, count in occur.most_common():
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

#now reassign the column variables to the filtered data
obs_filt=filtered['Observer']
mod_jul_filt=filtered['Modified Julian Date']
mag_filt=filtered['Magnitude']


#we check the observers' counts to ensure filter works
occur_filt=Counter(filtered['Observer'])
print("The number of observations for each approved user is:")
print(" ")
print(" ")
print (occur_filt)





#plot the cleaned up data
plt.plot(mod_jul_filt,mag_filt,'r.')
plt.xlabel('modified julian date')
plt.ylabel('approx vis magnitude')
plt.title(" AFOEV amateur data on ZUMa using top " + str(no) +  " observers' data")