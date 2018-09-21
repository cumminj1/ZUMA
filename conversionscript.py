# -*- coding: utf-8 -*-
"""
date conversion test script
"""
import convertdate
from convertdate import julian
from convertdate import gregorian

import pandas as pd

AAVSO1= pd.read_excel('ZUMa_AFOEV_AAVSO.xlsx', sheet_name='ZUMa_4Mar1920_1Mar2012_aavsodat')
jul=AAVSO1['JD']


x=julian.monthcalendar(2018,3)
print (x)

#est= ju


output=[]
#greg=julian.gregorian_from_jd(jul)

for i in (jul):
    result= julian.to_gregorian(jul1[i])
    output.append(result)
    i=+1

print (output)
#print(greg)