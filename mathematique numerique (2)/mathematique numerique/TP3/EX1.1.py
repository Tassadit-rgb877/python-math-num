# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 08:57:34 2025

@author: asvini
ex1

"""

"ex1 Q2"

"""
import numpy

L=numpy.array([[2.,0.,0.,0],[1.,-2.,0.,0.],[1.,2.,-1.,0.],[0,1.,-2.,3]])
b=numpy.array([6.,1.,1.,-1.])
n=len(b)
x=numpy.zeros(n)

for i in range(n):
    somme=0
    for j in range(i):
        somme+=L[i,j]*x[j]
    x[i]=(1/L[i,i])*(b[i]-somme)

print(x)
"""

"EX1 Q3"
import numpy

L=numpy.array([[2.,0.,0.,0],[1.,-2.,0.,0.],[1.,2.,-1.,0.],[0,1.,-2.,3]])
b=numpy.array([6.,1.,1.,-1.])
def SolveTriInf(L,b):
    n=len(b)
    x=numpy.zeros(n)
    
    for i in range(n):
        somme=0
        for j in range(i):
            somme+=L[i,j]*x[j]
        x[i]=(1/L[i,i])*(b[i]-somme)
    
    return(x)
x=SolveTriInf(L,b)

print(x)

