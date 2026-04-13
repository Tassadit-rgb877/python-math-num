# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 11:48:48 2025

@author: netpc01
"""



import math
import numpy
import matplotlib.pyplot as pyplot

pyplot.close('all')


def intnum_trapeze (f,a,b):
    aire=0.5*(b-a)*(f(a)+f(b))
    return aire

def intnum_trapeze_n(f,a,b,n):
    aire=0
    dx=(b-a)/n
    for i in range(n):
        xi=a+i*dx
        xip1=xi+dx
        aire+=intnum_trapeze(f,xi,xip1)
        return aire

def f(x):
    valeur=(math.sin(x-1))**2
    return valeur

def prim_f(x):
    valeur=0,25*(2*x+math.sin(2-2*x)-2)
    return valeur

nb_points=20
x_min=1
x_max=5
dx=(x_max-x_min)/(nb_points-1)
x=numpy.zeros(nb_points)
y=numpy.zeros(nb_points)

for i in range(nb_points):
    xi=x_min+i*dx
    x[i]=xi
    y[i]=f(xi)
    
pyplot.plot(x,y,'-bo')

print('* integrale - valeur exacte :')
print(prim_f(x_max)-prim_f(x_min))
print('* estimation de l integrale - methode trapeze a '+str(n)+'support(s):')
print(intnum_trapeze_n(f,x_min,x_max,n))
