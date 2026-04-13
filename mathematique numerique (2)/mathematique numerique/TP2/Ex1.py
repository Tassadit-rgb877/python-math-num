# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 08:49:12 2025

@author: asvini
"""

import numpy
import matplotlib.pyplot as pyplot 
pyplot.close('all')

x_interp=numpy.array([-1,0,1,2])
y_interp=numpy.array([1,2,5,4])

n=len(x_interp)
A=numpy.zeros([n,n])
b=numpy.zeros(n)
coeff=numpy.zeros(n)
'''
#remplir la matrice(case par case ou par ligne) et du vecteur
A[0][0]=1
A[0][1]=x_interp[0]
A[0][2]=x_interp[0]**2
A[0][3]=x_interp[0]**3
A[1][0]=1
A[1][1]=x_interp[1]
A[1][2]=x_interp[1]**2
A[1][3]=x_interp[1]**3
A[2][0]=1
A[2][1]=x_interp[2]
A[2][2]=x_interp[2]**2
A[2][3]=x_interp[2]**3
A[3][0]=1
A[3][1]=x_interp[3]
A[3][2]=x_interp[3]**2
A[3][3]=x_interp[3]**3

b[0]=y_interp[0]
b[1]=y_interp[1]
b[2]=y_interp[2]
b[3]=y_interp[3]
'''
for i in range(n):
    b[i]=y_interp[i]
    for j in range(n):
        A[i][j]=x_interp[i]**j

coeff=numpy.linalg.solve(A,b)
print(coeff)

def p(x,coeff):
    somme=0
    n=len(coeff)
    for i in range(n):
        somme+=coeff[i]*x**i
    return somme

'''
nb_points_trace=100
x_trace=numpy.zeros(nb_points_trace)
y_trace=numpy.zeros(nb_points_trace)
x_min=-1
x_max=2
dx=(x_max-x_min)/(nb_points_trace-1)
for i in range(nb_points_trace):
    xi=x_min+i*dx
    x_trace[i]=xi
    y_trace[i]=p(xi,coeff)
pyplot.plot(x_trace ,y_trace,'-k')
pyplot.plot(x_interp ,y_interp,'ro')
'''
import matplotlib.pyplot as pyplot 
n=5
x=numpy.random.random(n)
x.sort()
y=numpy.random.random(n)

def DonneCoeff(x,y):
    n=len(x)
    A=numpy.zeros([n,n])
    b=numpy.zeros(n)
    for i in range(n):
        b[i]=y[i]
        for j in range(n):
            A[i][j]=x[i]**j
    coeff=numpy.linalg.solve(A,b)
    return coeff

coeff=DonneCoeff(x,y)
n_trace=100
x_trace=numpy.linspace(x[0],x[n-1],n_trace)
y_trace=numpy.zeros(n_trace)
for i in range(n_trace):
    y_trace[i]=p(x_trace[i],coeff)
    
pyplot.plot(x_trace,y_trace,'-k')
pyplot.plot(x,y,'ro')
    
