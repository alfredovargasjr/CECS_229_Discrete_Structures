# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:03:31 2018

@author: Alfredo Vargas

CECS 229 - Lab 1
"""

#1 Enter a Boolean expression to test whether the sum of 673 and 909 is divisible by 3.
print((673 + 909) % 3 == 0)

#2 Write a comprehension over {0, 1, 2, 3, 4} who value is the set consisting of the first give powers of two, starting with 20
powersSet = {2**x for x in {0,1,2,3,4}}
print(powersSet)

#3 The value of the previous comprehension {x*y for x in {1, 2, 3} for y in {2, 3, 4}} is a seven-element set. Replace {1, 2, 3} and {2, 3, 4} with two other three-element sets so that the value becomes a nine-element set.
print({x*y for x in {1,2,3} for y in {5,6,7}})

#4 Write a double list comprehension over the lists ['A', 'B', 'C'] and [1, 2, 3] whose value is the list of all possible two-element lists [letter, number]. That is, the value is [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 2], ['C', 3]]
print([(x,y) for x in ['A', 'B', 'C'] for y in [1,2,3]])

#5 Suppose S is a set of integers = {-4, -2, 1, 2, 5, 0}.
s = {-4,-2,1,2,5,0}

    #Write a triple comprehension whose value is a list of all three-element tuples (i, j, k) such that i, j, k are elements of S whose sum is zero.
print({(i,j,k) for i in s for j in s for k in s if (i+j+k) == 0 })
    #Modify the comprehension of the previous task so that the resulting list does not include (0, 0, 0).
print({(i,j,k) for i in s for j in s for k in s if (i+j+k) == 0 and (i!=0 or j!=0 or k!=0)})

    #Modify the expression so that its value is not the list of all such tuples but is the first such tuples
    