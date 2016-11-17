# File: proj1.py
# Author: Uzoma Uwanamodo
# Date: 11/14/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# A Connect Four game
# Collaboration:
# I did not collaborate with anyone on this assignment





# I was not able to complete the win/lose functionality

# The user's menu options

YES = "y"
NO= "n"
MINIMUM_ROWS = 5
MINIMUM_COLUMNS = 5
BLANK_SPACE = "_"
PLAYER_TOKENS = ["x","o"]
SAVE_FILE_ACTION = "s"
DEFAULT_FILE_EXTENSION = ".txt"
SWITCH_PLAYER = 3

#   formatFileName() takes a filename and adds the deafult file extension if it is omitted
def formatFileName(file):
    
    # return the formatted file name
    return file + (DEFAULT_FILE_EXTENSION if file[-4:] != DEFAULT_FILE_EXTENSION else "")


#   newBoard() creates a new game board
#   Input: None
#   Output: 2D Array, a new game board
def newBoard():
    
    # game board dimensions
    rows  = 0
    colus = 0
    
    # prompt user for number of rows
    print("Please choose the number of rows:")
    while rows < MINIMUM_ROWS:
        rows = int(input("Please enter a number greater than or equal to %s: " % MINIMUM_ROWS))
    
    # prompt user for number of columns
        print("Please choose the number of columns:")
    while colus < MINIMUM_COLUMNS:
        colus = int(input("Please enter a number greater than or equal to %s: " % MINIMUM_COLUMNS))
    
    # return a row x columns gameboard filled with BLANK_SPACEs as placeholders
    return [list(BLANK_SPACE*colus) for i in range(rows)]  + [["1"]]

#   loadBoard() loads a game board from a save file
#   Input: None
#   Output: 2D Array, the restored game board
def loadBoard():
    
    #prompt user for the name of the save file
    saveFile = open(formatFileName(input("What game file would you like to load from? ")))
    
    # process the save file data into a game board array
    board = [list(i.strip()) for i in list(saveFile)]
    saveFile.close()
    
    return board

#   getBoard() load save game if user requests
#   Input: None
#   Output: 2D array, a game board, with the player number in the last row
def getBoard():
    
    # Ask user whether or not they want to load a game
    load = ""
    while not load in [YES,NO]:
        load = input("Would you like to load a game (%s/%s)? " % (YES,NO))
    
    # return a new game or load the new game based on user''s request
    return loadBoard() if load == YES else newBoard()
    

#   Board() take the game board array and parses it
#   Input: board, a 2D array that stores the current game board
#   delimiter, a string that determines how the text columns should be formatted
#   Output: 2D array, a game board, with the player number in the last row
def parseBoard(board,delim=""):
    
    # return the parsed board
    print(delim)
    return "\n".join([delim.join(x) for x in board])



#   displayBoard() take the game board and displays it in a user friendly manner
#   Input: board, a 2D array that stores the current game board
#   Output: 2D array, a game board, with the player number in the last row
def displayBoard(board):
    
    # return the user friendly game board, with separator space
    return parseBoard(board," ")



#   takeTurn() prompts user for their input during their "turn"
#   Input: turn and board, the current player's number and a 2D array that stores the current game board
#   Output: 2D array, an updated game board, with the player number in the last row
def takeTurn(turn, board):
    
    # Inform player it is their turn
    print("\nPlayer %s what is your choice?" % turn)
    
    # player's action
    y = len(board[0])
    action = ""
    
    # continously prompt user for their action until they enter a column number
    while True:
        action = input("Please choose a column to place your piece in (1 - %s) or %s to save: " % (y,SAVE_FILE_ACTION))
        if not action in [str(i+1) for i in range(y)] and action == SAVE_FILE_ACTION:
                saveFile(board, turn)
                print("Player %s what is your choice?" % turn)
        elif action in [str(i+1) for i in range(y)]:
            update = updateBoard(int(action)-1, board, turn)
            if update:
                return [checkWinner(board,int(action)-1,turn),update]
        


#   saveFile() saves the current game board as a text file
#   Input: board, a 2D array, the current game bord
#   Output: none
def saveFile(board,turn):
    
    # open/write to save file
    saveFile = open(formatFileName(input("What game file would you like to save to? ")), "w")
    saveFile.write(parseBoard(board+[[str(turn)]]))
    print("File saved")
    
    # end function
    return
    

#   updateBoard() updates the current game board
#   Input: (col,board, turn) {col:[integer, current column number], board: [2D Array, current game board], turn: [integer, the number of the player whose turn it is]}
#   Output: 2D array, updated game board or false if the column was full
def updateBoard(col,board,turn):
    
    # Get and store the current column
    column = [board[i][col] for i in range(len(board))]
    
    
    
    if not BLANK_SPACE in column:
        print("That column is full.")
        return False
    
    
    # Get the number of the first row that does not have a BLANK_SPACE character
    try:
        rowNumber = column.index(next(filter(lambda x: x!=BLANK_SPACE,column))) - 1
    except:
        rowNumber = len(board) - 1

    
    # Get row number of first blank space and use it to update the game board 
    board[rowNumber][col] = PLAYER_TOKENS[turn-1]
    
    # return the updated game board
    return board

    



#    checkWinner() checks to if a player has won yet
#   Input: board, 2D array, gameboard
#   Output: boolean that conveys whether or not somebody has won
def checkWinner(board,col,turn):
    
    # current column
    column = [board[i][col] for i in range(len(board))]
    
    # current row number
    rowNumber = column.index(PLAYER_TOKENS[turn-1])
    
    # current row
    row = board[rowNumber]
    
    
    
    # regular diagonal
#    diagonal = [board[(rowNumber + i) % len(board)][(col+i) % len(board[0])] for i in range(len(board))]
    diagonal = {((rowNumber + i) % len(board),(col+i) % len(board[0])):board[(rowNumber + i) % len(board)][(col+i) % len(board[0])] for i in range(len(board))}
    
    
    # Counter diaognal = 
#    counterDiagonal = [board[(rowNumber + i) % len(board)][(col-i) % len(board[0])] for i in range(len(board))]
    counterDiagonal = {((rowNumber + i) % len(board),(col-i) % len(board[0])):board[(rowNumber + i) % len(board)][(col-i) % len(board[0])] for i in range(len(board))}
    
    
    # Match the row, column and diagonals against the 4 consectuive PLAYER_TOKENs, which signifies a win
    connectFour = (PLAYER_TOKENS[turn-1] *4)

#    print(diagonal,diagonal2)
#    print(counterDiagonal,[diagonal3[i] for i in sorted(diagonal3)])
    # if there is even one match, the game is over
    for i in ["".join(column),"".join(row),"".join([diagonal[i] for i in sorted(diagonal)]),"".join([counterDiagonal[i] for i in sorted(counterDiagonal)])]:
        if connectFour in i:
            return True
    return False

def main():
    
    # Whether or not the user wants to quit
    play = YES
    
    # Print welcome message
    print("Welcome to Connect Four\nThis game is for two players")
    
    # Retrieve board
    board = getBoard()
    
    # While the user has not opted to quit
    while play != NO:
        # load or create boarzd
        
        turn = int(board.pop()[0])

        # display the board
        print(displayBoard(board))
        winner  = False
        turnResult = [False ]

        # continously take their turns
        while not winner:
            turnResult= takeTurn(turn, board)
            board = turnResult[1]
            print(displayBoard(board))
            winner = turnResult[0]
            if winner:
                print("Player %s wins!" % turn)
            if BLANK_SPACE not in [board[i][j] for i in range(len(board)) for j in range(len(board[0]))]:
                print("There was a draw!")
                winner = True
            turn ^= SWITCH_PLAYER
            
        
        play = input("Would you like to play again (y/n): ")
        while not play in [YES,NO]:
            play = input("Would you like to play again (y/n): ")
        if play == YES:
            board = newBoard()

    
main()