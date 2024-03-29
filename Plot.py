'''
Created on 28 Oct 2016

@author: david
'''

import numpy as np
import matplotlib.pyplot as plt
import SinglePendulum
import DoublePendulum

class Plot(object):
	def __init__(self, damping_coefficient, start, rows, R = 1, G = 0):
		self.sp = SinglePendulum.SinglePendulum(damping_coefficient, start)
		self.dp = DoublePendulum.DoublePendulum(start, R, G)
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
		y = self.sp.error(method, h, steps)
		self.subplots.append(self.fig.add_subplot(self.rows,1,self.row_counter))
		self.subplots[self.row_counter-1].set_ylabel('Error')
		self.subplots[self.row_counter-1].plot(x,y)
		self.row_counter += 1

	def plotMethod(self, method, h, steps, true_value=False):
		x = np.linspace(0,h*steps,steps)
		values = self.sp.iterateMethod(method, h, steps)
		y = values[0]
		v = values[1]
		E = np.empty(steps)
		E_error = np.empty(steps)
		for i in range(len(y)):
			E[i] = ((v[i]**2)/2) + 1 - np.cos(y[i])
			E_error[i] = np.abs((E[i] - E[0])/E[0])
		self.subplots.append(self.fig.add_subplot(self.rows,1,self.row_counter))
		self.subplots[self.row_counter-1].set_ylabel('Relative Energy Error')
		self.subplots[self.row_counter-1].plot(x,y)
		#self.subplots[self.row_counter-1].plot(x,v)
		#self.subplots[self.row_counter-1].plot(x,E_error)
		if true_value:
			self.analytical(h,steps)
		self.row_counter += 1

	def plotDoubleMethod(self, method, h, steps):
		x = np.linspace(0,h*steps,steps)
		y,E,E_error = self.dp.iterateMethod(method, h, steps)
		print "Plotting..."
		self.subplots.append(self.fig.add_subplot(self.rows,1,self.row_counter))
		self.subplots[self.row_counter-1].set_ylabel('Relative Energy Error')
		self.subplots[self.row_counter-1].plot(x,y[0])
		self.subplots[self.row_counter-1].plot(x,y[1])
		#self.subplots[self.row_counter-1].plot(x,y[2])
		#self.subplots[self.row_counter-1].plot(x,y[3])
		#self.subplots[self.row_counter-1].plot(x,E_error)
		#plt.hist(E_error,np.linspace(0,E_error.max(),100))
		self.row_counter += 1

	def show(self):
		plt.ticklabel_format(axis='y', style='sci')
		plt.show()
