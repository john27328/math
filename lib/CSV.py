#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:46:21 2018

@author: raptev
"""
from tkinter import Tk
from tkinter.filedialog import askopenfilename
def readCSV(separator = ' ', lineSkip = 0):
    Tk().withdraw() 
    filename = askopenfilename() 
    f = open(filename)
    line = []
    for i in f:
        line.append(i)
    xd = []
    yd = []   
    for i in range(lineSkip,len(line)):
        ln = line[i].replace(',', '.').split(separator)
        xd.append(float(ln[0]))
        yd.append(float(ln[1])) 
    return xd,yd
