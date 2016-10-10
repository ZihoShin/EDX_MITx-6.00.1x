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
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    while True: 
        user = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ') 
        if user == 'n': 
            while True: 
                user_t = input('Enter u to have yourself play, c to have the computer play: ') 
                n = HAND_SIZE 
                if user_t == 'u': 
                    hand = dealHand(n)
                    playHand(hand, wordList, n) 
                    break 
                elif user_t == 'c': 
                    hand = dealHand(n)
                    compPlayHand(hand, wordList, n) 
                    break 
                else:
                    print("Invalid command.") 
        elif user == 'r': 
                while True: 
                    try: 
                        len(hand) > 0 
                        user_r = input('Enter u to have yourself play, c to have the computer play: ') 
                        if user_r == 'u': 
                            playHand(hand, wordList, n) 
                            break 
                        elif user_r == 'c': 
                            compPlayHand(hand, wordList, n) 
                            break 
                        else: 
                            print ("Invalid command.")
                    except: 
                        print ('You have not played a hand yet. Please play a new hand first!' )
                        break
        elif user == 'e': 
            break 
        else: 
            print ("Invalid Command.")
    

                        
