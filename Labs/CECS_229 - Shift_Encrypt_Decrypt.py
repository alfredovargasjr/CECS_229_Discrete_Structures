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
        string[i] = chr(((ord(s[i]) - 97) + shift) % 26 + 97)
    return ''.join(string)

def shift_decrypt(s, shift):
    string = list(s)
    for i in range(len(string)):
        string[i] = chr(((ord(s[i]) - 97) - shift) % 26 + 97)
    return ''.join(string)

l = 'alfredo'
encrypted = shift_encrypt(l, 5)
decrypted = shift_decrypt(encrypted, 5)
print(encrypted)
print(decrypted)