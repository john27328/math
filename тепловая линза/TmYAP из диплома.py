#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:17:13 2018

@author: raptev
"""

Pabs = 40 * 0.25
pi = 3.14
Kt = 11.
d = .8e-3
dn_dt = 10.08e-6
v = 0.3
at = 9.5e-6
n=1.91

D = Pabs / (pi * Kt * pow(d,2)) * (dn_dt + (n-1)*at)

print(D,1/D)