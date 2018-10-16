# -*- coding: utf-8 -*-
"""
This script will import large datasets with the date in 
Julian Day count and add append a column which has a Gregorian date.
This is merely to make the timeperiods easier to identify from a human 
perspective.

The data is imported, converted to panda dataframe and saved using a pickle
which can be used by other scripts and will save considerable time over having
to read the data each time you want to use it.

Jeaic O Cuimin
"""

from convertdate import julianday
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#AAVSO1= pd.read_excel('ZUMa_AFOEV_AAVSO.xlsx', sheet_name='ZUMa_4Mar1920_1Mar2012_aavsodat').dropna()
#AAVSO2016=pd.read_csv("CCD.csv", sep=',', header=0)
AAVSO2016=pd.read_csv("AAVSO_full_dataset.csv", sep=',', header=0)
AAVSO2016=AAVSO2016.reindex()
#take the specific date column needed
#jul=AAVSO1['JD']

obs2012=AAVSO2016['Observer']
jul2012=AAVSO2016['JD']
mag2012=AAVSO2016['Magnitude']

#empty list to store values
output2012=[]
for i in range(1,len(jul2012)-1):
    result= julianday.to_gregorian(jul2012[i])
    output2012.append(result)
#write the results to a dataframe and then output via csv
#df=pd.DataFrame(np.array(output))
df2012=pd.DataFrame(np.array(output2012))
df2012=df2012.join(mag2012)
df2012=df2012.join(obs2012)
df2012=df2012.join(jul2012)
df2012[0]=df2012[0].astype(str)+"-"
df2012[1]=df2012[1].astype(str)+"-"
df2012['Gregorian']=df2012[[0,1,2]].astype(str).sum(axis=1)
df2012["Gregorian"]=pd.to_datetime(df2012["Gregorian"], errors='coerce')
df2012=df2012.drop(columns=[0,1,2])
df2012=df2012.set_index(df2012["Gregorian"])
print(df2012)
#df2012.to_pickle("AAVSOCCD")
df2012.to_pickle("AAVSO_full_dataset_conversion")












