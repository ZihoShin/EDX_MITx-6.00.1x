# -*- coding: utf-8 -*-
"""
Created on Thu Oct  11 12:02:21 2016

@author: zshin

Problem 3
"""
def getAvailableLetters(lettersGuessed):
    s=list(string.ascii_lowercase)
    for a in lettersGuessed:
        if a in s:
            s.remove(a)
    return ''.join(str(x) for x in s)
 
def ispresent(secretWord,g):
    x=list(secretWord)
    if g in x:
        return True
    else:
        return False
   
