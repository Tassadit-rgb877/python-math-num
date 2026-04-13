# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 12:20:05 2025

@author: asvini
"""


import numpy

x=numpy.array([0,1,0,-1,0,1])
y=numpy.array([0,0,1,0,1,1])
z=numpy.array([86,88,71,80,95,73])

n=len(x)

A=numpy.zeros([n,n])
b=numpy.zeros(n)

for i in range (n):
    A[i]=[1,x[i],y[i],x[i]**2,x[i]*y[i],y[i]**2]
    
b=z
coeff=numpy.linalg.solve(A,b)

def p(x,y,coeff):
    monomes=numpy.array([1,x,y,x**2,x*y,y**2])
    return coeff@monomes