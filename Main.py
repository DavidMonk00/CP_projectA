'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import SmallAngle as sa
import Plot
from matplotlib import pyplot as plt
import ctypes as ct

def doublePendulum(A, R, G, cycles, h):
    start = [A,0.0,0.0,0.0]
    pt = Plot.Plot(0,start,1,R,G)
    steps = int(cycles*2*np.pi/h)
    method = sa.SmallAngle.rk4DoublePendulumMethod
    pt.plotDoubleMethod(method,h,steps)
    pt.show()

def singlePendulum(A, D, cycles, h):
    start = [A,0.0]
    pt = Plot.Plot(D,start,1)
    steps = int(cycles*2*np.pi/h)
    method = sa.SmallAngle.rk4SineMethod
    pt.plotMethod(method,h,steps)
    pt.show()

def main():
    A, D, R, G = 0.1, 0, 1, 0
    cycles = 10
    h = 0.01
    #doublePendulum(A, R, G, cycles, h)
    singlePendulum(A, D, cycles, h)

main()
