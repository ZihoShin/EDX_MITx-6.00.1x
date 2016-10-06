# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:50:21 2016

@author: zshin

Problem 1

(10/10 points)
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5

"""
size = len(s)

count = 0
for o in range (0,size):
    if (s[o] == 'a'):
        count += 1
    elif (s[o] == 'e'):
        count += 1
    elif (s[o] == 'i'):
        count +=1
    elif (s[o] == 'o'):
        count += 1
    elif (s[o] == 'u'):
        count += 1
    else:
        count = count
print (count)
