# File: proj1.py
# Author: Uzoma Uwanamodo
# Date: 11/14/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# A Connect Four game
# Collaboration:
# I did not collaborate with anyone on this assignment


# The user's menu options

LOAD_GAME = "y"
NEW_GAME = "n"



#   loadGame() load save game if user requests
#   Input: None
#   Output: 2D array, the game board if user requests to load game or an empty one
def loadGame():
    
    # Ask user whether or not they want to load a game
    load = ""
    while not load in [LOAD_GAME,NEW_GAME]:
        load = input("Would you like to load a game (%s/%s)? " % (LOAD_GAME,NEW_GAME))
    
    if load == LOAD_GAME:
        open(input("What game file would you like to load from? "))
    
    

def main():
    
    # Print welcome message
    print("Welcome to Connect Four\nThis game is for two players")
    
    
    
    
    
main()