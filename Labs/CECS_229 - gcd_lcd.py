# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:10:59 2018

@author: varga
"""

#This will return the factorization of n
#   - the list will have the number of times that factor is in n
#   - starting at 2.. until n is 1
def factors_List(n):
    i = 2
    reps = 0
    facts = []
    while n > 1 :
        if n % i == 0:
            reps = reps + 1
            n = int(n / i)
        else:
            facts.append(reps)
            reps = 0
            i = i + 1
    facts.append(reps)
    return facts


def gcd(a, b):
    factA = factors_List(a)
    factB = factors_List(b)
    lenA = len(factA)
    lenB = len(factB)
    if lenA < lenB:
        for i in range(lenB - lenA):
            factA.append(0)
    if lenA > lenB:
        for i in range(lenA - lenB):
            factB.append(0)
    gcdiv = 1
    j = 2
    for i in range(len(factA)):
        gcdiv = gcdiv * (j**(min(factA[i], factB[i])))
        j = j + 1
    return gcdiv

def lcm(a, b):
    factA = factors_List(a)
    factB = factors_List(b)
    lenA = len(factA)
    lenB = len(factB)
    if lenA < lenB:
        for i in range(lenB - lenA):
            factA.append(0)
    if lenA > lenB:
        for i in range(lenA - lenB):
            factB.append(0)
    lcmult = 1
    j = 2
    for i in range(len(factA)):
        lcmult = lcmult * (j**(max(factA[i], factB[i])))
        j = j + 1
    return lcmult

def eucludian_gcd(b, a):
    x = b
    y = a
    while x != 0:
        r = y % x
        y = x
        x = r
    return y

print(gcd(0,5))
print(eucludian_gcd(120,500))
print(lcm(120,500))