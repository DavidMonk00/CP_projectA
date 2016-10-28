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

def ctest():
    ct.cdll.LoadLibrary("./libseries.so")
    series = ct.CDLL("./libseries.so")
    series.ser.restype = ct.c_double
    f = ct.c_double(1)
    l = ct.c_double(5000)
    print "The calculation gives %11.9f"%(series.ser(f,l))

ctest()
