'''
Created on 28 Oct 2016

@author: david
'''

import numpy as np
import matplotlib.pyplot as plt
import SmallAngle

class Plot(object):
	def __init__(self, damping_coefficient, start, rows, R = 1, G = 0):
		self.sa = SmallAngle.SmallAngle(damping_coefficient, start)
		self.fig = plt.figure()
		self.row_counter = 1
		self.rows = rows
		self.subplots = []
		self.A = start[0]
		self.R = R
		self.G = G

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
		y = method(self.sa,h, steps,0)
		v = method(self.sa,h, steps,1)
		E = []
		for i in range(len(y)):
			E.append(y[i]**2 + v[i]**2)
		self.subplots.append(self.fig.add_subplot(self.rows,1,self.row_counter))
		self.subplots[self.row_counter-1].set_ylabel('Value')
		#self.subplots[self.row_counter-1].plot(x,y)
		#self.subplots[self.row_counter-1].plot(x,v)
		self.subplots[self.row_counter-1].plot(x,E)
		if true_value:
			self.analytical(h,steps)
		self.row_counter += 1

	def plotDoubleMethod(self, method, h, steps):
		x = np.arange(0,h*steps,h)
		y_i = method(self.sa,h, steps, self.R, self.G,0)
		y_ii = method(self.sa,h, steps, self.R, self.G,1)
		v_i = method(self.sa,h, steps, self.R, self.G,2)
		v_ii = method(self.sa,h, steps, self.R, self.G,3)
		E = []
		for i in range(len(y)):
			E.append(y_i[i]**2 + v_i[i]**2 + y_ii[i]**2 + v_ii[i]**2)

		self.subplots.append(self.fig.add_subplot(self.rows,1,self.row_counter))
		self.subplots[self.row_counter-1].set_ylabel('Value')
		self.subplots[self.row_counter-1].plot(x,y_i)
		self.subplots[self.row_counter-1].plot(x,y_ii)
		self.row_counter += 1

	def show(self):
		plt.ticklabel_format(axis='y', style='sci')
		#plt.ylim([-1,5])
		plt.show()
