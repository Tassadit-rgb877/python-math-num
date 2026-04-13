# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:26:40 2025

@author: asvini
"""
import numpy


xi=numpy.array([-1,0,1,2])
yi=numpy.array([1,2,5,4])

def l1(x): #cas particulier pour 4 pt
    return(x-xi[1])/(xi[0]-xi[1])*(x-xi[2])/(xi[0]-xi[2])*(x-xi[3])/(xi[0]-xi[3])

def l2(x): #cas particulier pour 4 pt
    return(x-xi[0])/(xi[1]-xi[0])*(x-xi[2])/(xi[1]-xi[2])*(x-xi[3])/(xi[1]-xi[3])

def l3(x): #cas particulier pour 4 pt
     return(x-xi[0])/(xi[2]-xi[0])*(x-xi[1])/(xi[2]-xi[1])*(x-xi[3])/(xi[2]-xi[3])

def l4(x): #cas particulier pour 4 pt
     return(x-xi[0])/(xi[3]-xi[0])*(x-xi[1])/(xi[3]-xi[1])*(x-xi[2])/(xi[3]-xi[2])


for x in xi:
    print("l1(",x,")=",l1(x))

for x in xi:
    print("l2(",x,")=",l2(x))

for x in xi:
    print("l3(",x,")=",l3(x))

for x in xi:
    print("l4(",x,")=",l4(x))

import matplotlib.pyplot as pyplot 

n_trace=100
x_trace=numpy.linspace(min(xi),max(xi),n_trace)
y1_trace=numpy.zeros(n_trace)
y2_trace=numpy.zeros(n_trace)
y3_trace=numpy.zeros(n_trace)
y4_trace=numpy.zeros(n_trace)
y_trace=numpy.zeros(n_trace)#interpolant global

for i in range(n_trace):
    y1_trace[i]=l1(x_trace[i])
    y2_trace[i]=l2(x_trace[i])
    y3_trace[i]=l3(x_trace[i])
    y4_trace[i]=l4(x_trace[i])
    
    y_trace[i]+=yi[0]*y1_trace[i]
    y_trace[i]+=yi[1]*y2_trace[i]
    y_trace[i]+=yi[2]*y3_trace[i]
    y_trace[i]+=yi[3]*y4_trace[i]
    
    
pyplot.close('all')
pyplot.figure(1)
pyplot.plot(x_trace,y1_trace,'-r')
pyplot.plot(x_trace,y2_trace,'-g')
pyplot.plot(x_trace,y3_trace,'-b')
pyplot.plot(x_trace,y4_trace,'-y')

pyplot.figure(2)
pyplot.plot(x_trace,y_trace,'-k')
pyplot.plot(xi,yi,'ro')

'''
def p(x,xi,yi):
    n=len(xi)
    somme=0
    for i in range(n):
        
        for j in range(n):
            
    return somme
    
'''