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

def newGame():
    rows, cols = 5, 5
    arr = [['_']*cols]*rows

def game(initial_1,initial_2) :
    newGame()
    symbols = [initial_1.upper(),initial_2.upper()]
    random_number = random.randint(1, 6)





