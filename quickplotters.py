#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:15:13 2018

@author: CUMMINJ1
"""

import matplotlib.pyplot as plt
import numpy as np

period5=[181.5,198,190.5,187,189,193.5,196.5,192,193.5,196.5,192,
         193.5,193.5,196.5,187.5,193.5,187.5,187.5]
period10=[178,190.5,193.5,193.5,192,192,187]

plt.hist([period5,period10], bins=[180,182,184,186,188,190,192,194,196,198,200], label=['5 year sweeps','10 year sweeps'])
plt.title("primary oscillation period for Z UMa")
plt.xlabel("primary period [days]")
plt.ylabel("frequency [counts]")
plt.xticks(np.arange(180, 200, step=2))
plt.legend()
plt.show()