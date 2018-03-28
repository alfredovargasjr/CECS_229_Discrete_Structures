# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:08:01 2018

@author: varga
"""
days = 7
total_min = days * 24 * 60
print(total_min)

print(2304811 % 47)
print(2304811 / 47)
print(6.002e23)
print(((673 + 909) % 3) == 0)
print((673 % 3 == 0) and (909 % 3 == 0))

L = set() 
L = {1,2,3}
L.add(5)
L.remove(1)
len(L)
print(sum({1,2,3}))
print(sum(L))

pow = 2**3

s = {1,2,3}
s or {3,4,5}

#List
m = [1,2,3] + ["test"]
m.append("appending")
len(m)
m[0]

for i in range(0, len(m)):
    print(m[i])
    
#nested for loops
n = []
m = [(x,y) for x in range(10) for y in range(10)]

n = [0,1,2,3,4]
s = [2**i for i in range(5)]

ss = []
for i in range(5):
    ss.append(2**i)
    
y = [a*b for a in range(1,10) for b in range(1,10)]

#expressions 
y1 = [20,10,15,75]
avg = sum(y1) / len(y1)

letters = ['A', 'B', 'C']
numbers = [2,3,4]
y2 = [[l,n] for l in ['A', 'B', 'C'] for n in [2,3,4]]

#Tuples (Map)
a,b = [3,6]

tupleList = zip(letters, numbers)
tupleListSet = set(tupleList)

l = [1,2,3]
m = [4,5,6]
p = [7,8,9]
[(i,j,k) for i in l for j in m for k in p if(i + j + k == 12)]

#Dictionary
dicTest = {"m":10, "n":5}
dicTest.keys()
dicTest.values()
dicTest["o"] = 12

[[m,n] for m in dicTest.keys() for n in dicTest.values()]

dictTest1 = {}
for i in range(100):
    dictTest1[i] = i**2

