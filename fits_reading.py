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
import os 
import pandas as pd

plt.style.use('dark_background')
folder='/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/ref_spectra'

for filename in os.listdir(folder):
     if filename.endswith(".fits"):
         spectrum_2=pyasl.read1dFitsSpec(str(folder)+'/'+str(filename))  
         wl=spectrum_2[0]
         flux=spectrum_2[1]
         print("Fits file "+str(filename)+ " successfully read")
         plt.plot(wl,flux, alpha=0.25, label=str(filename[:-4]))
         plt.title("Reference Spectra M(n)III stars for Z-UMa" )
         plt.xlabel("Wavelength [Angstroms]")
         plt.ylabel("Flux [erg/cm2/s/A]")
         plt.ylim([0,14])
         plt.xlim(3750,8000)
         #plt.show()

#open the file (minimum)
spectrum_1= fits.open('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/_zuma_20140713_934_D_Boyd_flux.fit')
spectrum_2=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/_zuma_20140401_932_D_Boyd_flux.fit')


spectrum_max=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/_zuma_20140709_946_D_Boyd_flux.fit')
#reference spectrua
#esa
#specref=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/ukm7iii.fits')
specref_1= fits.open('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/ref_spectra/m7iii.fits')
#refwl=specref[0]
#refflux=specref[1]
refhdu=specref_1[0]
#lets see what overview we can get

#first lets get the basic information
print(" ")
print(str(spectrum_1.info()))
print(" ")

#lets check the heaer unit
print("the header data unit is")
print(" ")
hdu=spectrum_1[0]
hdu_2=spectrum_1[0].data
print(hdu)
print(" ")

#now for the shape of the data
print(hdu.data.shape)
print(" ")

m=11.5


print(hdu.header)
print(" ")
print(refhdu.header)
start_time=hdu.header['JD-OBS']
mid_time=hdu.header['JD-MID']

print('Observation was started at: ['+ str(start_time) +"] in Julian Day")
print(" ")
print("Observation mid-point was at: [" + str(mid_time)+ "] in Julian Day")
print(spectrum_2)

wl=spectrum_2[0]
flux=spectrum_2[1]

wl_max=spectrum_max[0]
flux_max=spectrum_max[1]

#plotting the extracted data
#plt.plot(wl,(flux*(3.5*10**(11))+0.45), label=("Julian: "+str(mid_time))+"(minimum)", color='r')
plt.plot(wl_max,(flux_max*(1*10**(11))+0.005), label=("Julian: "+str(mid_time))+"(maximum)", color='g')
#and plotting the reference spectrum
#plt.plot(m7_ref_wl,m7_ref_flux, label=("M7 Reference Spectrum"))
#plt.plot(refwl,refflux*1e-12)
plt.title("Spectral data for Z-UMa, JD" + str(mid_time))
plt.xlabel("Wavelength [Angstroms]")
plt.ylabel("Flux [erg/cm2/s/A]")
plt.legend()
