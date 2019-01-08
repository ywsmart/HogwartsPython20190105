#!/usr/bin/env python
#coding=utf-8


import numpy as np
from pylab import plt
#%pylab inline
#%matplotlib inline
x = np.linspace(0,10)
plt.plot(x,np.sin(x), x,np.cos(x))
#plt.imsave("test.jpg")
plt.savefig('foo.png', bbox_inches='tight')
plt.show()

'''
from mayavi import mlab
mlab.init_notebook()
s = mlab.test_plot3d()
'''