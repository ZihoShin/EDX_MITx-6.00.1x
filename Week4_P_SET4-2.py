# -*- coding: utf-8 -*-
"""
Created on Thu Oct  10 12:02:21 2016

@author: zshin

Problem 4
"""
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    handCopy = hand.copy()
    for i in word:
        handCopy[i] -= 1
    return handCopy


