#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 12:41:49 2018

@author: CUMMINJ1
"""
import numpy
import matplotlib.pyplot as plt
plt.style.use('ggplot')

period_1=(195)
frequency_1=(1/period_1)

period_2=(3513)
frequency_2=(1/period_2)

period_3=(391)
frequency_3=(1/period_3)

#convolute the three sinusoidals
#the divisor on x changes the spacin of the poinsts along the line
x = numpy.arange(9000)
y = 1*numpy.sin(x*2.0*numpy.pi*frequency_1)+0.25*numpy.sin(x*frequency_2*2.0*numpy.pi)+0.15*numpy.sin(x*frequency_3*2.0*numpy.pi)

#adding the noise
# we use a normal distibution with a std deviation of 1.0, centered at 0
stddevs=.05
#shape our noise to the signal's dimensions
noise=numpy.random.normal(0,stddevs,x.shape)
#add to the signal
y1=y+noise

plt.plot(x,y, linewidth=3)
plt.show()

