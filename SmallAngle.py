'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np

class SmallAngle(object):
	D = 0
	y_start = np.zeros(2)
	array = np.array([[0.0,1.0],[-1.0,-D]],dtype='float64')

	def __init__(self, damping_coefficient, start):
		self.D = damping_coefficient
		self.y_start = start

	def eulerForwardMethod(self, h, steps):
		y = np.empty(2*steps).reshape(2,steps)
		y[:,0] = self.y_start
		for i in xrange(steps-1):
			y[:,i+1]=np.dot((np.eye(2, dtype='float64') + h*self.array),y[:,i])
		return y[0,:]

	def leapfrogMethod(self,h,steps):
		y = np.empty(2*steps).reshape(2,steps)
		y[:,0] = self.y_start
		y[:,1] = np.dot((np.eye(2, dtype='float64') + h*self.array), y[:,0])
		for i in xrange(1, steps-1):
			y[:,i+1] = y[:,i-1] + 2*np.dot(h*self.array, y[:,i])
		return y[0,:]

	def rk4Method(self, h, steps):
		y = np.empty(2*steps).reshape(2,steps)
		y[:,0] = self.y_start
		for i in xrange(steps - 1):
			k = [0,0,0,0]
			k[0] = h*np.dot(self.array, y[:,i])
			k[1] = h*np.dot(self.array, y[:,i] + 0.5*k[0])
			k[2] = h*np.dot(self.array, y[:,i] + 0.5*k[1])
			k[3] = h*np.dot(self.array, y[:,i] + k[2])
			y[:,i+1] = y[:,i] + (k[0] + 2*k[1] + 2*k[2] + k[3])/6.0
		return y[0,:]

	def implicitEulerMethod(self, h, steps):
		y = np.empty(2*steps).reshape(2,steps)
		y[:,0] = self.y_start
		inv_t = np.linalg.inv(np.eye(2, dtype='float64') - h*self.array)
		for i in xrange(steps - 1):
			y[:, i+1] = np.dot(inv_t,y[:,i])
		return y[0,:]

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
