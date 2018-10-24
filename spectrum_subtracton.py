#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script to identify mechanisms of change in red giants
by subtracting reference spectra from the observed spectra
at minimum and maximum (and later in between)
Created on Thu Oct 18 15:28:05 2018

@author: CUMMINJ1
"""
import matplotlib.pyplot as plt
from astropy.io import fits
from PyAstronomy import pyasl
import os 
import pandas as pd
import numpy as np
import scipy.interpolate as interp
import heapq
#dark background easier on the eyes
plt.style.use('dark_background')

#getting the scaels of the flux to match
scale_factor=6e11
scale_factor_1=5.9e10
#matching the curve positions for reference
translation_factor=0.45
#The spectrum for maximum
spectrum_max=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/_zuma_20140709_946_D_Boyd_flux.fit')
wl_max=spectrum_max[0]
flux_max=spectrum_max[1]

#the spectrum for minimum
spectrum_minimum=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/_zuma_20140401_932_D_Boyd_flux.fit')
wl_min=spectrum_minimum[0]
flux_min=spectrum_minimum[1]
#the m7III reference spectrum
spectrum_m3=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/ref_spectra/m7iii.fits')
wl_m3=spectrum_m3[0]
flux_m3=spectrum_m3[1]
#the m4iii referecne spectrum
spectrum_m4=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/ref_spectra/m4iii.fits')
wl_m4=spectrum_m4[0]
flux_m4=spectrum_m4[1]


#empty lists for the reference spectra
wl_ref=[]
flux_ref=[]
#and for the max
wl_ref_max=[]
flux_ref_max=[]


#loop through and take only values which fall in the same 
#wavelength as the Dr Boyd measurements
for i in range( len(wl_m3)):
    if wl_m3[i] < 7600 and wl_m3[i] > 3750:
        wl_ref.append(wl_m3[i])
        flux_ref.append(flux_m3[i])

#and the same for the maximum
for i in range( len(wl_m3)):
    if wl_m4[i] < 7600 and wl_m4[i] > 3750:
        wl_ref_max.append(wl_m4[i])
        flux_ref_max.append(flux_m4[i])
        


#apply the scale and translation
flux_min=(flux_min*scale_factor)+(translation_factor)
flux_max=(flux_max*scale_factor_1)+(translation_factor)
#convert to a numpy array
wl_ref=np.asarray(wl_ref)
flux_ref=np.asarray(flux_ref)
wl_ref_interp=wl_ref-20.1

#and the same for the maximum
wl_ref_max=np.asarray(wl_ref_max)
flux_ref_max=np.asarray(flux_ref_max)


#trying to reshape the reference and observer data to have to same 
#dimensions to make them easier to compare

#compressing to the size of the reference spectrum [wavelength axis]
"""wl_min_interp=interp.interp1d(np.arange(wl_ref.size), wl_ref,fill_value="extrapolate")
wl_min_compress= wl_min_interp(np.linspace(0, wl_min.size-1, wl_ref.size))"""

#compressing to the size of the reference spectrum [flux axis]
flux_min_interp=interp.interp1d(np.arange(flux_min.size), flux_min, fill_value="extrapolate")
flux_min_compress=flux_min_interp(np.linspace(0, flux_min.size-1, flux_ref.size))

flux_max_interp=interp.interp1d(np.arange(flux_max.size), flux_max, fill_value="extrapolate")
flux_max_compress=flux_max_interp(np.linspace(0, flux_max.size-1, flux_ref_max.size))
print("Interpolation successful..." )
print("Preparing to plot..." )

#now It's time to subtract them and see what's what
spectral_difference_min= -flux_ref+flux_min_compress
spectral_difference_max=-flux_ref_max+flux_max_compress
#ind_min=np.argpartition(spectral_difference_min, -5)[-5:]
ind_min = (spectral_difference_min).argsort()[-20:][::-1]
ind_max=(spectral_difference_max).argsort()[-20:][::-1]
min_vals= wl_ref[ind_min]
max_vals=wl_ref[ind_max]
print("The peaks in the spectrum at min: "+str(min_vals))
print(" ")
print("The peaks in the spectrum at max"+str(max_vals))
fig=plt.figure
#ploting the  reference spectrum beside the observed spectrum
#plt.plot(wl_min,flux_min, color='m', label='spectrum at minimum [2014]')
plt.subplot(2,2,1)
plt.plot(wl_ref,flux_ref/10, color='c', label='reference spectrum  M7III', alpha=0.5, linestyle='--') #m7iii plot
plt.plot(wl_ref_interp, flux_min_compress/10, color='m', label='Spectrum at minimum [2014]' ) #the minimum
plt.title("Spectrum at minimum")
plt.xlabel("Wavelength [$\AA$]")
plt.ylabel("Flux [reference]")
plt.legend()
plt.grid(linestyle='--', alpha=0.2)
plt.tight_layout()

#the difference plot at min
plt.subplot(2,2,2)
plt.plot(wl_ref, spectral_difference_min, label="Observed Min - M7iii ")
plt.axhline()
plt.xlabel("Wavelength [$\AA$]")
plt.ylabel("Flux [reference]")
plt.title("Observed vs Reference - MIN")
plt.tight_layout()
plt.xlim([3750,7600])
plt.legend()

#for the star at a max
plt.subplot(2,2,3)
plt.plot(wl_ref_interp, flux_max_compress, color='r', label='Spectrum at max [2014]')#the maximum
plt.plot(wl_ref_max, flux_ref_max, color='w', label="Reference spectrum M4III", alpha=0.5, linestyle='--')#M4iii plot
plt.title("Spectrum at maximum")
plt.xlabel("Wavelength [$\AA$]")
plt.ylabel("Flux [reference]")
plt.tight_layout()
plt.legend()
plt.grid(linestyle='--', alpha=0.2)


#the difference plot at max
plt.subplot(2,2,4)
plt.plot(wl_ref, spectral_difference_max, label="Observed Max - M4ii ")
plt.axhline()
plt.xlabel("Wavelength [$\AA$]")
plt.ylabel("Flux [reference]")
plt.title("Observed vs Reference - MAX")
plt.tight_layout()
plt.xlim([3750,7600])
plt.legend()
plt.show()
