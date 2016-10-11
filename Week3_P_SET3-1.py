# -*- coding: utf-8 -*-
"""
Created on Thu Oct  11 12:02:21 2016

@author: zshin

Problem 3
"""
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set(secretWord) <= set(lettersGuessed)

   
