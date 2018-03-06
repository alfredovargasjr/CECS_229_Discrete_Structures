# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:06:34 2018

@author: alfredo vargas

CECS 229
Lab 3
"""

# =============================================================================
# 1.	Define a one-line procedure cubes(L) specified as follows: 
# • input: list L of numbers 
# • output: list of numbers whose ith element is the cube of the ith element of 
#   L 
# • example: input [1, 2, 3], output [1, 8, 27].
# =============================================================================

def cubes(L):
    return [i**3 for i in L]
print(cubes([1,2,3,4]))

# =============================================================================
# 2.	Define a one-line procedure dict2list(dct,keylist) with this spec: 
# • input: dictionary dct, list keylist consisting of the keys of dct 
# • output: list L such that L[i] = dct[keylist[i]] for i = 0, 1, 2,..., 
#   len(keylist) - 1 
# • example: input dct={'a':'A', 'b':'B', 'c':'C'} and keylist=['b','c','a'], 
#   output ['B', 'C', 'A']
# =============================================================================

def dict2list(dct, keylist):
    return [dct[x] for x in keylist]

dct={'a':'A', 'b':'B', 'c':'C'}
keylist=['b','c','a']
print(dict2list(dct, keylist))

# =============================================================================
# 3.	Define a one-line procedure list2dict(L, keylist) specified as follows: 
# • input: list L, list keylist of immutable items 
# • output: dictionary that maps keylist[i] to L[i] for i = 0, 1, 2,..., 
#   len(L) - 1 
# • example: input L=[’A’,’B’,’C’] and keylist=[’a’,’b’,’c’], 
#   output {'a':'A', 'b':'B', 'c':'C'} 
# Hint: Use a comprehension that iterates over a zip or a range
# =============================================================================

def list2dict(L, keylist):
    return {L[i]:keylist[i] for i in range(len(L))}

L=['A','B','C']
keylist=['a','b','c']
print(list2dict(L,keylist))