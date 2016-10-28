'''
Created on 28 Oct 2016

@author: david
'''

import numpy as np
import matplotlib.pyplot as plt
import SmallAngle

class Plot(object):
	def __init__(self, damping_coefficient, start, rows):
		self.sa = SmallAngle.SmallAngle(damping_coefficient, start)
		self.fig = plt.figure()
		self.row_counter = 1
		self.rows = rows
		self.subplots = []
		self.A = start[0]

	def analytical(self, h, steps):
		x = np.arange(0,h*steps,h)
		y = self.A*np.cos(x)
		self.subplots[self.row_counter-1].plot(x,y)

	def error(self, method, h, steps):
		x = np.arange(0,h*steps,h)
		y = self.sa.error(method, h, steps)
		self.subplots.append(self.fig.add_subplot(self.rows,1,self.row_counter))
		self.subplots[self.row_counter-1].set_ylabel('Error')
		self.subplots[self.row_counter-1].plot(x[1:],y)
		self.row_counter += 1

	def stability(self, h, steps):
		x = np.arange(0,h*steps,h)
		y = self.sa.stability(h, steps)
		ax = self.fig.add_subplot(self.rows,1,self.row_counter)
		self.row_counter += 1
		ax.plot(x[1:],y)

	def plotMethod(self, method, h, steps, true_value=False):
		x = np.arange(0,h*steps,h)
		y = method(self.sa,h, steps)
		self.subplots.append(self.fig.add_subplot(self.rows,1,self.row_counter))
		self.subplots[self.row_counter-1].set_ylabel('Value')
		self.subplots[self.row_counter-1].plot(x,y)
		if true_value:
			self.analytical(h,steps)
		self.row_counter += 1

	def show(self):
		plt.ticklabel_format(axis='y', style='sci')
		#plt.ylim([-1,5])
		plt.show()