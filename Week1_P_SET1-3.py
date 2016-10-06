# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:47:13 2016

@author: zshin

Problem 3

(15/15 points)
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

"""
MAX = ''
CHK = ''
for char in s:
    if (CHK == ''):
        CHK = char
    elif (CHK[-1] <= char):
        CHK += char
    elif (c[-1] > char):
        if (len(MAX) < len(CHK)):
            MAX = CHK
            CHK = char
        else:
            CHK = char
if (len(CHK) > len(MAX)):
    MAX = CHK
print(MAX)

