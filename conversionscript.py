# -*- coding: utf-8 -*-
"""
date conversion test script
"""

from convertdate import julianday
from openpyxl import load_workbook
import pandas as pd
import numpy as np

AAVSO1= pd.read_excel('ZUMa_AFOEV_AAVSO.xlsx', sheet_name='ZUMa_4Mar1920_1Mar2012_aavsodat')

#take the specific date column needed
jul=AAVSO1['JD']

#empty list to store values
output=[]

#loop through the data and append the empty list with
#the converted dates
for i in range(1,83686):
    result= julianday.to_gregorian(jul[i])
    output.append(result)
    
#write the results to a dataframe and then output via csv
df=pd.DataFrame(np.array(output))
#df.to_csv('time_conversion.csv',encoding='utf-8', sep=' ')

path= r"/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/ZUMa_AFOEV_AAVSO.xlsx"
print("path read")

book=load_workbook(path)
print("book loaded")
writer=pd.ExcelWriter(path, engine='openpyxl')
writer.book=book
df.to_excel(writer, sheet_name='gregorian_dates', index='False')
print("Gregorian Dates written to file")

writer.save()
print("sheet has been saved to " + str(path))