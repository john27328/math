#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:56:33 2018

@author: raptev
"""

class Res:
    pass
    
def test():
    rez = Res()
    rez.A = 1
    rez.B = 2
    return rez

rez = test()
print (rez.A, rez.B)