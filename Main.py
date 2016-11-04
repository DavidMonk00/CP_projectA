'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import SmallAngle as sa
import Plot
from matplotlib import pyplot as plt
import ctypes as ct

def doublePendulum():
    D = 0
    A = 0.1
    R = 1
    G = 0
    start = [A,0.0,0.0,0.0]
    pt = Plot.Plot(D,start,1,R,G)
    h = 0.08
    cycles = 30
    steps = int(cycles*2*np.pi/h)
    method = sa.SmallAngle.rk4DoublePendulumMethod
    pt.plotDoubleMethod(method,h,steps)
    pt.show()

def singlePendulum():
    A = 0.1
    D = 0
    start = [A,0.0]
    pt = Plot.Plot(D,start,1)
    h = 0.01
    cycles = 10
    steps = int(cycles*2*np.pi/h)
    method = sa.SmallAngle.rk4SineMethod
    pt.plotMethod(method,h,steps)
    pt.show()

def main():
    #doublePendulum()
    singlePendulum()

main()
