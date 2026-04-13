# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 09:58:56 2025

@author: asvini
"""

"EX2"

import numpy

U=numpy.array([[1.,-1.,1.,2.],[0.,-2.,1.,-1.],[0.,0.,-1.,1.],[0,0.,0.,2.]])
b=numpy.array([1.,2.,-2.,-2.])
def SolveTriSup(U,b):
    n=len(b)
    x=numpy.zeros(n)
    
    for i in range(n):
        ii=n-1-i #indice de ligne courant
        somme=0
        for j in range(i):
            jj=n-1-j
            somme+=U[ii,jj]*x[jj]
        x[ii]=(1/U[ii,ii])*(b[ii]-somme)
    
    return(x)
x=SolveTriSup(U,b)

print(x)