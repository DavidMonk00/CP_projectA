'''
Created on 28 Oct 2016

@author: david
'''

import numpy as np
import matplotlib.pyplot as plt
import SmallAngle

class Plot(object):
	def __init__(self, damping_coefficient, start):
		self.sa = SmallAngle.SmallAngle(damping_coefficient, start)

	def analytical(self, h, steps, A):
		x = np.arange(0,h*steps,h)
		y = A*np.cos(x)
		plt.plot(x,y)
	def error(self, method, h, steps):
		x = np.arange(0,h*steps,h)
		y = self.sa.error(method, h, steps)
		plt.plot(x[1:],y)
	def stability(self, h, steps):
		x = np.arange(0,h*steps,h)
		y = self.sa.stability(h, steps)
		plt.plot(x[1:],y)

	def plotMethod(self, method, h, steps):
		x = np.arange(0,h*steps,h)
		y = method(self.sa,h, steps)
		plt.plot(x,y)

	def show(self):
		#plt.ylim([-1,5])
		plt.show()
