# -*- coding: utf-8 -*-
"""
Created on Thu Oct  11 12:02:21 2016

@author: zshin

Problem 3
"""
def getGuessedWord(secretWord, lettersGuessed):
    result=''
    for e in secretWord:
        if e in lettersGuessed:
            result+=e
        else:
            result+=' _ '
    return result

   
