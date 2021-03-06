# -*- coding: utf-8 -*-
"""
Created on Thu Oct  10 12:02:21 2016

@author: zshin

Problem 4
"""
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand = False 
    while True: 
        user = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ").lower() 
        if user not in 'nre': 
            print("Invalid command.") 
        else: 
            if user == 'r' and not hand: 
                print("You have not played a hand yet. Please play a new hand first!") 
            elif user == 'n': 
                hand = dealHand(HAND_SIZE) 
                playHand(hand.copy(), wordList, HAND_SIZE) 
            elif user == 'r' and hand: 
                playHand(hand.copy(), wordList, HAND_SIZE) 
            else: 
                break
            print("")

