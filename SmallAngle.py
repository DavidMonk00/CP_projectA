'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import ctypes as ct

class SmallAngle(object):
	D = 0
	y_start = [0,0]
	array = np.array([[0.0,1.0],[-1.0,-D]],dtype='float64')

	def __init__(self, damping_coefficient, start):
		self.D = damping_coefficient
		self.y_start = start

	def eulerForwardMethod(self, p_h, p_steps):
		ct.cdll.LoadLibrary("./smallangle.so")
		csa = ct.CDLL("./smallangle.so")
		csa.eulerForward.restype = ct.POINTER(ct.c_double)
		c_start = (ct.c_double*len(self.y_start))(*self.y_start)
		steps = ct.c_int(p_steps)
		h = ct.c_double(p_h)
		values = csa.eulerForward(c_start,ct.c_double(self.D), steps,h)
		y = np.empty(p_steps)
		for i in range(p_steps):
			y[i] = values[i]
		return y

	def leapfrogMethod(self,p_h,p_steps):
		ct.cdll.LoadLibrary("./smallangle.so")
		csa = ct.CDLL("./smallangle.so")
		csa.leapfrog.restype = ct.POINTER(ct.c_double)
		c_start = (ct.c_double*len(self.y_start))(*self.y_start)
		steps = ct.c_int(p_steps)
		h = ct.c_double(p_h)
		values = csa.leapfrog(c_start,ct.c_double(self.D), steps,h)
		y = np.empty(p_steps)
		for i in range(p_steps):
			y[i] = values[i]
		return y

	def rk4Method(self, p_h, p_steps):
		ct.cdll.LoadLibrary("./smallangle.so")
		csa = ct.CDLL("./smallangle.so")
		csa.rk4.restype = ct.POINTER(ct.c_double)
		c_start = (ct.c_double*len(self.y_start))(*self.y_start)
		steps = ct.c_int(p_steps)
		h = ct.c_double(p_h)
		values = csa.rk4(c_start,ct.c_double(self.D), steps,h)
		y = np.empty(p_steps)
		for i in range(p_steps):
			y[i] = values[i]
		return y

	def implicitEulerMethod(self, p_h, p_steps):
		ct.cdll.LoadLibrary("./smallangle.so")
		csa = ct.CDLL("./smallangle.so")
		csa.implicitEuler.restype = ct.POINTER(ct.c_double)
		c_start = (ct.c_double*len(self.y_start))(*self.y_start)
		steps = ct.c_int(p_steps)
		h = ct.c_double(p_h)
		values = csa.implicitEuler(c_start,ct.c_double(self.D), steps,h)
		y = np.empty(p_steps)
		for i in range(p_steps):
			y[i] = values[i]
		return y

	def rk4DoublePendulumMethod(self, p_h, p_steps, p_R, p_G):
		ct.cdll.LoadLibrary("./smallangle.so")
		csa = ct.CDLL("./smallangle.so")
		csa.rk4DoublePendulum.restype = ct.POINTER(ct.POINTER(ct.c_double))
		c_start = (ct.c_double*len(self.y_start))(*self.y_start)
		steps = ct.c_int(p_steps)
		h = ct.c_double(p_h)
		R = ct.c_double(p_R)
		G = ct.c_double(p_G)
		values = csa.rk4DoublePendulum(c_start,R,G,ct.c_double(self.D), steps,h)
		y = np.empty(p_steps)
		for i in range(p_steps):
			y[i] = values[1][i]
		return y

	def error(self, method, h, steps):
		x = np.arange(0,h*steps,h)
		real = (self.y_start[0]*np.cos(x))[1:]
		y = method(self, h, steps)
		return np.abs(y[1:]-real)

	def stability(self, h, steps):
		e = self.error(h,steps)
		s = np.zeros(e.size)
		for i in xrange(s.size-1):
			s[i+1] = np.abs(e[i+1]/e[i])
		return s
