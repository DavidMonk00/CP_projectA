'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import SinglePendulum as sp
import Plot
from matplotlib import pyplot as plt
import ctypes as ct

def doublePendulum(A, R, G, cycles, h):
    ct.cdll.LoadLibrary("./doublependulum.so")
    csa = ct.CDLL("./doublependulum.so")
    start = [A,0.0,0.0,0.0]
    pt = Plot.Plot(0,start,1,R,G)
    steps = int(cycles*2*np.pi/h)
    print 'Steps: ', steps
    method = csa.rk4
    pt.plotDoubleMethod(method,h,steps)
    #pt.plotDoubleMethod(csa.leapfrog,h,steps)
    pt.show()

def singlePendulum(A, D, cycles, h):
    ct.cdll.LoadLibrary("./singlependulum.so")
    csa = ct.CDLL("./singlependulum.so")
    start = [A,0.0]
    pt = Plot.Plot(D,start,1)
    steps = int(cycles*2*np.pi/h)
    method = csa.eulerForward
    pt.plotMethod(method,h,steps)
    #pt.error(method,h,steps)
    #pt.plotMethod(csa.leapfrog,h,steps)
    pt.show()

def main():
    A, D, R, G = 0.1, 0.2, 100, 1.0
    cycles = 20
    s = [0.01,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.5,2,2.5,3]
    t = np.arange(2.9,3,0.01)
    h = 0.01
    Rlist = np.logspace(-3,3,7)
    #for i in Rlist:
    #doublePendulum(A, R, G, cycles, h)
    #for i in t:
    #    print i, "  "
    singlePendulum(A, D, cycles, h)

main()
