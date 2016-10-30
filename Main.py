'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import SmallAngle as sa
import Plot
import ctypes as ct


def main():
    A = 0.5
    D = 0
    start = np.array([A,0.0])
    pt = Plot.Plot(D,start,2)
    h = 0.1
    steps = int(np.pi*10/h)
    method = sa.SmallAngle.implicitEulerMethod
    pt.plotMethod(method,h,steps,True)
    pt.error(method, h,steps)
    pt.show()

def ctest(max):
    ct.cdll.LoadLibrary("./smallangle.so")
    sa = ct.CDLL("./smallangle.so")
    sa.eulerForward.restype = ct.POINTER(ct.c_double)
    D = ct.c_double(0)
    steps = ct.c_int(max)
    x = sa.eulerForward(D, steps)
    y = []
    for i in range(2):
        y.append(x[i])
    #print y

ctest(int(1e2))
