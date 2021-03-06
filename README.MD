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

Given this success I have added some moderate noise to the simulated data, to see if the pdm with
the same settings is still able to discern the three frequencies.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/pdm_3_7_11_noise.png)

We can see that PDM has again, successfully identified the thre frequencies found within the convoluted 
function, however the trough corresponding to f=11Hz is much shallower than the previous, noiseless version.

Friday, 14 Sept 2018

_______________________________________________________________________________________
_______________________________________________________________________________________
In work

Saturday, 15th Sept 2018
_______________________________________________________________________________________
_______________________________________________________________________________________
In work 

Sunday, 16th Sept 2018
_______________________________________________________________________________________
_______________________________________________________________________________________
Upon first running of code, console returned an error with the importing of NUMPY which had had no issues prior.
Spent a few hours troubleshooting, and realised that the IDE I was using was defaulting to python 3.4 
while the system version was Python 2.7. Changing to an earlier version of the IDE was easier and 
quicker than changing the systemwide version of python, so naturally that's what I did (given that all packages
being used are fairly old, and built on 2.7). 

Doing some preliminary testing with PDM on the data which I preciously cleaned up, however I'm not really
expert enough yet to get good results, and so I am playing with the parameters of the PDM script to see how
they change the results.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/not_enough_data_pdm.png)

Want to clean up the number of datapoints, maybe with 1 month averages or 2 week averages, but given the 
inconsistency in the data points takes (large time gaps), not too sure what an effective way to implement
this through code would be.

Bit of a slow day because my CMOS for the telescope came and I was trying to set that up alongside
the matching software for linux

Monday, 17 Sept 2018

______________________________________________________________________________________
______________________________________________________________________________________


Have been working on a function in AAVSO script which will allow to make 1 month averages etc.
It's fairly rudimentary at the moment, going by number of entries rather than their values but
should still work in datasets without large gaps. That said, it is returning an error which I
will have to figure out: "ValueError: cannot set using a slice indexer with a different length 
than the value". Been staring at it for too long so gonna go get some dinner.

Tuesday, 18th Sept 2018
_______________________________________________________________________________________
_______________________________________________________________________________________
Not much in the way of progress. Really just bashing my head against a wall trying to make a 
breakthrough.

Wednesday, 19th Sept 2018

_______________________________________________________________________________________
_______________________________________________________________________________________
Came up with a boolean way of filtering the data POST-import from the spreadsheet. The code
is quite rough around the edges but the principle is there, and after polisihing should work 
a treat. Computer in astro-room wasn't working. slowed progress.

Thursday, 20th Sept 2018
_______________________________________________________________________________________
_______________________________________________________________________________________
Finally made a breakthrough on that. The filtering code by max and min magnitude is implemented
so no I'm filtering data by [1] observation count [2] min/max reasonable observation. I've 
been working on a script which imports the dates in julian day count, then converts to Gregorian,
this is with the help of dateconvert package. I'm doing this because once I'm in Gregorian, 
Pandas package will allow month averages etc to be taken v easily. It's working (it runs)
but disagrees with the US Navy's online converter. Need to look at again.

Friday,21st Sept 2018
________________________________________________________________________________________
________________________________________________________________________________________

In work

Saturday, 22nd Sept 2018
_______________________________________________________________________________________
_______________________________________________________________________________________
In work

Sunday, 23rd Sept 2018
_______________________________________________________________________________________
_______________________________________________________________________________________
Great Success! I have the filtering with user AND the extreme values working. I'd been
having trouble with the extreme values and I  couldn't figure out why. My issue was that
for the Boolean < and > the magnitude column dtype was read as an object and not as float.
Many permutations of commands later, changing the command for what the floatconverter does
when it encounters non-numerical characters. I had been using errors='ignore', just disregarding
the rows with non-numericals, but changing to errors='coerce' and reading non-numericals as
'NaN's seems to have cleared everything up.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/AAVSO_filtered.png)

Now I need to perfect the dateconversion script such that the results can be read by 
PANDAS and allow me to do moving, windowed averages fairly easily.

Monday, 24th Sept 2018

_________________________________________________________________________________________
_________________________________________________________________________________________
Had to work from home today, but git push in college wasn't successful- only the README was
pushed??? Hopefully just forgot to add the specific files yesterday, will see in morning but
this gives me time to do some additional reading on late type semiregulars.


Tuesday, 25th Sept 2018

_________________________________________________________________________________________
_________________________________________________________________________________________
Worked on tidying up considerable and getting the conversion script to output to an excel 
sheet within the workbook. They can now be added and read by the data script which allows 
the calendar to be filtered alongside the magnitude and so on. Now need to get the finger
out and figure out the rolling averages

Wednesday, 26th Sept 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
After a lot of trials I have managed to be able to plot 1 month averages, however the xaxis
ticks aren't there since I've been using two parameters in the pandas.groupby command. hopefully
this will be a relatively easy fix, and then I'll move on to shortening the window to perhaps only 
10 days

![alt text](https://github.com/cumminj1/ZUMA/blob/master/yearlyavg.png)

Above is the groupby function from pandas implemented with a mean, on a yearly basis.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/monthlyavg.png)

And here we have a monthly average for the data, although it does look messy, given
just how many years are condensed into a relatively short graph. Once everything is up and
running, then I'll work on graphing only within 5-10 year timeseries but with multiple subplots

Thursday, 27th Sept 2018

__________________________________________________________________________________________
__________________________________________________________________________________________
Found that in an update, pandas ".rolling().mean()" is now able to handle datetime data with
time gaps. I have been working with a rolling 15-day average, with datapoints assigned only 
where there are entries at least 10 times within that 15 day period. This is good news. Although
the data is still fairly noisy at full timescale, when one /ZUMa/s (haha) in to a decade worth of 
data, we can clearly see the primary curve. In order to improve this, I plan to remove users whose
contribution to a bin is not within N standard deviations of the mean.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/15dayfull.png)
dataset in full with 15 day averaging

![alt text](https://github.com/cumminj1/ZUMA/blob/master/15dayzoom.png)
dataset zoomed to a ten year period or so

![alt text](https://github.com/cumminj1/ZUMA/blob/master/40squiet.png)
confirmation that the late 40s were quiet for ZUMa

Friday, 28h Sept 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Work

Saturday, 29th Sept 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Work

Sunday, 30th Sept 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Figured out why there were so many artefacts in the data; I was passing the window size as 
an integer number of days when it should have been specified as a string. Following that,
duplicates appeared but were removed by taking all duplicates out of the dataframe (currently
just using the last entry, but would rather use a mean). Have taken fixed window, non-moving
averages for comparison and they are subplots alongside the smoother moving averages. Still seem
to be some bumps over small timescales, which isn't really whats expected for a star this size.



![alt text](https://github.com/cumminj1/ZUMA/blob/master/comparing_avgs.png)

![alt text](https://github.com/cumminj1/ZUMA/blob/master/comparing_avgs_zoom.png)

Monday, 1st Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Spent the day workin on PDM to take a break from data cleaning. Seems to be much improved when
working on simulated datasets I've generated. There are troughs representing mis-identified peaks
which, after rechecking the original 1978 Stellingwerf paper, is to be expected. He writes that 
for large datasets, you're likely to get aliasing from sidelobes and noise etc. The statistical effects
are not as important for the larger datasets, though they are paramount for the smaller datasets. the maths 
and stats can be found in the Stellingwerf paper for reference.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/PDM_.png)

Tuesday, 2nd Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Playing with the PDM code, and with the number of false periods returned from simulated data,
I realised that I had neglected to filter the results based upon their statistical significane.
As such I spent most of the day deciphering the relevant quantities from the Stellingwerf PDM
paper.


Wednesday, 3rd Oct 2018

__________________________________________________________________________________________
__________________________________________________________________________________________
Continuing from yesterday,using the Theta values for variance ratios 
to get F-value, and hence p-values, by rejecting periods with p < 0.05 the false peaks have effectively been removed, although for very large binsthere is aliasing (sidelobes?). It seems better
to keep the bin sizes larger than the estimated fundamental freq, but not by much. Even with the
more stringent statistical tests, harmonics are sometimes identified as periods. Need to work on this.
![alt text](https://github.com/cumminj1/ZUMA/blob/master/statistical_filtering.png)
Thursday, 4th Oct 2018

__________________________________________________________________________________________
__________________________________________________________________________________________
Continued same as yesterday, found that the fixed averaging is an awful lot easier to work with
as the timestamps are with a continuous number of days (no gaps)

Friday, 5th Oct 2018

__________________________________________________________________________________________
__________________________________________________________________________________________
In Work

Saturday, 6th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
In Work

Sunday, 7th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Finished reading some papers on similar topics and radial vs non-radial pulsations seem 
to be relevant, as do the spectral type of the star when any real changes come about. The
C-rich, and O-rich variants seem to have different characteristic pulsation

Monday, 8th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
I'm trying to figure out a way to have my pdm script read through my moving averages data,
but the issue is that this data has timegaps, and the PYPDM package reads discrete days, 
not really understanding the gaps. Trying to either interpolate or just fill the gaps in 
the Datetime index with NaNs, but worried that they might affect the PDM results

Tuesday, 9th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
I had the PDM data working and started using the AFOEV data for comparison, and it returns
a similar, but not the same value for the primary period after being run through the script.
We get a value of 190 rather than 195. interesting

Wednesday, 10th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________

Spent day polishing report mostly.

Thursday, 11th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Report submited and going through the AAVSO and AFOEV data, data request from AAVSO to update
my data up to 2018. This allows me to see a particularly deep minimum which was reported in 
2014, although it also seems to be present 2 years later in 2016. Waiting to hear if I'll
get spectral data from Doctor David Boyd in the UK to analyse the timeperiod

Friday, 12th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Doctor Boyd got back to me and said I could use his data. Asked what format, and what 
specific data

Saturday, 13th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Dr Boyd sent the data

Sunday, 14th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Have been trying to read the data, but it seems to be only 1 dimensional. Ive tried opening 
it but i only seem to be getting a wavelength axis. Emailed Brian to see if I'm doing anything
wrong before I contact Dr Boyd again. Had some issue at first but finally got the spectra 
from the fits files working properly. Wrote a looping script which would reach into the containing
folder and cycle through, plotting the fits files

![alt text](https://github.com/cumminj1/ZUMA/blob/master/dark_spectra.png)

Monday, 15th Oct 2018
__________________________________________________________________________________________
__________________________________________________________________________________________
Finally merged the AAVSO files into a csv which covers 1920s up to 2018 and ran some more 
analysis. In order to make the graphs more legible, I converted the colour scheme so that they
would match a dark background. Reading up on analysing the spectrum of the star to see if 
I can see any mechanistic data for changes

![alt text](https://github.com/cumminj1/ZUMA/blob/master/darkmovingfixed.png)
Tuesday, 16 Oct 2018


_____________________________________________________________________________________
_____________________________________________________________________________________
In order to get some structural information on the star I want to be able to compare the
spectra of the star to some reference spectra to see what kind of differences I can find in
the star as it pulsates, I did some reading and found some MIII spectra from the PICKLES
library of spectra (from ESO website). Also have been reading into astroseismology and 
identifying stars' internal structure based upon spectra. If the resolution of the 
spectrum was finer could see rotational splitting and then determine what comes from 
which mode of rotation

Wednesday, 17 Oct 2018

_____________________________________________________________________________________
_____________________________________________________________________________________
On the back of yesterday I have been trying to compare the Boyd spectra to that of the 
spectral library, but had some problems based upon the diferent sizes of the datasets.
I feel it would make more sense to shrink the larger one down, rather than to interpolate
upwards, but this is seeming to be more difficult than I anticipated, since I can't do
any non-integer slicing, or resampling by final sample size. Will need to think on it a bit
more

Thurdsay, 18th Oct 2018

_____________________________________________________________________________________
_____________________________________________________________________________________
A bit unwell so stayed at home and did some work, but no real breakthroughs here tbh

Friday, 19th Oct 2018
_____________________________________________________________________________________
_____________________________________________________________________________________
In Work

Satruday, 19th Oct 2018
_____________________________________________________________________________________
_____________________________________________________________________________________
In Work

Sunday, 20th Oct 2018
_____________________________________________________________________________________
_____________________________________________________________________________________
I was able to reduce the size of the dataset for the observed spectra such that it 
matched the size of its reference spectra. I have now done this for both MAX and MIN
of the star, and created some difference plots to see if there are emission features 
which I can identify to show differences between the max and the min.

![alt text](https://github.com/cumminj1/ZUMA/blob/master/4_spectra_difference_plot.png)

_____________________________________________________________________________________
_____________________________________________________________________________________





