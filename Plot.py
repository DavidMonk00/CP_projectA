'''
Created on 28 Oct 2016

@author: david
'''

import numpy as np
import matplotlib.pyplot as plt

class Plot(object):
	def __init__(self, damping_coefficient, start):
		self.sa = SmallAngle(damping_coefficient, start)
	def eulerForward(self, h, steps):
		y = self.sa.eulerForwardMethod(h, steps)
		x = np.arange(0,y.size*h,h)
		plt.plot(x,y)
	def leapfrog(self, h, steps):
		y = self.sa.leapfrogMethod(h,steps)
		x = np.arange(0,y.size*h,h)
		plt.plot(x,y)
	def rk4(self, h, steps):
		y = self.sa.rk4Method(h,steps)
		x = np.arange(0,y.size*h,h)
		plt.plot(x,y)
	def implicitEuler(self, h, steps):
		y = self.sa.implicitEulerMethod(h,steps)
		x = np.arange(0,y.size*h,h)
		plt.plot(x,y)
	def analytical(self, h, steps, A):
		x = np.arange(0,h*steps,h)
		y = A*np.cos(x)
		plt.plot(x,y)
	def error(self, h, steps):
		x = np.arange(0,h*steps,h)
		y = self.sa.error(h, steps)
		plt.plot(x[1:],y)
	def stability(self, h, steps):
		x = np.arange(0,h*steps,h)
		y = self.sa.stability(h, steps)
		plt.plot(x[1:],y)
	
	def show(self):
		plt.ylim([-1,5])
		plt.show()
