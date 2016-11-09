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
		cR = ct.c_double(self.R)
		cG = ct.c_double(self.G)
		csteps = ct.c_int(steps)
		ch = ct.c_double(h)
		method.restype = ct.POINTER(ct.POINTER(ct.c_double))
		c_start = (ct.c_double*len(self.y_start))(*self.y_start)
		print "Obtaining values..."
		values = method(c_start, ct.c_double(self.R), ct.c_double(self.G),ct.c_int(steps),ct.c_double(h))
		print "C complete. Casting to numpy and calculating energy..."
		y = np.empty(4*steps).reshape(4,steps)
		E = np.empty(steps)
		prev = 0
		for i in range(steps):
			if (i % (steps/100) == 0):
				print (float(i)/steps)*100
			for j in range(4):
				y[j][i] = values[j][i]
			E[i] = 2*values[0][i]**2 + values[1][i]**2 + 2*values[2][i]**2 + values[3][i]**2 + 2*values[3][i]*values[2][i]*(1-(values[0][i]-values[1][i])/2)
		return y,E
