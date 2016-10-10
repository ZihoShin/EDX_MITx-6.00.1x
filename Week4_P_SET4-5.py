# -*- coding: utf-8 -*-
"""
Created on Thu Oct  10 12:02:21 2016

@author: zshin

Problem 4
"""
def playHand(hand, wordList, n): 
     totalScore = 0 
     output = "Run out of letters." 
     while calculateHandlen(hand) > 0: 
         displayHand(hand) 
         word = input('Enter word, or a "." to indicate that you are finished: ').lower() 
         if word == '.': 
             output = "Goodbye!" 
             break 
         else: 
             if not isValidWord(word, hand, wordList): 
                 print("Invalid word, please try again.") 
             else: 
                 score = getWordScore(word, n) 
                 totalScore += score 
                 print('"{0:s}" earned {1:d} points. Total: {2:d} points.'.format(word, score, totalScore)) 
                 hand = updateHand(hand, word) 
     print('{0:s} Total score: {1:d} points.'.format(output, totalScore)) 

