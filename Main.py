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
pt = Plot.Plot(D,start)
h = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

i = 0.001
#for i in h:
#pt.plotMethod(sa.SmallAngle.leapfrogMethod,i,int(np.pi*2/i))
#pt.plotMethod(sa.SmallAngle.eulerForwardMethod,i,int(np.pi*2/i))
#pt.analytical(i,int(np.pi*2/i),A)
pt.error(sa.SmallAngle.rk4Method, i,int(np.pi*100/i))
pt.show()
