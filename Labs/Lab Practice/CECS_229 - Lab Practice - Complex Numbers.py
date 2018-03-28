# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:33:27 2018

@author: Alfredo Vargas

Lab Practice for Complex Numbers using Python
CECS 229
"""
import cmath
import math

z1 = complex(1,2)
z2 = complex(3,4)
z90 = complex(0,1)

print(z1 + z2)
print(z1*z2)

z3 = z1 + z2

print(cmath.phase(z3))  #return radians 
print(cmath.polar(z3))  #returns (radius, degree)
print(math.degrees(cmath.phase(z90)))
