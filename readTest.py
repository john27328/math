#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:02:21 2018

@author: raptev
"""

import sys 
sys.path.append("/home/raptev/src/math/lib/")
from CSV import readCSV
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

x,y = readCSV(" ",2)

k = 2.33 / 19.8

for i, yi in enumerate(y):
    y[i] = yi/k
    
plt.plot(x, y, 'o')

x = np.array(x)
y = np.array(y)
lowess = sm.nonparametric.lowess(y, x, frac=0.01)
plt.plot(lowess[:, 0], lowess[:, 1])
plt.grid(True) 
