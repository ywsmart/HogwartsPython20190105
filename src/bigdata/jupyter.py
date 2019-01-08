#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
#%pylab inline
x = np.linspace(0,10)
plt.plot(x,np.sin(x), x,np.cos(x))
#plt.show()
