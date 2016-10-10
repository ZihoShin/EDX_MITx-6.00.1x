# -*- coding: utf-8 -*-
"""
Created on Thu Oct  10 12:02:21 2016

@author: zshin

Problem 4
"""
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    handCopy = hand.copy()
    wordDic = {}
    for i in word:
        wordDic[i] = wordDic.get(i, 0) + 1
    count = 0
    for j in word:
        count += wordDic[j] <= handCopy.get(j, 0)
    return count == len(word) and word in wordList            
    

