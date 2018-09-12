# -*- coding: utf-8 -*-
"""
plotting the recent ZUMA data from AFOEV


Created on Wed Sep 12 17:53:56 2018

@author: jeaic
"""
#import the relevant packages
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


# pull the date and magnitude into lists
afoev= pd.read_excel('ZUMa_recent_AFOEV_noNTS.xlsx', sheetname='Sheet1')
mod_jul=afoev['Modified Julian Date']
mag=afoev['Visual magnitude']

#we need to see the fairweather observers
#use counter to determine the number of times
#observer has taken measurements
occur=Counter(afoev['Observer'])
print (occur)
#this allows us to remove inconsistent observers




#plot the cleaned up data
plt.plot(mod_jul,mag,'ro')
plt.xlabel('modified julian date')
plt.ylabel('approx vis magnitude')
plt.title("AFOEV recent data on ZUMa")
plt.show()