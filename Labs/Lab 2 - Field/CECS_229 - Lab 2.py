# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 08:47:12 2018

@author: alfredo vargas

CECS 229
Lab 2

Complex numbers on a complex graph
"""

import math
import cmath
import matplotlib.pyplot as plt

import image
import plotting

# =============================================================================
# 1.	Given S = {2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j} and 
# T = {(e**(2*pi*1j/20))**x for x in range(20)}, use the function 
# def transform(L,a,b): return{a*x+b for x in L} to produce the following image.
# =============================================================================

S = [(2+2j),(3+2j),(1.75+1j),(2+1j),(2.25+1j),(2.5+1j),(2.75+1j),(3+1j),(3.25+1j)]
T = [(math.e**(2*math.pi*1j/20))**x for x in range(20)]

def transform(L,a,b): return[a*x+b for x in L]

S1 = transform(S, 1, -1.5j - 2.5)

x = [x.real for x in S1 + T]
y = [y.imag for y in S1 + T]

xy = [(x.real, x.imag) for x in S1+T ]

plotting.plot(xy, scale=3, dot_size = 3, browser=None)

# =============================================================================
# Task 1.4.10 - Use a comprehension to assign to a list pts the set of complex numbers x + yi 
# such that the image intensity of pixel (x, y) is less than 120, and plot the 
# list pts.
# =============================================================================

# =============================================================================
# imported method that coverts image file into a 2D list, each element
#   contains the intesity of pixel(x,y)
# =============================================================================

# convert 2D list into a set of complex points.
def listList2set(L):
    points = []
    for y in range(len(L)):
        for x in range(len(L[0])):
            if L[y][x][0] < 120:
                points.append(complex(x,len(L)-y))
    return points

image = image.file2image('img01.png')
plotimg = listList2set(image)
    # scaling the image to .20 of its size"
setImg = transform(plotimg,0.20,0+0j)
plotting.plot(setImg)

# =============================================================================
# Task 1.4.19 - rotate the above image
# =============================================================================

def rotateRad(L, rd):
    # use euler's method to change the angle's radius (translate the points)
    return [complex(z.real*math.cos(rd*math.pi)-z.imag*math.sin(rd*math.pi),z.real*math.sin(rd*math.pi)+z.imag*math.cos(rd*math.pi)) for z in L]

plotting.plot(rotateRad(setImg,0.25))