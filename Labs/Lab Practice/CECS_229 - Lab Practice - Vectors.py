# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:08:33 2018

@author: alfredo vargas

Lab Practice for Vectors and operations
CECS 229
"""
import numpy as np
from PIL import Image

# =============================================================================
# suppose we represent n-vectors by n-element list. Write a proc scalar vector
# mult(alpha, v) that mult the vector v by the scalar alpha
# =============================================================================
u = [5,2]
v = [4,1]

def scalar_vector_mult(alpha, v): return [alpha*x for x in v]

def vector_add(u, v): 
    if len(u) == len(v):
        return [u[i]+v[i] for i in range(len(u))]
    print("Vectors are not the same size")


print(scalar_vector_mult(0.3, u))
print(vector_add([3,2], [2,3]))
print(vector_add(scalar_vector_mult(0.4, u), v))

img = Image.open('morty.png').convert('RGBA')
u = np.array(img)
u_array = u.ravel()

shape = u.shape

img = Image.open('rick.png').convert('RGBA')
v = np.array(img)
v_array = v.ravel()

u1 = scalar_vector_mult(0.5,u_array)
v1 = scalar_vector_mult(0.5,v_array)

uv = vector_add(u1,v1)

result = np.asarray(uv).reshape(shape)

uv_image = Image.fromarray(result, 'RGBA')
uv_image.show()