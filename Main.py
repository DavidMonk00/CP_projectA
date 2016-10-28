'''
Created on 26 Oct 2016

@author: david
'''

import numpy as np
import SmallAngle as sa
import Plot

A = 0.5
D = 0
start = np.array([A,0.0])
pt = Plot.Plot(D,start,2)

h = 0.1
steps = int(np.pi*10/h)
method = sa.SmallAngle.implicitEulerMethod
pt.plotMethod(method,h,steps,True)
pt.error(method, h,steps)

pt.show()
