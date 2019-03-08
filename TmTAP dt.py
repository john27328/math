#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 08:38:10 2018

@author: raptev
"""
import matplotlib.pyplot as plt
import numpy as np

#исходные данные
t15 = 2, 3, 4, 5, 30
dt15 = 2.3, 2.7, 2.8, 2.8, 2.8

t20 = 2,3,4,5,6,8,10,12,15,20,30
dt20 = 0.8,0.9,1.3,1.2,1.4,1.6,1.6,1.6,1.6,1.7,1.7

t25 = 2,3,4,5,6,8,10,12,15,20,30
dt25 = 0.5,0.6,0.7,0.8,0.8,0.9,1,1,1,1.1,1.2

t30 = 2,3,4,5,6,8,10,12,15,20,30
dt30 = 0.4,0.5,0.5,0.6,0.6,0.6,0.6,0.7,0.8,0.8,0.8

t35 = 2,3,4,5,6,8,10,12,15,20,30
dt35 = 0.3,0.3,0.4,0.4,0.5,0.5,0.5,0.6,0.6,0.6,0.6

t40 = 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 30
dt40 = 0.3,0.3,0.3,0.3,0.3,0.4,0.4,0.4,0.4,0.5,0.5

t = t15, t20, t25, t30,t35,t40
dt = dt15, dt20, dt25, dt30,dt35,dt40

for i, ti in enumerate(t):
    plt.plot(ti, dt[i])
plt.grid(True)

#калибровки
I0 = 1.5, 2, 2.5, 3, 3.5, 4
tmin = 2, 2, 2, 2, 2, 2
tconst = 4, 8, 10, 15, 12, 20 
tmax = 30, 30, 30, 30, 30, 30
dtmin = 2.3, .8, .5, .4, .3, .3
dtmax = 2.8, 1.7, 1.2, 0.8, 0.6, 0.5

#алгоритм
def dt(I, t):
    # ищу диапазон для линейной апроксимации
    for i, I0i in enumerate(I0):
        iI = len(I0) - 1 # на случай, если точка будет справа от калибровок
        if I <= I0i:
            iI = i
            break
    if iI == 0: # на случай, если точка будет слева от калибровок
        iI = 1;
    k = (I - I0[iI - 1]) / (I0[iI] - I0[iI - 1])    
    tminI = tmin[iI - 1] + k * (tmin[iI] - tmin[iI - 1])
    tconstI = tconst[iI - 1] + k * (tconst[iI] - tconst[iI - 1])
    #tmaxI = tmax[iI - 1] + k * (tmax[iI] - tmax[iI - 1])
    dtminI = dtmin[iI - 1] + k * (dtmin[iI] - dtmin[iI - 1])
    dtmaxI = dtmax[iI - 1] + k * (dtmax[iI] - dtmax[iI - 1])
    print(tminI, tconstI,  dtminI, dtmaxI)
    if tconstI <= tminI: # защита от деления на 0
        tconstI = 0
    if t < tconstI:
        dt = dtminI + (t - tminI) / (tconstI - tminI) * (dtmaxI - dtminI)
    else:
        dt = dtmaxI
    return dt

I = np.arange(1.9, 2.1, 0.05)
t = np.arange(1, 35, .2)
for i in I:
    p = []
    for j in t:
        p.append(dt(i,j))
#        print (dt(i,j))
    plt.plot(t, p)