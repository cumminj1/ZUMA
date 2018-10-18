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
import scipy as sp
plt.style.use('dark_background')
scale_factor=6e11
translation_factor=0.5

#the spectrum for minimum
spectrum_minimum=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/_zuma_20140401_932_D_Boyd_flux.fit')
wl_min=spectrum_minimum[0]
flux_min=spectrum_minimum[1]
#the m4III reference spectrum
spectrum_m3=pyasl.read1dFitsSpec('/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/ref_spectra/m7iii.fits')
wl_m3=spectrum_m3[0]
flux_m3=spectrum_m3[1]

wl_ref=[]
flux_ref=[]

for i in range( len(wl_m3)):
    if wl_m3[i] < 7600 and wl_m3[i] > 3750:
        wl_ref.append(wl_m3[i])
        flux_ref.append(flux_m3[i])

flux_min=(flux_min*scale_factor)+(translation_factor)

wl_ref=np.asarray(wl_ref)
flux_ref=np.asarray(flux_ref)

wl_min=wl_min.reshape(-1, len(wl_ref))
flux_min=flux_min.reshape(-1, len(flux_ref))

plt.plot(wl_min,flux_min, color='m', label='spectrum at minimum [2014]')
plt.plot(wl_ref,flux_ref, color='c', label='reference spectrum  M7III')
plt.xlabel("Wavelength [$\AA$]")
plt.ylabel
plt.title("Spectrum at minimum")
plt.legend()
plt.grid(False)
plt.show()
