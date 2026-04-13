# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import numpy
import matplotlib.pyplot as pyplot

pyplot.close('all')

def f(x):
    valeur=math.sin(x)
    return valeur

def g(x):
    val=(-0.0624+1.32*x-0.418*x**2)
    return val

nb_points=20
x_min=-5
x_max=5
dx=(x_max-x_min)/(nb_points-1)
x=numpy.zeros(nb_points)
y=numpy.zeros(nb_points)
y1=numpy.zeros(nb_points)

for i in range(nb_points):
    xi=x_min+i*dx
    x[i]=xi
    y[i]=f(xi)
    
    y1[i]=g(xi)
    
pyplot.plot(x,y,'-bo')
pyplot.plot(x,y1,'-rs')



