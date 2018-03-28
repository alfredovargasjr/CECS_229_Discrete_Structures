# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:02:25 2018

@author: alfredo vargas
    CECS 229
    Lab - Shift Cypher
            - Encryption using character shift
            - Decryption knowing the shift amount
"""
def shift_encrypt(s, shift):
    string = list(s)
    for i in range(len(string)):
        if string[i].isalpha():
            string[i] = chr(((ord(s[i]) - 97) + shift) % 26 + 97)
    return ''.join(string)

def shift_decrypt(s, shift):
    string = list(s)
    for i in range(len(string)):
        if string[i].isalpha():
            string[i] = chr(((ord(s[i]) - 97) - shift) % 26 + 97)
    return ''.join(string)

def affin_encrypt(s, a, b):
    string = list(s)
    for i in range(len(string)):
        if string[i].isalpha():
            string[i] = chr((((ord(s[i]) - 97)*a) + b) % 26 + 97)
    return ''.join(string)

def affin_decrypt(s, a, b):
    string = list(s)
    for j in range(26):
        j = 1
        string = list(s)
        for i in range(len(string)):
            if string[i].isalpha():
                string[i] = chr(int((((ord(s[i]) - 97) - b) / a + j)) % 26 + 97)
        print(''.join(string))
        j = j + 1
    return ''.join(string)

l = 'encrypt this homie'
encrypted = shift_encrypt(l, 5)
decrypted = shift_decrypt(encrypted, 5)
affinencrypt = affin_encrypt(l,2,3)
affindecrypt = affin_decrypt(affinencrypt,2,3)
print(encrypted)
print(decrypted)
print(affinencrypt)
print(affindecrypt)