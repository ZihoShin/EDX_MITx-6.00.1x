# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:50:21 2016

@author: zshin

Problem 2

(10/10 points)
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2

"""
size = len(s)
count = 0
for loop in range (0, size):
    if(loop+2 < size):
        if(s[loop] == 'b' and s[loop+1] =='o' and s[loop+2] =='b'):
            count += 1
    else:
        count = count
print (count)
