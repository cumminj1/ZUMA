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
