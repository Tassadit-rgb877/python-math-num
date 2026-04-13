# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 09:41:41 2025

@author: netpc01
"""

import math
import numpy
import matplotlib.pyplot as pyplot

pyplot.close('all')

def intnum_Rectangle(f,a,b):
    aire1=(b-a)*f(0.5*(a+b))
    return aire1

def intnum_trapeze (f,a,b):
    aire=0.5*(b-a)*(f(a)+f(b))
    return aire

def intnum_Simpson(f,a,b):
    aire2=((b-a)/6)*(f(a)+4*f((a+b)/2)+f(b))
    return aire2

def intnum_GLeg2(f):
    nb_points=2
    xi=[-math.sqrt(1/3),math.sqrt(1/3)]
    wi=[1,1]
    somme=0
    for i in range(nb_points):
        somme+=wi[i]*f(xi[i])
    return somme

def intnum_GLeg3(f):
    nb_points=3
    xi=[-math.sqrt(3/5),0,math.sqrt(3/5)]
    wi=[5/9,8/9,5/9]
    somme=0
    for i in range(nb_points):
        somme+=wi[i]*f(xi[i])
    return somme

def intnum_GLob4(f):
    nb_points=3
    xi=[-1,-math.sqrt(1/5),math.sqrt(1/5),1]
    wi=[1/6,5/6,5/6,1/6]
    somme=0
    for i in range(nb_points):
        somme+=wi[i]*f(xi[i])
    return somme

def f(x):
    #valeur=(math.sin(x-1))**2
    valeur=((x-(1/2))**0+1)
    return valeur

nb_points=20
x_min=-1
x_max=1
dx=(x_max-x_min)/(nb_points-1)
x=numpy.zeros(nb_points)
y=numpy.zeros(nb_points)

for i in range(nb_points):
    xi=x_min+i*dx
    x[i]=xi
    y[i]=f(xi)
    
pyplot.plot(x,y,'-bo')

print('* integrale - valeur exacte :')
print(1-math.sin(4)/4)
print('* estimation de l integrale - methode rectangle :')
print(intnum_Rectangle(f,-1,1))
print('* estimation de l integrale - methode trapeze :')
print(intnum_trapeze(f,-1,1))
print('* estimation de l integrale - methode Simpson :')
print(intnum_Simpson(f,-1,1))
print('* estimation de l integrale - methode Gauss-Legendre 2 points :')
print(intnum_GLeg3(f))
print('* estimation de l integrale - methode Gauss-Legendre 3 points :')
print(intnum_GLob4(f))
print('* estimation de l integrale - methode Gauss-Lobato 4 points :')
print(intnum_GLeg2(f))