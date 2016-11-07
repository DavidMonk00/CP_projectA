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
    method = csa.rk4
    pt.plotDoubleMethod(method,h,steps)
    pt.show()

def singlePendulum(A, D, cycles, h):
    ct.cdll.LoadLibrary("./singlependulum.so")
    csa = ct.CDLL("./singlependulum.so")
    start = [A,0.0]
    pt = Plot.Plot(D,start,1)
    steps = int(cycles*2*np.pi/h)
    method = csa.rk4
    pt.plotMethod(method,h,steps)
    pt.show()

def main():
    A, D, R, G = 0.1, 0, 1, 0
    cycles = 10
    h = 0.2
    doublePendulum(A, R, G, cycles, h)
    #singlePendulum(A, D, cycles, h)

main()
