#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:30:13 2018

@author: CUMMINJ1
"""

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

folder='/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/'








for filename in os.listdir(folder):
     if filename.endswith(".fit"):
         print(filename)
         spectrum_1=fits.open(str(folder)+'/'+str(filename))
         print('spectrum 1 successful')
         spectrum_2=pyasl.read1dFitsSpec(str(folder)+'/'+str(filename))      
         hdu=spectrum_1[0]
         hdu_2=spectrum_1[0].data
         start_time=hdu.header['JD-OBS']
         mid_time=hdu.header['JD-MID']
         wl=spectrum_2[0]
         flux=spectrum_2[1]
         plt.style.use('dark_background')
         plt.plot(wl,flux, label=("Julian: "+str(mid_time)))
         plt.title("Spectral data for Z-UMa" )
         plt.xlabel("Wavelength [Angstroms]")
         plt.ylabel("Flux [erg/cm2/s/A]")
         plt.xlim(3750,8000)
         plt.ylim(0, 7e-11)
         plt.legend()
         plt.savefig("/cphys/ugrad/2015-16/JF/CUMMINJ1/zuma/2014_spectra/spectrum_"+str(filename)+".png")
         plt.close()
         #plt.show()
     else:
        print('none found')