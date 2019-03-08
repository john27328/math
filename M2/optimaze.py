#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:26:27 2018

@author: raptev
"""
import sys 
#import scipy.interpolate
sys.path.append("/home/raptev/src/math/lib/")
from CSV import readCSV
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
#from PyQt5.QtWidgets import (QFileDialog, QApplication)

def func(z, a, b, c):
    return np.sqrt(a + b * z + c * z**2)


x,y = readCSV(" ",0)

print(x,y)
z = np.array(x)
y = np.array(y)   

#y_interp = scipy.interpolate.interp1d(t, y)
#
#t = np.linspace(t[0], t[-1], 100)
#y = y_interp(t)

popt, pcov = curve_fit(func, z, y, (1., 0.02, 0.0001), maxfev=10**6)    
a, b, c = popt
print('a={0}\nb={1}\nc={2}\n'.format(*tuple(popt)))
lambdaP = 532e-9 * 1e3
M2 = np.pi / (8 * lambdaP) * np.sqrt(4 * a * c - b**2)
print('M2 = ', M2)

zteor = np.linspace(z[0], z[-1], 1000)
N=1000
yteor = func(zteor,a,b,c)
plt.scatter(z, y, s=30, color='orange')
plt.plot(zteor, yteor)
plt.grid(True)