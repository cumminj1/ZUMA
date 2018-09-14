Z-Ursae Majoris is a late-type, semi-regular red giant star (SRb). Magnitude typically varies by 2 magnitudes
Amateur observations, primarily from AAVSO & AFOEV will be cleaned up and compared to limited CCD data to determine
its reliability, such that the nature of the aperiodicity can be determined (overtones of the fundamental frequency?).
Given the shape of this data, a simple DFT or FFT is unlikely to work, and as such it is planned that the data will
be binned and analysed using PDM, or "phase dispersion minimisation" using a python code
adapted from the original method of Stellingwerf.

It may be possible to obtain spectrographic data of the star, however it is currently unclear as to whether this 
data will be useful.

It may also be worth comparing this star to other stars with similar classifications such as MIRA or RV Tauri stars.

Tue, 11 Sept 2018

____________________________________________________________________________________
____________________________________________________________________________________

Having read a paper on R Doradus by T.R. Bedding et al (Mode switching in the nearby Mira-like variable R Doradus), I have come across another technique to use alongside (or in place of?) phase dispersion minimisation. Paper refers to wavelet analysis- specifically
Weighted Wavelet Z-transform (WWZ for frequency acquisition), and Weighted Wavelet Amplitude (WWA for Amplitude acquistion). The two are used in conjunction.

I have plotted recent data from the AFOEV database on ZUMa and removed what I have deemed 'inconsistent observers'; that is an observer named NTS whose observations were almost perfectly static and clear outliers. I have also removed the observers that I consider to be 'fairweather observers'- those with 10 or fewer observations. The data of the observers: NTS, DPV, STM, PRO, POY, BDJ,FSJ,BVE, CAS, AKG, ANC, GGU, HOK, BEN, STO, has been purged.

The resulting plot was cleaner, although there are still muddy sections, even among the consistent observers. These
consistent observers have been colour-coded in a spreadsheet, corresponding to the number of observations and/or their
regularity of observation. I have attached two .png files which show the set prior-to, and post purge.

Wed, 12 Sept 2018

_____________________________________________________________________________________
_____________________________________________________________________________________

Spent the day working on a python script which reads the database, and allows for filtering by user by the number
of datapoints they have contributed, and subsequently plots the new data. With the fairweather observers removed
there is a much clearer sense of periodicity, however there is more to be done. I plan on binning data into 5-10
day intervals which will hopefully clear things up even further and then polish by removing any remaining outliers.
This script should be easy to apply to AFOEV data, but has been thus far only applied to the AAVSO data.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/AAVSO_raw.png)

![alt text](https://github.com/cumminj1/ZUMA/blob/master/AAVSO_TOP_USERS.png)
Thurs, 13 Sept 2018
 
____________________________________________________________________________________
____________________________________________________________________________________
Started day by modifiying the parameters of the AAVSO filtering script to suit the AFOEV amateur
data. This Dataset has a large period of no measurement once fairweather observers are removed.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/AFOEV_raw.png)
![alt text](https://github.com/cumminj1/ZUMA/blob/master/AFOEV_fairweather_removed.png)

I have been experimenting with the PyAstronomy package in python and using its built-in
phase dispersion minimmisation module, and have tested it on artificial data. In this case 
the data consisted of three convoluted sinusoidals, with freqeuncies of 3Hz, 7Hz, and 11Hz.
As can be seen from the image below, it would seem that the script is running as hoped, although
there is some small spread from the theoretical result.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/pdm_3_7_11.png)
