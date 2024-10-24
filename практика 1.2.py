# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:14:59 2024

@author: ubkstud
"""
import math
import numpy as np
xx = [1, 10, 100]
print('xx =', xx, type(xx))

x = xx[0]
print('x =', x, type(x))

y = 5/4+1/x**(1/5)
print('y =', y, type(y))
t = math.exp(1/(math.sin(x)+1))
y = math.log(t/y, 1+x*x)
print('y=', y, type(y))

yy=5/4 + np.power(xx, -1/5)
print ('yy=', yy, type(yy))
t= np.exp(1/(np.sin(xx)+1))
print ('t=', t, type(t))
yy = np.log(t/yy) / np.log(1+np.power(xx,2))

print('yy=', yy, type(yy))
