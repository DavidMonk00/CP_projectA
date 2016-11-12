'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import ctypes as ct

class SinglePendulum(object):
	D = 0
	y_start = [0,0]

	def __init__(self, damping_coefficient, start):
		self.D = damping_coefficient
		self.y_start = start

	def iterateMethod(self, method, h, steps):
		method.restype = ct.POINTER(ct.POINTER(ct.c_double))
		c_start = (ct.c_double*len(self.y_start))(*self.y_start)
		values = method(c_start,ct.c_double(self.D),ct.c_int(steps),ct.c_double(h))
		y = np.empty(2*steps).reshape(2,steps)
		for i in range(steps):
			y[0][i] = values[0][i]
			y[1][i] = values[1][i]
		return y

	def error(self, method, h, steps):
		x = np.arange(0,h*steps,h)
		real = (self.y_start[0]*np.cos(x))
		y = self.iterateMethod(method, h, steps)
		return np.abs(y[0]-real)

	def stability(self, h, steps):
		e = self.error(h,steps)
		s = np.zeros(e.size)
		for i in xrange(s.size-1):
			s[i+1] = np.abs(e[i+1]/e[i])
		return s
