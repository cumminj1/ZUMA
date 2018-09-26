# -*- coding: utf-8 -*-
"""
date conversion test script
"""
import convertdate
from convertdate import julianday
from convertdate import gregorian

import pandas as pd
import numpy as np

AAVSO1= pd.read_excel('ZUMa_AFOEV_AAVSO.xlsx', sheet_name='ZUMa_4Mar1920_1Mar2012_aavsodat')
jul=AAVSO1['JD']

#empty list to store values
output=[]

#loop through the data and append the empty list with
#the converted dates
for i in range(1,83686):
    result= julianday.to_gregorian(jul[i])
    output.append(result)
    
#output1=list(output)
#output1=[n.replace(', ','-')for n in output1]
#print (output1)

#write the results to a dataframe and then output via csv
df=pd.DataFrame(np.array(output))
df.to_csv('time_conversion.csv',encoding='utf-8', sep=' ')
<<<<<<< HEAD
#print(greg)
=======
#print(greg)
>>>>>>> 46dd9a4b96afb2f67019e7bd78d5b7a97a9454fc
