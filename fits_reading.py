#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is for reading FITS datafiles and moving them 
to a point where they can be read by pandas to incorporate them 
into my datetime dataframes.

Created on Mon Oct 15 11:00:40 2018

@author: Jeaic O Cuimin
"""
import matplotlib.pyplot as plt
from astropy.io import fits
from PyAstronomy import pyasl

#open the file
spectrum_1= fits.open('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/_zuma_20140713_934_D_Boyd_flux.fit')
spectrum_2=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/_zuma_20140721_936_D_Boyd_flux.fit')
#lets see what overview we can get

#first lets get the basic information
print(" ")
print(str(spectrum_1.info()))
print(" ")

#lets check the heaer unit
print("the header data unit is")
print(" ")
hdu=spectrum_1[0]
print(hdu)
print(" ")

#now for the shape of the data
print(hdu.data.shape)
print(" ")

print(hdu.header)
print(" ")

start_time=hdu.header['JD-OBS']
mid_time=hdu.header['JD-MID']

print('Observation was started at: ['+ str(start_time) +"] in Julian Day")
print(" ")
print("Observation mid-point was at: [" + str(mid_time)+ "] in Julian Day")

plt.imshow(spectrum_2)
#plt.figure()
#