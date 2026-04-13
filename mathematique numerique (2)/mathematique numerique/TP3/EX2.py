# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 10:21:16 2025

@author: asvini 
"""

"EX2"
import numpy

A=numpy.array([[1.,-1.,2.],[2.,1.,-1],[-2.,2.,2.]])
b=numpy.array([6.,-1.,0.])


def SolveTriSup(A,b):
    n=b.size
    x=numpy.zeros(n)
    

def Triangulaire(A,b):
    [n1,n2]=A.shape
    for i in range (n2-1): #i=>colone
        for j in range(i+1,n1): #j=>ligne
            print(i,j)
            pivot=A[j,i]/A[i,i]
            for k in range(n2): # peut-on faire m
                A[j,k]-=pivot*A[i,k]
            b[j]-=pivot*b[i]
        #print(A,b)
    return 1#[A,b]
        
#[A,b]=Triangulaire(A,b)
Triangulaire(A,b)
x=SolveTriSup(A,b)
print (x)
"""
            coeff=A[n1][n2]-=coeff*A[n1][n2]
            for k in range(j):
                A[][???]-=coeff*A[???][???]
            b[???]-=coef*b[???]

            
def SolveTriSup(U,b):
    n=b.size
    x=numpy.zeros(n)
    
    return x

"""
