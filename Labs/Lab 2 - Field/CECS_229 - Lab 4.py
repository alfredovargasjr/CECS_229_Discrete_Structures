# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:24:19 2018

@author: alfredo vargas

Lab 4: Vectors and Complex numbers
CECS 229

"""
import math
import cmath
import matplotlib.pyplot as plt

# =============================================================================
# 1.	Given S = {2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j} and 
# T = {(e**(2*pi*1j/20))**x for x in range(20)}, use the function 
# def transform(L,a,b): return{a*x+b for x in L} to produce the following image.
# =============================================================================

S = [(2+2j),(3+2j),(1.75+1j),(2+1j),(2.25+1j),(2.5+1j),(2.75+1j),(3+1j),(3.25+1j)]
T = [(math.e**(2*math.pi*1j/20))**x for x in range(20)]

def transform(L,a,b): return[a*x+b for x in L]

y1 = transform([y.imag for y in S], 1, -1)

x = [x.real for x in transform(S,1,-2.5) + T]
y = [y.imag for y in transform([y.imag for y in S],1,-1) + T]
plt.scatter(x,y)
plt.show()
