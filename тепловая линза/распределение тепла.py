#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:55:01 2018

@author: raptev
"""

from math import exp, log

T_tm = .25
eta_h = 1 - T_tm
P_abs = 80  #W
w = 0.8e-3 / 2 # 
K_c = 11
L=8e-3
r0 = 3e-3 / 2
alpha_NS = - log(T_tm)/L
pi = 3.14159265359

def dT(r,z):
    
    A = eta_h*P_abs / (4 * pi * K_c) * alpha_NS*exp(-alpha_NS * z) /  \
        (1 - exp(-alpha_NS * L))
    if abs(r) <=w:
        B = log(r0**2 / w**2) + 1 - r**2 / w**2
    else:
        B = log(r0**2 / r**2)
    return A * B

print(dT(0,0), dT(0,L), dT(r0,L))

ndr = 201
ndz = 201


dr = 2*r0/(ndr-1);
dz = L/(ndz-1);

dtsp=[0]*ndr
rsp=[0]*ndr
zsp=[0]*ndr
for i in range(ndr):
    r = i * dr - r0
    dtsp[i] = [0] * ndz
    rsp[i] = [0] * ndz
    zsp[i] = [0] * ndz
    for j in range(ndz):
        z = j * dz
        dtsp[i][j] = dT(r,z)
        #print(r,z,dT(r,z))
        rsp[i][j] = r
        zsp[i][j] = z
        
import numpy as np
data = np.loadtxt("tmYAP diplom v7.GGDT", delimiter=' ', dtype=np.float)


dtz0=[0]*ndr
rz0=[0]*ndr
for i in range(ndr):
    r = i * dr - r0
    rz0[i]=r
    dtz0[i] = dtsp[i]
nddr = 21
nddz = 21
    
dtdz0=[0]*nddr
rdz0=[0]*nddr
print(nddr*int((nddr-1)/2))
print(20*nddr**2 + nddr*int((nddr-1)/2) + 0)
for i in range(nddr):
    dtdz0[i]=[0]*nddz
    for j in range(nddz):
        rdz0[i]=  data[i*nddr**2 + nddr*int((nddr-1)/2) + j][0] * 1e-3
        dtdz0[i][j] = data[i*nddr**2 + nddr*int((nddr-1)/2) + j][3] -16
    
#import matplotlib.pyplot as plt
plot(rz0, dtz0,label = 'teor')
plot(rdz0, dtdz0, label = 'model')