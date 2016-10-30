'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import SmallAngle as sa
import Plot
from matplotlib import pyplot as plt
import ctypes as ct


def main():
    A = 0.5
    D = 0
    start = [A,0.0]
    pt = Plot.Plot(D,start,2)
    h = 0.3
    steps = int(100*2*np.pi/h)
    method = sa.SmallAngle.leapfrogMethod
    pt.plotMethod(method,h,steps,True)
    pt.error(method, h,steps)
    pt.show()
    #y = ctest(steps,h)
    #x = np.arange(0,h*steps,h)
    #plt.plot(x,y)
    #plt.show()

def ctest(p_steps, p_h):
    y_start = [0.5,0.0]
    D = 0.0
    ct.cdll.LoadLibrary("./smallangle.so")
    csa = ct.CDLL("./smallangle.so")
    csa.eulerForward.restype = ct.POINTER(ct.c_double)
    c_start = (ct.c_double*len(y_start))(*y_start)
    steps = ct.c_int(p_steps)
    h = ct.c_double(p_h)
    c_D = ct.c_double(D)
    values = csa.eulerForward(c_start, D, steps,h)
    y = np.empty(p_steps)
    for i in range(p_steps):
        y[i] = values[i]
    return y

main()
