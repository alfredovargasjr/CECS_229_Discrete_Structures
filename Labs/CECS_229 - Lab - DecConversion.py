# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:59:08 2018

@author: varga
"""
    
def convert(n, b):
    q = n
    a = []
    if q == 0:
        return [0]
    while(q != 0):
        a.append(q % b)
        q = int(q / b)
    a.reverse()
    return a

def getSquare(n):
    return n * n
    
dictionary = {}
for i in range(100):
    dictionary[i] = convert(i, 2)
#print(dictionary)

dictSquares = {}
for i in range(100):
    dictSquares[i] = getSquare(i)

#print({k:getSquare(k) for k in range(100)})
    
names = ['Larry', 'Curly', '', 'Moe']
id_salary = {0:1000, 3:990, 1:1200.50}
names_salary = {}
for i in range(len(names)):
    names_salary[names[i]] = id_salary.get(i)
print(names_salary)

def nextInts(a):
    y = []
    for i in range(len(a)):
        y.append(a[i] + 1)
    return y

t = [1,5,7]
print(nextInts(t))

def dict2List(dct, keyList):
    output = []
    for k,v in dct.items():
        if k in keyList:
            output.append(k)
    return output

keys = ["x", "w"]
dictL = {"x": "Ex", "w":"World"}
print(dict2List(dictL, keys))

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i > 0:
            i = i + 1
        else:
            factors.append(i)
            n = n / i
    if i > 1:
        factors.append(n)
    return factors

number = 331
print(factorization(8191))

def findPrimes_IP(L):
    primes = []
    for i in range(len(L)):
        if isPrime(L[i]):
            primes.append(L[i])
    return primes

def findPrimes(n):
    primes_out = [i for i in range(2,n+1)]
    for i in primes_out:
        factors = [i for i in range(i,n+1,i)]
        for f in factors:
            if f in primes_out:
                primes_out.remove(f)
    return primes_out

