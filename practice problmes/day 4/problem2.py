# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row,col) enter the player's initial. 
# If the player  A rolls the dice and  if  player B already has their initial in the same row,col
# add a point to A and change the initial to A. 

# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
# Use functions

import random
import time

def displayBoard(board):                                    #function to display board everytime
    for i in range(6) :
        for j in range(6):
            print(board[i][j],end=" ") 
        print()


def game(initial_1,initial_2) :
    
    rows, cols = 6, 6                                       #initialising empty board
    board = [['_'] * 6 for _ in range(6)]

    displayBoard(board)
        
    score = [0,0]                                          #initialising scores
    symbols = [initial_1.upper(),initial_2.upper()]        #creating symbols list for easier access within the for loop
    
    #initialising a while loop until any one players gets 5 points
    while(score[0] != 5 and score[1] != 5) :
        
        #for loop to roll the dice and update the score
        for i in range (2) :
            initial = symbols[i]
            print("Player ", i+1,"rolls the dice : ") 
            row, col= random.randint(1, 6),random.randint(1, 6)         #generating random numbers
            print(row,col)

            #checking for positions and updating the score accordingly
            if board[row-1][col-1] == '_' :
                board[row-1][col-1] = initial
            elif board[row-1][col-1]!= initial :
                board[row-1][col-1] = initial
                score[i] += 1
                print(f"Player {i+1}, gets a point")
            displayBoard(board)                                         
            time.sleep(1)                                               #pausing the execution for a second to track the output
            if score[i] == 5 :                                          #breaking out of the loop once if any one of the players gets 5 points                          
                break
            
    index = score.index(5)
    print("Winner : Player ", i+1)
    
    
#main code
initial_1 = input("Enter the initials of player 1 : ")
initial_2 = input("Enter the initials of player 2 : ")
game(initial_1,initial_2)



