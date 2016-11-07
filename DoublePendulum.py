'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import ctypes as ct

class DoublePendulum(object):
	R = 1
	G = 0
	y_start = [0,0]

	def __init__(self, start, R, G):
		self.y_start = start
		self.R = R
		self.G = G

	def iterateMethod(self, method, h, steps):
		method.restype = ct.POINTER(ct.POINTER(ct.c_double))
		c_start = (ct.c_double*len(self.y_start))(*self.y_start)
		values = method(c_start, ct.c_double(self.R), ct.c_double(self.G),ct.c_int(steps),ct.c_double(h))
		y = np.empty(4*steps).reshape(4,steps)
		for i in range(steps):
			for j in range(4):
				y[j][i] = values[j][i]
		return y
