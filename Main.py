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
    h = 0.1
    cycles = 20
    steps = int(cycles*2*np.pi/h)
    method = sa.SmallAngle.rk4Method
    pt.plotMethod(method,h,steps)
    pt.show()

def ctest(p_steps, p_h):
    y_start = [0.5,0.0]
    D = 0.0
    ct.cdll.LoadLibrary("./smallangle.so")
    csa = ct.CDLL("./smallangle.so")
    csa.rk4.restype = ct.POINTER(ct.c_double)
    c_start = (ct.c_double*len(y_start))(*y_start)
    steps = ct.c_int(p_steps)
    h = ct.c_double(p_h)
    c_D = ct.c_double(D)
    values = csa.rk4(c_start, c_D, steps,h)
    y = np.empty(p_steps)
    for i in range(p_steps):
        y[i] = values[0][i]
    return y

def main():
    doublePendulum()

main()
